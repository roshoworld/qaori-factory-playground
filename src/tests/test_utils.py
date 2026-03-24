# As a senior QA engineer, before committing, I would first ensure the source file
# src/utils.py is syntactically valid by running:
# python -m py_compile src/utils.py
# This adheres to IRON RULE M: PYTHON SYNTAX MUST BE VALIDATED BEFORE COMMIT.

import pytest
from src.utils import calculate_discount

# Using pytest.approx for float comparisons to account for potential floating-point inaccuracies.
# The current implementation of calculate_discount applies a fixed discount percentage
# for each customer type, regardless of the price tiers (price > 100, price > 50, else).
# These tests are designed to validate this specific behavior.

@pytest.mark.parametrize(
    "price, customer_type, expected_discounted_price",
    [
        # --- Gold Customer (20% discount) ---
        # Arrange: price > 100
        (120.0, "gold", 120.0 - (120.0 * 0.20)),
        # Arrange: price == 100 (boundary condition)
        (100.0, "gold", 100.0 - (100.0 * 0.20)),
        # Arrange: 50 < price < 100
        (90.0, "gold", 90.0 - (90.0 * 0.20)),
        # Arrange: price == 50 (boundary condition)
        (50.0, "gold", 50.0 - (50.0 * 0.20)),
        # Arrange: price < 50
        (30.0, "gold", 30.0 - (30.0 * 0.20)),
        # Arrange: price == 0
        (0.0, "gold", 0.0),
        # Arrange: price slightly above 100
        (100.01, "gold", 100.01 - (100.01 * 0.20)),
        # Arrange: price slightly below 100
        (99.99, "gold", 99.99 - (99.99 * 0.20)),
        # Arrange: price slightly above 50
        (50.01, "gold", 50.01 - (50.01 * 0.20)),
        # Arrange: price slightly below 50
        (49.99, "gold", 49.99 - (49.99 * 0.20)),
        # Arrange: Negative price (function does not explicitly handle, but should follow logic)
        (-10.0, "gold", -10.0 - (-10.0 * 0.20)),

        # --- Silver Customer (10% discount) ---
        # Arrange: price > 100
        (120.0, "silver", 120.0 - (120.0 * 0.10)),
        # Arrange: price == 100 (boundary condition)
        (100.0, "silver", 100.0 - (100.0 * 0.10)),
        # Arrange: 50 < price < 100
        (90.0, "silver", 90.0 - (90.0 * 0.10)),
        # Arrange: price == 50 (boundary condition)
        (50.0, "silver", 50.0 - (50.0 * 0.10)),
        # Arrange: price < 50
        (30.0, "silver", 30.0 - (30.0 * 0.10)),
        # Arrange: price == 0
        (0.0, "silver", 0.0),

        # --- Bronze Customer (5% discount) ---
        # Arrange: price > 100
        (120.0, "bronze", 120.0 - (120.0 * 0.05)),
        # Arrange: price == 100 (boundary condition)
        (100.0, "bronze", 100.0 - (100.0 * 0.05)),
        # Arrange: 50 < price < 100
        (90.0, "bronze", 90.0 - (90.0 * 0.05)),
        # Arrange: price == 50 (boundary condition)
        (50.0, "bronze", 50.0 - (50.0 * 0.05)),
        # Arrange: price < 50
        (30.0, "bronze", 30.0 - (30.0 * 0.05)),
        # Arrange: price == 0
        (0.0, "bronze", 0.0),

        # --- Unknown Customer Type (0% discount) ---
        # Arrange: various prices with unrecognized customer types
        (120.0, "platinum", 120.0),
        (75.0, "guest", 75.0),
        (25.0, "new", 25.0),
        (0.0, "unknown", 0.0),
        (100.0, "", 100.0), # Empty string customer type
    ]
)
def test_calculate_discount_valid_inputs(price: float, customer_type: str, expected_discounted_price: float):
    """
    Verify the calculate_discount function returns the correct discounted price
    for various customer types and price points, including boundary conditions.
    """
    # Act
    actual_discounted_price = calculate_discount(price, customer_type)

    # Assert
    assert actual_discounted_price == pytest.approx(expected_discounted_price)


@pytest.mark.parametrize(
    "price, customer_type, expected_discounted_price",
    [
        # Arrange: Invalid customer_type (non-string)
        (100.0, None, 100.0),
        (50.0, 123, 50.0),
        (20.0, True, 20.0),
        (150.0, ["gold"], 150.0),
        (75.0, {"type": "silver"}, 75.0),
    ]
)
def test_calculate_discount_invalid_customer_type_inputs(price: float, customer_type, expected_discounted_price: float):
    """
    Test scenarios where the customer_type input is not a string or is an unexpected type.
    The function should default to no discount (discount = 0) in these cases.
    """
    # Act
    actual_discounted_price = calculate_discount(price, customer_type)

    # Assert
    assert actual_discounted_price == pytest.approx(expected_discounted_price)


@pytest.mark.parametrize(
    "price, customer_type",
    [
        # Arrange: Non-numeric price input (type hint violation, but Python allows)
        ("100", "gold"),
        (None, "silver"),
        ([50.0], "bronze"),
    ]
)
def test_calculate_discount_invalid_price_type_inputs(price, customer_type):
    """
    Test scenarios where the price input is not a float/int.
    The function should raise a TypeError due to arithmetic operations on incompatible types.
    """
    # Act & Assert
    with pytest.raises(TypeError):
        calculate_discount(price, customer_type)
