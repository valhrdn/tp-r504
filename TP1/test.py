import pytest
import fonctions as f

def test_1():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4
    assert f.puissance(5, 0) == 1
    assert f.puissance(10, 1) == 10
    assert f.puissance(0, 3) == 0

def test_2():
    assert f.puissance(-2, 3) == -8
    assert f.puissance(-2, 2) == 4
    assert f.puissance(-5, 0) == 1
    assert f.puissance(-10, 1) == -10
    assert f.puissance(-3, -2) == 1 / 9  # Puissance négative

