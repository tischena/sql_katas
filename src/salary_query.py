import sqlite3
from pathlib import Path

def get_salary_proc(db_path: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = Path("queries/get_salary_proc.sql").read_text()
    cur.execute(query)

    result = cur.fetchall()
    conn.close()
    return result
