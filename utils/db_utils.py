import os
import sqlite3
import pandas as pd

DB_PATH = os.path.join("data", "processed", "ecom.db")

def get_connection():
    """Return SQLite connection."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def run_query(query):
    """Execute SQL query and return a DataFrame."""
    conn = get_connection()
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        conn.close()
        raise Exception(f"SQL execution error: {e}")
    conn.close()
    return df
