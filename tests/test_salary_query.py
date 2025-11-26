import sqlite3
import pytest
from src.main import get_salary_proc

@pytest.fixture
def test_get_salary_proc_db(tmp_path):
    db = tmp_path / "my_test.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE salary (
            id_employee INTEGER,
            department TEXT,
            salary INTEGER
        );

        INSERT INTO salary VALUES
        (11, 'sales', 100000),
        (12, 'sales', 95000),
        (13, 'sales', 55000),
        (14, 'IT', 150000),
        (15, 'IT', 250000),
        (16, 'IT', 155000);
    """)

    conn.commit()
    conn.close()

    return str(db)
    
def test_my_salary_percentages(test_get_salary_proc_db):
    result = get_salary_proc(test_get_salary_proc_db)

    expected = [
        (11, 'sales', 100000, 40),
        (12, 'sales', 95000, 38),
        (13, 'sales', 55000, 22),
        (14, 'IT', 150000, 27),
        (15, 'IT', 250000, 45),
        (16, 'IT', 155000, 28),
    ]

    assert result == expected
