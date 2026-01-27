# CourseWeave AI 🎓

An intelligent, multi-agent chatbot that helps university students plan their coursework based on career objectives. Built with LangChain, RAG, and deployed on Google Cloud Platform.

## 🚀 Features

- **Career-Aligned Course Recommendations**: Get personalized course suggestions based on your target role (Data Scientist, ML Engineer, etc.)
- **Automated Prerequisite Validation**: Intelligent checking of course prerequisites and co-requisites
- **Multi-Agent Architecture**: 
  - Course Planning Agent
  - Alumni Insights Agent
  - Analytics Agent
- **Real-Time Semester Availability**: Track when courses are offered (Fall/Spring)
- **24/7 Accessibility**: Instant guidance without scheduling constraints

## 📋 Prerequisites

- Python 3.11+
- Google Cloud Platform account with enabled services:
  - Cloud Run
  - Cloud Storage
  - Secret Manager
- Git

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/courseweave-ai.git
cd courseweave-ai
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
# OR using make
make install
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
# Edit .env with your GCP credentials and API keys
```

Required environment variables:
```
GCP_PROJECT_ID=your-project-id
GCP_REGION=us-central1
VECTOR_DB_ENDPOINT=your-vertex-ai-endpoint
OPENAI_API_KEY=your-openai-key  # Or other LLM provider
LANGCHAIN_API_KEY=your-langchain-key
```

### 5. Set Up GCP Resources
```bash
# Authenticate with GCP
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Run setup script
bash scripts/setup_gcp.sh
```

## Running Locally

### Start the API Server
```bash
# Using uvicorn directly
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

# OR using make
make run
```

API will be available at `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### Data Ingestion
```bash
# Scrape and process course catalog data
python scripts/ingest_data.py --university northeastern

# OR using make
make ingest
```

## Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# OR using make
make test
```

## 🐳 Docker Development
```bash
# Build image
docker build -f docker/Dockerfile -t CourseWeave-ai:latest .

# Run container
docker-compose -f docker/docker-compose.yml up

# OR using make
make docker-build
make docker-run
```

## ☁️ Deployment to GCP

### Option 1: Using Terraform (Recommended)
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### Option 2: Manual Deployment
```bash
# Deploy to Cloud Run
bash scripts/deploy.sh

# OR using make
make deploy
```

## 📊 Project Structure
```
src/
├── agents/          # Multi-agent implementations
├── data/            # Data scraping, preprocessing, loading
├── retrieval/       # RAG pipeline and vector search
├── api/             # FastAPI endpoints
└── utils/           # Configuration and utilities
```

## 🔧 Configuration

Agent and model configurations are in `configs/`:
- `agent_config.yaml`: Agent-specific parameters
- `model_config.yaml`: LLM and embedding model settings
- `gcp_config.yaml`: GCP service configurations

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [API Documentation](docs/api_documentation.md)
- [Deployment Guide](docs/deployment_guide.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## 👥 Team

- Sachin Sreekumar
- Nagashree Bommenahalli Kumaraswamy
- Vigneshwaran Jayaraman
- Kavin Priyadarrsan Murugesan
- Jogeashwini Srinivasan Ramesh
- Siddharth Mohapatra

## 🙏 Acknowledgments

- Northeastern University LLMOps Course
- LangChain Framework
- Google Cloud Platform

## 📧 Contact

Project Link: [https://github.com/yourusername/courseweave-ai](https://github.com/yourusername/CourseWeave-ai)

---

**Crafted with ❤️ for University students, by University students**
