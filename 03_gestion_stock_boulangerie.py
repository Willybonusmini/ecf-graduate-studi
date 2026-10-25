# -*- coding: utf-8 -*-
"""
Module: Gestion de Stock (Cas Pratique: Boulangerie Dupain)
Objectif: Démonstration des structures fondamentales (Variables, Fonctions, Boucles, Conditions)
"""

def verifier_stock(ingredients: dict, seuil_critique: int) -> None:
    """
    Fonction qui itère sur un inventaire et lève une alerte si le stock est bas.
    """
    print("--- Rapport d'Inventaire ---")
    # Boucle (structure de répétition) pour analyser chaque ingrédient
    for nom, quantite in ingredients.items():
        # Condition (structure conditionnelle) pour l'alerte
        if quantite <= seuil_critique:
            print(f"[ALERTE] Stock critique pour : {nom} ({quantite} unités restantes)")
        else:
            print(f"[OK] Stock suffisant pour : {nom} ({quantite} unités)")

if __name__ == "__main__":
    # Déclaration des variables (Structure de données structurée)
    inventaire_boulangerie = {
        "Farine (kg)": 150,
        "Levure (g)": 500,
        "Sucre (kg)": 5,
        "Beurre (kg)": 2
    }
    
    # Appel de la fonction avec un seuil d'alerte défini à 10
    verifier_stock(inventaire_boulangerie, 10)