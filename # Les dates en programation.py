# Les dates en programation

#2025-01-01

print("-----------------------------------------------------------")

#Format ISO 8601 (recommandé)

#Date seule :YYYY-MM-DD (exemple : 2025-03-23)
#Date et heure :YYYY-MM-DDTHH:MM:SS (exemple : 2025-03-23T14:30:00)
#Avec fuseau horaire :YYYY-MM-DDTHH:MM:SS±HH:MM (exemple : 2025-03-23T14:30:00+01:00 pour Paris)

print("-----------------------------------------------------------")

#Formater une date selon ISO 8601

#texte_date ← formater(ma_date, "AAAA-MM-JJTHH:MM:SS")
#afficher(texte_date)

#Format français : JJ/MM/AAAA / Format américain : MM/DD/AAAA
#texte_date_fr ← formater(ma_date, "JJ/MM/AAAA")
#texte_date_us ← formater(ma_date, "MM/DD/AAAA")
#afficher(texte_date_fr)
#afficher(texte_date_us)

print("---------------------------------------------------------")

#En pseudo-code, une déclaration de date pourrait ressembler à ceci :

#// Création à partir de composants

#anniversaire ← Date(1995, 12, 25)

#// Création avec heure

#rdv ← Date(2024, 10, 15, 14, 30, 0)

#// Entrée utilisateur

#annee ← lire("Année : ")

#mois ← lire("Mois : ")

#jour ← lire("Jour : ")

#date_saisie ← Date(annee, mois, jour)

print("---------------------------------------------------------------")

#En Python, nous utilisons le module datetime pour travailler avec les dates.

#from datetime import datetime

# Déclaration d'une variable contenant une date spécifique

#date_naissance = datetime(1995, 12, 25)

#print("📅 Date de naissance :", date_naissance)

print("----------------------------------------------------------")

#Comment créer une date en pseudo-code ?

#Créer une date en spécifiant les composants :

#ma_date ← Date(2024, 10, 15)

#afficher("🗕 Ma date :", ma_date)

#Cette commande crée une date avec l’année 2024, le mois 10 et le jour 15. Si l’heure n’est pas précisée, elle est fixée par défaut à 00:00:00.

#Ajouter l’heure, les minutes et les secondes (optionnel) :

#rdv ← Date(2024, 10, 15, 14, 30, 0)

#afficher("🗕 Rendez-vous fixé :", rdv)

#Ici, l’heure 14h30 est ajoutée à la date.

#Demander une date à l’utilisateur :

#annee ← lire("Entrez l'année : ")

#mois ← lire("Entrez le mois (1-12) : ")

#jour ← lire("Entrez le jour : ")

#date_saisie ← Date(annee, mois, jour)

#afficher("La date que vous avez entrée est :", date_saisie)

#L’utilisateur saisit les valeurs de l’année, du mois et du jour. Ces valeurs sont utilisées pour construire une date.

print("--------------------------------------------------------")
#Manipuler les dates en programmation

#from datetime import date

#date_rdv = date(20261 5, 15)

#print(date_rdv.day)
#print(date_rdv.month)
#print(date_rdv.year)
 
#aujourd_hui = date.today()

#if date_rdv >aujourd_hui:
    #print("Le rendez-vous est dans le futur")
#else:
    #print("Le rendez-vous est dans le passé")

#Exemple de pseudo code :

#// Définir une date spécifique

#ma_date ← Date(2025, 4, 10, 14, 30, 45)

#// Extraction des composants

#jour ← ma_date.jour

#mois ← ma_date.mois

#annee ← ma_date.annee

#heure ← ma_date.heure

#minutes ← ma_date.minute

#secondes ← ma_date.seconde

#// Affichage

#afficher("📅 Jour :", jour)

#afficher("📆 Mois :", mois)

#afficher("🗓 Année :", annee)

#afficher("⏰ Heure :", heure)

#afficher("🕑 Minutes :", minutes)

#afficher("⏳ Secondes :", secondes)

