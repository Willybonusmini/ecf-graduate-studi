# -*- coding: utf-8 -*-
"""
Module: Logique Booléenne et Structures de Contrôle
"""

def evaluer_alarme_ou(capteur_mvt1: bool, capteur_mvt2: bool, detecteur_fumee: bool) -> str:
    # L'opérateur OU renvoie vrai si au moins une condition est vraie
    if capteur_mvt1 or capteur_mvt2 or detecteur_fumee:
        return "Alarme activée"
    else:
        return "Alarme désactivée"

def evaluer_alarme_et_stricte(capteur_mvt1: bool, capteur_mvt2: bool, detecteur_fumee: bool) -> str:
    # L'opérateur ET exige que toutes les conditions soient vraies simultanément
    # Utilisation de parenthèses pour forcer la priorité d'évaluation logique
    if detecteur_fumee and (not capteur_mvt1 and not capteur_mvt2):
        return "Alarme activée"
    else:
        return "Alarme désactivée"

if __name__ == "__main__":
    # Test selon le cas d'usage: Mouvement 1 (Activé), Mouvement 2 (Désactivé), Fumée (Désactivé)
    c_mvt1 = True
    c_mvt2 = False
    d_fumee = False
    
    print("Test Condition OU :", evaluer_alarme_ou(c_mvt1, c_mvt2, d_fumee))
    print("Test Condition ET :", evaluer_alarme_et_stricte(c_mvt1, c_mvt2, d_fumee))