def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
