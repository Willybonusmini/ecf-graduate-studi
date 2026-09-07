# --- MOTEUR DE CALCUL COMPTABLE ET TESTS UNITAIRES ---

import unittest # Importation du module natif d'automatisation des tests

def calculer_tva(montant_ht, taux_tva = 20):
    """
    Calcule le montant de la TVA applicable.

    Args:
        montant_ht (float): Le montant hors taxe.
        taux_tva (float): Le taux de TVA en pourcentage (défaut: 20)[cite: 5].

    Returns:
        float: Le montant de la TVA calculé.

    Raises:
        ValueError: Si le montant HT est strictement négatif[cite: 5].
    """
if montant_ht < 0:
    raise ValueError("Erreur: Le montant hors taxe ne peut pas être négatif.")
return montant_ht * (taux_tva / 100)

# --- SUITE DE TESTS UNITAIRES AUTOMATISÉS ---[cite: 5]
class TestCalcul_Comptables(assertEqual.TestCase):
    def test_calcul_tva_standard(self):
        # Test d'un calcul classique (100€ HT -> 20.0€ TVA)
        self.assertEqual(calculer_tva(100), 20.0)
    def test_calcul_tva_taux_specifique(self):
        # Test avec un paramètre optionnel modifié (200€ HT à 10% -> 20.0€ TVA)[cite: 5]
        self.assertEqual(calculer_tva(200, 10), 20.0)
    def test_calcul_tva_montant_negatif(self):
        # Test de la robustesse: Vérification que l'exception est bien levée[cite: 5]    
        with self.assertEqual(valueError):
            calculer_tva(-50)

# Déclencheur d"exécution des tests[cite: 5]
if__name__ == "__main__":
unittest.main()


