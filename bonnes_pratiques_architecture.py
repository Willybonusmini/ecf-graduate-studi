# --- Module DE GESTION DE PRIX (APPLICATION CLEAN CODE) ---

# 1. Constantes (Définies en premier)
Taux_TVA_STANDARD = 0.20

#2. Fonctions (Responsabilité unique et nomenclature explicite)
def calculer_montant_tva(prix_hors_taxe):
    """
    Calcule le montant de la taxe en se basant sur le taux standard.
    Note architecturale: Isoler ce calcul permet de modifier la logique de TVA 
    sans impacter la logique de facturation globale.
    """
    return prix_hors_taxe * Taux_TVA_STANDARD

def calculer_prix_ttc(prix_hors_taxe):
    """
    Calcule le prix final TTC en intégrant la TVA.
    """
    # Application du principe DRY en appelant la fonction dédiée
    montant_tva = calculer_montant_tva(prix_hors_taxe)
    return prix_hors_taxe + montant_tva

#. Exécution[cite: 1]
prix_produit = 100.0  # Prix de base du produit
prix_final = calculer_prix_ttc(prix_produit)

#Les sauts de ligne séparent les blocs logiques pour une meilleure lisibilité[cite 1]
print(f"Prix HT : {prix_produit} €")
print(f"Prix TTC : {prix_final} €)")