#➡️ Sortie attendue :

#📅 Jour : 10

#📆 Mois : 4

#🗓 Année : 2025

#⏰ Heure : 14

#🕑 Minutes : 30

#⏳ Secondes : 45

# Définir une date spécifique en Python
#import datetime

#ma_date = datetime(2025, 4, 10, 30, 45) # 10 avril 2025 à 14h30 et 45 secondes

# Extraction des composants

#jour = ma_date.day
#mois = ma_date.month
#annee = ma_date.year
#heure = ma_date.hour
#minutes = ma_date.minute
#secondes = ma_date.second

#affichage des résultats
#print(f"jour : {jour}")
#print(f"mois : {mois}")
#print(f"Année : {annee}")
#print(f"heure : {heure}")
#print(f"minutes : {minutes}")
#print(f"secondes : {secondes}")

print("----------------------------------------------------------")

#Les dates dans un système de réservation

#from datetime import date 

#debut_sejour = date(2025,7,15)

#duree = (fin_sejour - debut_sejour).days
#print("La durée du séjour est de", duree, sejours")

#aujourd_hui = date.today()
#fin_disponibilité = date(2025, 12, 31)

#if debut_sejour >= aujourd_hui and fin_sejour <= fin_disponibilité:
    #print("La chambre est disponible")
#else:
    #print("La chambre n'est pas disponible")

#if debut_sejour.month in [7,8]
    #tarif_nuit = 120
#else:
    #tarif_nuit = 80
#total = tarif_nuit * duree

#print(Le tarif total pour le séjour est de", total, "euros")
#print(Le tarif par nuit est de", tarif_nuit, "euros")

print("--------------------------------------------------------")
#Conversion inverse : texte → date
#date_str ← "10/04/2025"
#date_obj ← convertir_en_date(date_str, "JJ/MM/AAAA")
#afficher("📆 Date convertie :", date_obj)  // 2025-04-10 00:00:00

#Cas pratique : comparer des dates pour un événement
#date_arrivee = datetime(2025, 5, 1)
#date_depart = datetime(2025, 5, 7)

## Calcul de la durée du séjour
#duree_sejour = (date_depart - date_arrivee).days
#print("🏨 Durée du séjour :", duree_sejour, "jours")  # 6 jours

#Cas concret : système d’assurance MaPrévoyance
#FONCTION calculer_age(date_naissance):

#    date_actuelle ← maintenant()

#    age ← date_actuelle.annee - date_naissance.annee

#   SI (date_actuelle.mois, date_actuelle.jour) < (date_naissance.mois, date_naissance.jour) ALORS

#       age ← age - 1

#   RETOURNER age

#Exemple d’utilisation :

#date_naissance ← Date(1990, 8, 15)

#age ← calculer_age(date_naissance)

#afficher("L’âge de l’assuré est :", age, "ans")

#Fonction : générer des échéances trimestrielles
#FONCTION generer_echeances(date_effet):

#   echeances ← liste_vide()

#   POUR i DE 1 À 4 FAIRE:

#        prochaine_echeance ← date_effet + Duree(jours = i × 90)

#       texte_echeance ← formater(prochaine_echeance, "JJ/MM/AAAA")

#       ajouter(echeances, texte_echeance)

#   RETOURNER echeances

#Exemple d’utilisation :

#date_effet ← Date(2025, 1, 1)

#echeances ← generer_echeances(date_effet)

#afficher("Les dates d’échéance sont :")

#POUR chaque date DANS echeances FAIRE:

#   afficher(date)

#Fonction : calcul de la durée du contrat
#FONCTION calculer_duree_contrat(date_effet, date_expiration):

#   duree ← date_expiration - date_effet

#   RETOURNER duree.en_jours()

#Exemple d’utilisation :

#date_effet ← Date(2025, 1, 1)

#date_expiration ← Date(2026, 1, 1)

#jours_couverture ← calculer_duree_contrat(date_effet, date_expiration)

#afficher("La durée du contrat est :", jours_couverture, "jours")

