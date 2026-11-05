"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a pick-list quantity string into a non-negative integer.

    Raises ValueError for non-integer input or negative values.
    """
    qty = int(value.strip())
    if qty < 0:
        raise ValueError(f"Quantity must be non-negative, got {qty}")
    return qty
