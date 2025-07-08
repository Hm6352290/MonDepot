# Fonction à tester
def multiplaction(a, b):
    return a * b

# Tests simples sans utiliser unittest.TestCase
def test_multiplaction_positive():
    assert multiplaction(3, 4) == 12

def test_multiplaction_zero():
    assert multiplaction(0, 5) == 0

def test_multiplaction_negative():
    assert multiplaction(-3, 4) == -12

def test_multiplaction_both_negative():
    assert multiplaction(-2, -5) == 10

def test_multiplaction_float():
    assert multiplaction(2.5, 4) == 10.0

if __name__ == "__main__":
    test_multiplaction_positive()
    test_multiplaction_zero()
    test_multiplaction_negative()
    test_multiplaction_both_negative()
    test_multiplaction_float()
    print("Tous les tests sont passés ")
