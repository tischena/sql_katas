import sqlite3
import pytest
from src.main import salary_bigger_managers

@pytest.fixture
def test_get_db(tmp_path):
    db = tmp_path / "my_test.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE employee_salary (
            id_employee INTEGER,
            salary INTEGER,
            id_manager INTEGER
        );

        INSERT INTO employee_salary VALUES
        (10, 155000, 11),
        (11, 100000, 13),
        (12, 95000,	13),
        (13, 110000, 14),
        (14, 150000, null);
    """)

    conn.commit()
    conn.close()

    return str(db)
    
def test_bigger_salary(test_get_db):
    result = salary_bigger_managers(test_get_db)

    expected = [
        (10, 155000, 11)
    ]

    assert result == expected
