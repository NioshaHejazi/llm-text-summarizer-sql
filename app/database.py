import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS summaries (
                id SERIAL PRIMARY KEY,
                input_text TEXT NOT NULL,
                summary_text TEXT NOT NULL,
                tags TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            conn.commit()

def insert_summary(input_text, summary_text, tags=None):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO summaries (input_text, summary_text, tags)
            VALUES (%s, %s, %s)
            """, (input_text, summary_text, tags))
            conn.commit()
