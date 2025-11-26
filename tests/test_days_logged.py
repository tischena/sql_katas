import sqlite3
import pytest
from src.main import days_logged

@pytest.fixture
def test_get_db(tmp_path):
    db = tmp_path / "my_test.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE logs (
            id INTEGER,
            status TEXT,
            action_date DATE
        );

        INSERT INTO logs VALUES
        (1, 'start', '2025-01-01'),
        (2, 'start', '2025-01-02'),
        (1, 'end', '2025-01-03'),
        (2, 'end', '2025-01-18')
    """)

    conn.commit()
    conn.close()

    return str(db)
    
def test_days_logged(test_get_db):
    result = days_logged(test_get_db)

    expected = [
        (1, 2),
        (2, 16)
    ]

    assert result == expected
