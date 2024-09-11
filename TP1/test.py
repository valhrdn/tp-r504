import pytest
import fonctions as f

def test_positive_exponents():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4
    assert f.puissance(5, 0) == 1  # Test avec exposant égal à zéro
    assert f.puissance(0, 5) == 0  # Test avec base égale à zéro

def test_negative_exponents():
    # Exposants négatifs ne sont pas supportés par la fonction actuelle, mais vous pouvez tester ce comportement
    with pytest.raises(ValueError):  # Remplacez par le type d'exception approprié si nécessaire
        f.puissance(2, -3)

def test_large_numbers():
    assert f.puissance(10, 10) == 10000000000
    assert f.puissance(123456, 2) == 123456**2

# Ajouter d'autres tests selon les besoins