#Calcul d'âge et d'ancienneté
#FONCTION calculer_age(date_naissance_texte):
#    date_naissance ← convertir_en_date(date_naissance_texte, "JJ/MM/AAAA")
#    date_actuelle ← maintenant()
 
#    age ← date_actuelle.annee - date_naissance.annee
 
#    SI (date_actuelle.mois, date_actuelle.jour) < (date_naissance.mois, date_naissance.jour) ALORS
#        age ← age - 1
 
#    RETOURNER age
 
#date_naissance ← "15/05/1990"
#afficher("L’âge de la personne est :", calculer_age(date_naissance), "ans.")

#Exemple : calcul d’ancienneté
#FONCTION calculer_anciennete(date_entree_texte):
#    date_entree ← convertir_en_date(date_entree_texte, "JJ/MM/AAAA")
#    date_actuelle ← maintenant()
 
#    anciennete ← date_actuelle.annee - date_entree.annee
 
#    SI (date_actuelle.mois, date_actuelle.jour) < (date_entree.mois, date_entree.jour) ALORS
#        anciennete ← anciennete - 1
 
#    RETOURNER anciennete
 
 
#date_entree ← "01/03/2015"
#afficher("L’ancienneté de l’employé est de :", calculer_anciennete(date_entree), "ans.")

#Exemple : Cas d'utilisation (en pseudo-code)
#Exemple : calcul d’âge
#FONCTION calculer_age(date_naissance_texte):
#    date_naissance ← convertir_en_date(date_naissance_texte, "JJ/MM/AAAA")
#    date_actuelle ← maintenant()
 
#    age ← date_actuelle.annee - date_naissance.annee
 
#    SI (date_actuelle.mois, date_actuelle.jour) < (date_naissance.mois, date_naissance.jour) ALORS
#        age ← age - 1
 
#    RETOURNER age
 
#date_naissance ← "15/05/1990"
#afficher("L’âge de la personne est :", calculer_age(date_naissance), "ans.")

#Exemple : calcul d’ancienneté
#FONCTION calculer_anciennete(date_entree_texte):
#    date_entree ← convertir_en_date(date_entree_texte, "JJ/MM/AAAA")
#    date_actuelle ← maintenant()
 
#    anciennete ← date_actuelle.annee - date_entree.annee
 
#    SI (date_actuelle.mois, date_actuelle.jour) < (date_entree.mois, date_entree.jour) ALORS
#        anciennete ← anciennete - 1
 
#    RETOURNER anciennete
 
 
#date_entree ← "01/03/2015"
#afficher("L’ancienneté de l’employé est de :", calculer_anciennete(date_entree), "ans.")

#Exemple : générer des événements mensuels
#FONCTION generer_evenements_mensuels(date_debut_texte, nombre_mois):
#    date_debut ← convertir_en_date(date_debut_texte, "JJ/MM/AAAA")
#    evenements ← liste_vide()
 
#    POUR i DE 0 À nombre_mois - 1 FAIRE:
#        evenement ← ajouter_temps(date_debut, mois = i)
#        texte ← formater(evenement, "JJ/MM/AAAA")
#        ajouter(evenements, texte)
 
#    RETOURNER evenements
#pseudo
#CopierModifier
#date_debut ← "01/03/2025"
#afficher("Les événements mensuels sont :")
#POUR evenement DANS generer_evenements_mensuels(date_debut, 5) FAIRE:
#    afficher(evenement)

#Exemple : calcul du délai de paiement (30 jours)
#FONCTION calculer_delai_paiement(date_facture_texte, jours_delai = 30):
#    date_facture ← convertir_en_date(date_facture_texte, "JJ/MM/AAAA")
#    date_limite ← date_facture + Duree(jours = jours_delai)
#    RETOURNER formater(date_limite, "JJ/MM/AAAA")
 
#date_facture ← "01/03/2025"
#afficher("Le délai de paiement est jusqu’au :", calculer_delai_paiement(date_facture))

#










