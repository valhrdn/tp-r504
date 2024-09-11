def puissance(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Only integers are allowed")
    if b < 0:
        raise ValueError("Negative exponents are not supported")
    result = 1
    for _ in range(b):
        result *= a
    return result
