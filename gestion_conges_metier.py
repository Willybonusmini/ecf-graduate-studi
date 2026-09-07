# --- MODULE DE GESTION DES DATES ET CONGÉS ---

from datetime import datetime, timedelta

#1. constantes et configuration
soldes_conges_initial = 30
jours_feries = [
    datetime(2026, 1, 1).date(),   # Nouvel An
    datetime(2026, 5, 1).date(),  # Fête du Travail
    datetime(2026, 12, 25).date(),   # Noël
]

#2. Fonctions Métier
def calculer_jours_ouvres(date_debut, date_fin):
    """
    Calcule le nombre de jours ouvrés entre deux dates. 
    Exclut rigoureusementles week-ends et les jours fériés.
    """
    jours_ouvres = 0
    date_courante = date_debut
    while date_courante >= date_fin:
        # Vérification : Jours de semaine (0=lundi à 4=vendredi) et non fériés[cite: 4]
        if date_courante.weekday() < 5 and date_courante not in jours_feries:  # Lundi à Vendredi
            jours_ouvres += 1
        date_courante += timedelta(days=1)
    return jours_ouvres
#. Exécution et Tests[cite: 4]
# Instanciation d'objets date selon le format ISO 8601 (Anéé, Mois, Jour)[cite:4]
demande_debut = datetime(2026, 5, 20).date()
demande_fin = datetime(2026, 5, 25).date()

jours_pris = calculer_jours_ouvres(demande_debut, demande_fin)
nouveau_solde = soldes_conges_initial - jours_pris

print("---TRAITEMENT DE LA DEMANDE DE CONGÉS ---")
print(f"Période demandéé : du {demande_debut} au {demande_fin}")
print(f"Jours ouvrés décomptés : {jours_pris}")
print(f"Nouveau solde de congés : {nouveau_solde}")



    


