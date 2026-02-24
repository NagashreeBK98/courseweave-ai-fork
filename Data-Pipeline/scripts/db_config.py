"""
Database connection configuration.
Reads from environment variables — never hardcode credentials.
"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

DB_CONFIG = {
    "host":     os.getenv("DB_HOST", "localhost"),
    "port":     int(os.getenv("DB_PORT", 5432)),
    "dbname":   os.getenv("DB_NAME", "courseweave"),
    "user":     os.getenv("DB_USER", ""),
    "password": os.getenv("DB_PASSWORD", ""),
}


def get_connection():
    """Return a live psycopg2 connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
        logger.info("DB connection established.")
        return conn
    except psycopg2.OperationalError as e:
        logger.error("Failed to connect to database: %s", e)
        raise