import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATABASE_PATH = PROJECT_ROOT / "companion.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nexus_raw_data (
            endpoint TEXT NOT NULL,
            record_id TEXT NOT NULL,
            name TEXT,
            category TEXT,
            json_data TEXT NOT NULL,
            json_hash TEXT,
            last_synced TEXT NOT NULL,
            is_removed INTEGER NOT NULL DEFAULT 0,
            removed_at TEXT,
            PRIMARY KEY (endpoint, record_id)
        )
    """)

    add_column_if_missing(cursor, "nexus_raw_data", "name", "TEXT")
    add_column_if_missing(cursor, "nexus_raw_data", "category", "TEXT")
    add_column_if_missing(cursor, "nexus_raw_data", "json_hash", "TEXT")
    add_column_if_missing(cursor, "nexus_raw_data", "is_removed", "INTEGER NOT NULL DEFAULT 0")
    add_column_if_missing(cursor, "nexus_raw_data", "removed_at", "TEXT")

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_nexus_endpoint
        ON nexus_raw_data(endpoint)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_nexus_category
        ON nexus_raw_data(category)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_nexus_name
        ON nexus_raw_data(name)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_nexus_removed
        ON nexus_raw_data(is_removed)
    """)

    connection.commit()
    connection.close()


def add_column_if_missing(cursor, table_name, column_name, column_definition):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    existing_column_names = [column[1] for column in columns]

    if column_name not in existing_column_names:
        cursor.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_definition}"
        )