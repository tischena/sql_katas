import sqlite3
from pathlib import Path

def run_query(db_path: str, sql_file: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = Path(sql_file).read_text(encoding="utf-8")
    cur.execute(query)

    result = cur.fetchall()
    conn.close()

    return result

def get_salary_proc(db_path: str):
    return run_query(db_path, "queries/get_salary_proc.sql")

def salary_bigger_managers(db_path: str):
    return run_query(db_path, "queries/salary_bigger_managers.sql")

def cumulative_sum(db_path: str):
    return run_query(db_path, "queries/cumulative_sum.sql")

def moving_average(db_path: str):
    return run_query(db_path, "queries/moving_average.sql")

def days_logged(db_path: str):
    return run_query(db_path, "queries/days_logged.sql")

def top_products(db_path: str):
    return run_query(db_path, "queries/top_products.sql")

def top3_and_else(db_path: str):
    return run_query(db_path, "queries/top3_and_else.sql")