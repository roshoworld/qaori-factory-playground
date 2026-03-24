from src.utils import calculate_discount


def test_gold_discount():
    assert calculate_discount(100.0, "gold") == 80.0


def test_silver_discount():
    assert calculate_discount(100.0, "silver") == 90.0


def test_bronze_discount():
    assert calculate_discount(100.0, "bronze") == 95.0


def test_unknown_customer():
    assert calculate_discount(100.0, "unknown") == 100.0
