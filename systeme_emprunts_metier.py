# --- MOTEUR DE TRANSACTION : EMPRUNTS ET RETOURS ---

from datetime import datetime, timedelta

def emprunter_livre(catalogue, usager, isbn, date_emprunt):
    """
    Gère la transaction d'emprunt.
    Vérifie la disponibilité et met à jour les registres.
    """
    for livre in catalogue:
        if livre["isbn"] == isbn:
            if livre["disponible"]:
                #1. Mise à jour du statut du livre
                livre["disponible"] = False

                # 2. Initialisation du registre d'emprunts si inexistant[cite:6]
                if "emprunts" not in usager:
                    usager["emprunts"] = []

                #3. Ajout de la transaction dans le dossier de l'usager[cite: 6]
                nouvel_emprunt = {"isbn": isbn, "date_emprunt": date_emprunt}
                usager["emprunts"].append(nouvel_emprunt)

                return True, "Livre emprunté avec succès."
            else:
                return False, "Livre actuellement indisponible."
    return False, "Livre introuvable dans le catalogue."

def verifier_retards(usager, date_actuelle):
    """
    Scane le registre de l'usager pour détecter les emprunts dépassant
    le délai légal autorisé de 14 jours[cite: 6].
    """
    retards = []
    for emprunt in usager.get("emprunts", []):
        date_emprunt = emprunt["date_emprunt"]

        #Calcul du délai écoulé en jours[cite: 6]
        delai = (date_actuelle - date_emprunt).days
        #Identification de l'infraction (Délai supérieur à 14 jours)
        if delai > 14:
            retards.append(emprunt)
    return retards

# --- EXÉCUTION ET TESTS LOCAUX ---
# Base de données (Mock)
catalogue_db = [{"titre": "1984", "isbn": "1234", "disponible": True}]
usager_db = {"nom": "wilson", "identifiant": "W01"}

# Simulation temporel 
date_hier = datetime.now() - timedelta(days=20)
date_aujourd_hui = datetime.now()

print("--- EXÉCUTION DE LA TRANSACTION ---")
status, message = emprunter_livre(catalogue_db, usager_db, "1234", date_hier)
print(f"Transaction : {message}")

print("\n--- AUDIT DES RETARDS ---")
infractions = verifier_retards(usager_db, date_aujourd_hui)
if infractions:
    print(f"ALERTE : {len(infractions)} emprunts(s) en retard détecté(s).")
else:
    print("Dossier usager en règle.")






