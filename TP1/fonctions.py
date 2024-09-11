def puissance(a, b):
    """
    Calcule a élevé à la puissance b.
    :param a: Base (entier)
    :param b: Exposant (entier)
    :return: Résultat de a ** b
    :raises TypeError: Si a ou b ne sont pas des entiers
    """
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")
    return a ** b

