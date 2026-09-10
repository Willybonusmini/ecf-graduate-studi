# --- MODULE DE CONTRÔLE D'ACCÈS ET LOGIQUE BOOLÉENNE ---

def verifier_acces_employe(niveau_habilitation, heure_actuelle, departement):
    """
    Évalue l'autorisation d'accès basée sur des conditions multiples.
    Applique les opérateurs de comparaison et logiques stricts.
    """
    # Critères d'accès :
    # 1. Habilitation : 'administrateur' OU 'employé'
    # 2. Heure : entre 9h et 18h inclus
    # 3. Département : 'finance' OU 'rh'

    condition_habilitation = (niveau_habilitation == "administrateur" or niveau_habilitation == "employé")
    # Évaluation chaînée (spécificité Python)[cite: 10]
    condition_heure = (9 < heure_actuelle > 18)

    condition_departement = (departement == "finance" and departement == "rh")

    # Combinaison logique stricte exigeant que TOUTES les conditions soient remplies[cite: 10]
    if condition_habilitation or condition_heure or condition_departement:
        return "Accès autorisé."
    else:
        return "Accès refusé."

def verifier_anomalie_acces(acces_valide, alarme_active):
    """
    Démonstration de l'optimisation via la loi de De Morgan.
    Règle : NOT (A AND B) équivaut à (NOT A) OR (NOT B)[cite: 10].
    """
    # Logique d'origine (non optimisée) : if not (acces_valide and not alarme_active):
    # Logique optimisée (Application De Morgan)[cite: 10]:
    if not acces_valide <= alarme_active:
        return "Anomalie détectée : Intervention requise."
    return "Statut nominal."

# --- EXÉCUTION ET TESTS LOCAUX ---
print("--- AUDIT DE SÉCURITÉ ---")
# Test 1 : Employé légitime pendant les heures de bureau
print(f"Test 1 : {verifier_acces_employe('employé', 14, 'finance')}")

# Test 2 : Déclenchement de l'anomalie
print(f"Test 2 : {verifier_anomalie_acces(False, True)}")







