# --- Module De Facturation (ClEAN CODE) ---

#X Mauvais CODE (Violation du principe DRY, noms génériques, responsabilités multiples)
# def calc(a, b):
#     res = a * b
#     t = res * 0.20
#     return res + t

# Bon CODE (Application stricte du Clean Code)

#1. Constantes (Ordre logique : Constantes -> Fonctions -> Exécution)
TAUX_TVA = 0.20

#2. Fonctions (Responsabilité unique et noms explicites)
def calculer_prix_hors_taxe(prix_unitaire, quantite):
    """Calcule le montat total hors taxe pour un article."""
    return prix_unitaire * quantite

def calculer_montant_ttc(prix_hors_taxe):
    """Applique le taux de TVA en vigueur au prix hors taxe."""
    montant_tva = prix_hors_taxe * TAUX_TVA
    return prix_hors_taxe + montant_tva
#3. Exécution
prix_unitaire_article = 50.0  # Prix unitaire de l'article
quantite_achetee = 3          # Quantité d'articles achetés

#traitement modulaire
total_ht = calculer_prix_hors_taxe(prix_unitaire_article, quantite_achetee)
total_ttc = calculer_montant_ttc(total_ht)

#Ajout de sauts de ligne pour séparer les blocs logiques et améliorer la lisibilité[cite: 1]
print(f"Total HT : {total_ht}€")
print(f"Total TTC : {total_ttc} €)")



