import unittest

def sub(a, b):
    return a - b

# Fonctions de test individuelles
def test_sub_positive():
    assert sub(5, 3) == 2

def test_sub_negative():
    assert sub(3, 5) == -2

def test_sub_zero():
    assert sub(0, 0) == 0

def test_sub_mixed():
    assert sub(-5, 5) == -10

if __name__ == "__main__":
    test_sub_positive()
    test_sub_negative()
    test_sub_zero()
    test_sub_mixed()
    print("Tous les tests ont réussi ")