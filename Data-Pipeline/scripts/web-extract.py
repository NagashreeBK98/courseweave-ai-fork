"""
CourseWeave.ai - Web Data Extraction Pipeline
Northeastern University Course Catalog → Pinecone

Production-ready script for Apache Airflow DAG integration.
- Config-driven via JSON in GCS
- Structured error logging to GCS
- Output snapshots to GCS
- Upsert to Pinecone vector store
"""

import os
import re
import json
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google.cloud import storage
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec


# ============================================================================
# CONFIGURATION
# ============================================================================

load_dotenv()

GCS_BUCKET = os.getenv("GCS_BUCKET")
GCS_CONFIG_PATH = os.getenv("GCS_CONFIG_PATH", "config/course_urls.json")
GCS_ERROR_LOG_FOLDER = "error_logs"
GCS_WEB_OUTPUT_FOLDER = "web_output"
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"
EMBEDDING_DIMENSION = 384

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

gcs_client = storage.Client()
bucket = gcs_client.bucket(GCS_BUCKET)


# ============================================================================
# ERROR LOGGING
# ============================================================================

def log_error_to_gcs(course, stage, error_message):
    """Log structured error to GCS as a JSON file."""
    timestamp = datetime.now(timezone.utc).isoformat()
    error_obj = {
        "course": course,
        "stage": stage,
        "error_message": str(error_message),
        "timestamp": timestamp
    }
    filename = f"{GCS_ERROR_LOG_FOLDER}/web_{course}_{timestamp}.json"
    blob = bucket.blob(filename)
    blob.upload_from_string(json.dumps(error_obj, indent=2), content_type="application/json")


# ============================================================================
# CONFIG LOADER
# ============================================================================

def load_config_from_gcs():
    """Load course URLs config JSON from GCS."""
    blob = bucket.blob(GCS_CONFIG_PATH)
    if not blob.exists():
        raise FileNotFoundError(f"Config file not found at gs://{GCS_BUCKET}/{GCS_CONFIG_PATH}")
    data = blob.download_as_text()
    return json.loads(data)


# ============================================================================
# PARSING FUNCTIONS
# ============================================================================

def parse_course_header(header_text):
    """Parse header like 'IE 2310. Introduction to Industrial Engineering. (4 Hours)'"""
    match = re.match(
        r"([A-Z]+\s\d+)\.\s+(.+?)\.\s+\((\d+(?:-\d+)?)\s+Hours?\)",
        header_text.strip()
    )
    if match:
        return {
            "course_code": match.group(1),
            "title": match.group(2).strip(),
            "credits": match.group(3)
        }
    return None


def parse_prerequisites(prereq_text):
    """Parse prerequisite string into structured format."""
    if not prereq_text:
        return [], None

    prereq_text = prereq_text.strip()
    prereq_text = re.sub(r"(\d)with", r"\1 with", prereq_text)
    prereq_text = re.sub(r"-\s*or([A-Z])", r"- or \1", prereq_text)
    prereq_text = re.sub(r"\s+", " ", prereq_text).strip()

    has_graduate_admission = False
    if "graduate program admission" in prereq_text.lower():
        has_graduate_admission = True
        prereq_text = re.sub(
            r"\s*or\s+graduate program admission", "", prereq_text, flags=re.IGNORECASE
        ).strip()

    if not prereq_text:
        return [], "graduate_program_admission" if has_graduate_admission else None

    and_groups = [g.strip().strip("()").strip() for g in prereq_text.split(";")]

    prerequisites = []
    for group in and_groups:
        if not group:
            continue
        or_parts = re.split(r"\s+or\s+", group)
        or_list = []
        for part in or_parts:
            part = part.strip().strip("()").strip()
            match = re.match(
                r"([A-Z]+\s\d+)\s+with a minimum grade of\s+([A-Za-z][+-]?)",
                part
            )
            if match:
                or_list.append({"course": match.group(1), "min_grade": match.group(2)})
            else:
                code_match = re.match(r"([A-Z]+\s\d+)", part)
                if code_match:
                    or_list.append({"course": code_match.group(1), "min_grade": None})
        if or_list:
            prerequisites.append(or_list)

    graduate_alt = "graduate_program_admission" if has_graduate_admission else None
    return prerequisites, graduate_alt


def parse_corequisites(coreq_text):
    """Parse corequisite string into a list of course codes."""
    if not coreq_text:
        return []
    return re.findall(r"[A-Z]+\s\d+", coreq_text)


def parse_attributes(attr_text):
    """Parse attributes string into a list."""
    if not attr_text:
        return []
    return [a.strip() for a in attr_text.split(",") if a.strip()]


# ============================================================================
# COURSE BLOCK PARSER
# ============================================================================

