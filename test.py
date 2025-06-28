import unittest

# Fonction à tester
def addition(a, b):
    return a + b

# Classe de test
class TestAddition(unittest.TestCase):  # Il manquait "class" au début
    # Définition du code de la méthode de test
    def test_addition(self):
        # Assertions pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(7, 8), 15)
        self.assertEqual(addition(9, 3), 12)

# Définition d’un objet de test
test_addition = unittest.TestLoader().loadTestsFromTestCase(TestAddition)

# Exécution du test
unittest.TextTestRunner().run(test_addition)
