import unittest
# Créez une fonction simple à tester.
def addition(a, b):
    return a + b  # Correction ici : on enlève le -1

# TDD : développement dirigé par les tests (Test Driven Development).
# Écrivez une méthode de test pour la fonction addition.
def test_addition():
    # appeler la fonction à tester
    result = addition(3, 5)
    # Assertion pour vérifier si le résultat est au résultat attendu
    assert result == 8, f"Le résultat attendu est 8, mais le résultat obtenu est {result}"
    
    result = addition(3, 9)
    assert result == 12, f"Le résultat attendu est 12, mais le résultat obtenu est {result}"

# Créez une suite de tests et exécutez-les.
test_addition()
print("Test terminé ..... ")