def parse_course_block(block, source_url):
    """Parse a single courseblock div into document structure."""
    title_elem = block.find("p", class_="courseblocktitle")
    if not title_elem:
        return None

    header_text = title_elem.get_text(strip=True)
    header_text = re.sub(r"\u200b|\u00a0", " ", header_text)
    header_text = re.sub(r"\s+", " ", header_text).strip()

    header = parse_course_header(header_text)
    if not header:
        return None

    desc_elem = block.find("p", class_="cb_desc")
    description = desc_elem.get_text(strip=True) if desc_elem else ""

    prereq_text, coreq_text, attr_text = "", "", ""
    for field in block.find_all("p", class_="courseblockextra"):
        field_text = field.get_text(strip=True)
        field_text = re.sub(r"\u200b|\u00a0", " ", field_text)
        if field_text.startswith("Prerequisite(s):"):
            prereq_text = field_text.replace("Prerequisite(s):", "").strip()
        elif field_text.startswith("Corequisite(s):"):
            coreq_text = field_text.replace("Corequisite(s):", "").strip()
        elif field_text.startswith("Attribute(s):"):
            attr_text = field_text.replace("Attribute(s):", "").strip()

    prerequisites, graduate_alt = parse_prerequisites(prereq_text)
    corequisites = parse_corequisites(coreq_text)
    attributes = parse_attributes(attr_text)
    dept = header["course_code"].split()[0]

    page_content = f"{header['course_code']}. {header['title']}. {description}"

    metadata = {
        "course_code": header["course_code"],
        "title": header["title"],
        "department": dept,
        "source": "web_catalog",
        "credits": header["credits"],
        "prerequisites": prerequisites,
        "corequisites": corequisites,
        "attributes": attributes,
        "source_url": source_url,
    }

    if graduate_alt:
        metadata["graduate_admission_alternative"] = True
    if prereq_text:
        metadata["prerequisites_raw"] = prereq_text

    return {"page_content": page_content, "metadata": metadata}


# ============================================================================
# PAGE EXTRACTION
# ============================================================================

def fetch_and_extract_courses(url):
    """Fetch a catalog page and extract all courses."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    content_area = soup.find("div", class_="sc_sccoursedescs")
    if not content_area:
        content_area = soup

    course_blocks = content_area.find_all("div", class_="courseblock")

    courses = []
    for block in course_blocks:
        course = parse_course_block(block, url)
        if course:
            courses.append(course)

    return courses


# ============================================================================
# DOCUMENT PREPARATION
# ============================================================================

def courses_to_documents(courses):
    """Convert parsed courses to LangChain Documents with serialized metadata."""
    documents = []
    for course in courses:
        doc = Document(
            page_content=course["page_content"],
            metadata=course["metadata"]
        )
        if doc.metadata.get("prerequisites"):
            doc.metadata["prerequisites"] = json.dumps(doc.metadata["prerequisites"])
        if doc.metadata.get("corequisites"):
            doc.metadata["corequisites"] = json.dumps(doc.metadata["corequisites"])
        if doc.metadata.get("attributes"):
            doc.metadata["attributes"] = json.dumps(doc.metadata["attributes"])
        documents.append(doc)
    return documents


# ============================================================================
# GCS SNAPSHOT WRITER
# ============================================================================

def write_snapshot_to_gcs(course_code, courses):
    """Write extracted course data as a JSON snapshot to GCS."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    filename = f"{GCS_WEB_OUTPUT_FOLDER}/{course_code}_{timestamp}.json"
    blob = bucket.blob(filename)
    blob.upload_from_string(json.dumps(courses, indent=2), content_type="application/json")


# ============================================================================
# MAIN PIPELINE
# ============================================================================

def run_pipeline():
    """Main pipeline execution."""

    # Load config
    try:
        course_config = load_config_from_gcs()
    except Exception as e:
        log_error_to_gcs("GLOBAL", "config_loading", e)
        raise

    # Initialize embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    # Initialize Pinecone
    pc = Pinecone(api_key=PINECONE_API_KEY)
    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=EMBEDDING_DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    # Process each course
    pipeline_results = {"success": [], "failed": []}

    for entry in course_config:
        course_code = entry["course"]
        url = entry["url"]

        # Stage 1: Fetch and parse HTML
        try:
            courses = fetch_and_extract_courses(url)
        except Exception as e:
            log_error_to_gcs(course_code, "html_fetch_and_parse", e)
            pipeline_results["failed"].append(course_code)
            continue

        if not courses:
            log_error_to_gcs(course_code, "html_parsing", "No courses extracted from page")
            pipeline_results["failed"].append(course_code)
            continue

        # Stage 2: Write snapshot to GCS
        try:
            write_snapshot_to_gcs(course_code, courses)
        except Exception as e:
            log_error_to_gcs(course_code, "gcs_snapshot_write", e)

        # Stage 3: Convert to LangChain Documents
        try:
            documents = courses_to_documents(courses)
        except Exception as e:
            log_error_to_gcs(course_code, "document_conversion", e)
            pipeline_results["failed"].append(course_code)
            continue

        # Stage 4: Upsert to Pinecone
        try:
            doc_ids = [f"web_{doc.metadata['course_code'].replace(' ', '_')}" for doc in documents]
            PineconeVectorStore.from_documents(
                documents=documents,
                embedding=embeddings,
                index_name=PINECONE_INDEX_NAME,
                ids=doc_ids
            )
            pipeline_results["success"].append({"course": course_code, "count": len(documents)})
        except Exception as e:
            log_error_to_gcs(course_code, "pinecone_upsert", e)
            pipeline_results["failed"].append(course_code)
            continue

    # Write pipeline summary to GCS
    summary = {
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "total_courses_configured": len(course_config),
        "successful": len(pipeline_results["success"]),
        "failed": len(pipeline_results["failed"]),
        "details": pipeline_results
    }
    summary_blob = bucket.blob(
        f"{GCS_WEB_OUTPUT_FOLDER}/pipeline_summary_{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')}.json"
    )
    summary_blob.upload_from_string(json.dumps(summary, indent=2), content_type="application/json")

    return summary


if __name__ == "__main__":
    result = run_pipeline()
    print(json.dumps(result, indent=2))