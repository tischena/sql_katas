import sqlite3
import pytest
from src.main import cumulative_sum

@pytest.fixture
def test_get_db(tmp_path):
    db = tmp_path / "my_test.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE income (
            date_id DATE,
            income INTEGER
        );

        INSERT INTO income VALUES
        ('2025-01-01', 150),
        ('2025-01-02', 100),
        ('2025-01-03', 150),
        ('2025-01-04', 50),
        ('2025-01-05', 70)
    """)

    conn.commit()
    conn.close()

    return str(db)
    
def test_cumulative_sum(test_get_db):
    result = cumulative_sum(test_get_db)

    expected = [
        ('2025-01-01', 150, 150),
        ('2025-01-02', 100, 250),
        ('2025-01-03', 150, 400),
        ('2025-01-04', 50,	450),
        ('2025-01-05', 70,	520)
    ]

    assert result == expected
