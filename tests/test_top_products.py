import sqlite3
import pytest
from src.main import top_products

@pytest.fixture
def test_get_db(tmp_path):
    db = tmp_path / "my_test.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE log_sales (
            date_id DATE,
            product TEXT
        );

        INSERT INTO log_sales VALUES
        ('2025-01-01',	'персик'),
        ('2025-01-01',	'персик'),
        ('2025-01-01',	'яблоко'),
        ('2025-01-02',	'апельсин'),
        ('2025-01-02',	'апельсин'),
        ('2025-01-02',	'груша'),
        ('2025-01-02',	'груша'),
        ('2025-01-02',	'слива'),
        ('2025-01-03',	'вишня');
    """)

    conn.commit()
    conn.close()

    return str(db)
    
def test_top_products(test_get_db):
    result = top_products(test_get_db)

    expected = [
        ('2025-01-01',	'персик'),
        ('2025-01-02',	'апельсин'),
        ('2025-01-02',	'груша'),
        ('2025-01-03',	'вишня'),
    ]

    assert result == expected
