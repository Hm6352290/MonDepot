def factorielle(n):
    """
    Calcule la factorielle d'un nombre entier positif n.
    
    Args:
    n (int): Nombre entier positif.
    
    Returns:
    int: Factorielle de n.
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les entiers négatifs.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
#Tests unitaires sans classe pour la fonction

def test_factorielle_positive():
    assert factorielle(5) == 120  # 5! = 5*4*3*2*1

def test_factorielle_zero():
    assert factorielle(0) == 1    # 0! = 1

def test_factorielle_un():
    assert factorielle(1) == 1    # 1! = 1

def test_factorielle_negative():
    try:
        factorielle(-3)
        assert False, "Une exception aurait dû être levée pour n négatif"
    except ValueError:
        pass  # C'est le comportement attendu

if __name__ == "__main__":
    test_factorielle_positive()
    test_factorielle_zero()
    test_factorielle_un()
    test_factorielle_negative()
    print("Tous les tests sont passés ")
