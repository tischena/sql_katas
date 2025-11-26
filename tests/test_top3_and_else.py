import sqlite3
import pytest
from src.main import top3_and_else

@pytest.fixture
def test_get_db(tmp_path):
    db = tmp_path / "my_test.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE sales (
            date_id DATE,
            product TEXT,
            quantity INTEGER
        );

        INSERT INTO sales VALUES
        ('2025-01-01',	'персик', 15),
        ('2025-01-01',	'яблоко', 23),
        ('2025-01-01',	'груша', 17),
        ('2025-01-02',	'апельсин', 50),
        ('2025-01-02',	'слива', 11),
        ('2025-01-02',	'персик', 15),
        ('2025-01-02',	'вишня', 12),
        ('2025-01-02',	'яблоко', 9);
    """)

    conn.commit()
    conn.close()

    return str(db)
    
def test_top3_and_else(test_get_db):
    result = top3_and_else(test_get_db)

    expected = [
        ('апельсин', 50),
        ('яблоко', 32),
        ('персик', 30),
        ('другие', 40)
    ]

    assert result == expected
