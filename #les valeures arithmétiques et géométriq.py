#les valeures arithmétiques et géométriques

#n = 7

#if n % 2 == 0:
 # print("N est pair")
#else:
  #print("N est impair")

  # Division flottante
#result1 = 5 / 2  # 2.5 (float)
 
# Division entière
#result2 = 5 // 2  # 2 (int)
#print(result1)
#print(result2)

#result3 = 5.0 / 2  # 2.5 (float)
#print(result3)

from http import client
from operator import le


print("-------------------------------------------------------------")

#a = False

#if not a:
    #print("a est faux")

print("-------------------------------------------------------------")

#la logique booléenne

#si est_majeur ET a_permis ALORS
 #   Afficher "peut conduire." #afficher est la condition

#Si est_enseignant OU est_étudiant ALORS
 #   Afficher "peut entrer dans l'école."

print("-------------------------------------------------------------")
#Critère 1 : le client doit avoir dépensé plus de 500 €.

#Critère 2 : le client doit avoir effectué au moins 10 achats. 

#Critère 3 : le client doit être inscrit depuis plus de 6 mois.

depenses = 600
achats = 12
anciennete = 7 # en mois

#if depenses > 500 and achats > 10 and anciennete > 6:
    #print("Le client est éligible au programme de fidélité.")
#else:
    #print("Le client n'est pas éligible au programme de fidélité.")    

print("-------------------------------------------------------------")
# Résoudre des problèmes avec la logique booléenne

#est_premium = True
#montant_commande = 120
#habite_etranger = False

#commande_suffisante = montant_commande > 100

#a_droit_livraison = est_premium or (commande_suffisante and not habite_etranger)

#if a_droit_livraison:
 #   print("Vous avez droit à la livraison gratuite.")
#else:
 #   print("Le client n'a pas droit à la livraison gratuite.")

print("-------------------------------------------------------------")

# Critère 1 : le niveau d'habilitation de l'utilisateur (ex : administrateur, employé, visiteur).

# Critère 2 : la plage horaire (accès autorisé entre 9 h et 18 h).

# Critère 3 : le département de l'utilisateur (accès limité à certains départements seulement).

#niveau_habilitation = "administrateur"
#heure_actuelle = 14  # Heure actuelle 14:00
#departement_utilisateur = "finance" 

#vérifier les conditions 
#if (niveau_habilitation == "administrateur" or niveau_habilitation == "employé") and \
   # (9 <= heure_actuelle <= 18) and \
  #      (departement_utilisateur == "finance" or departement_utilisateur == "rh"):
 #           print("Accès autorisé.")
#else:
  #  print("Accès refusé.")

print("--------------------------------------------------------------------")   

#print("Bonjour")
#print("Bienvenue dans ce programme")
#print("Fin de l'exécution")

print("--------------------------------------------------------")

#le flux d'exécution en programation 

#prix = 10 
#quantité = 5
#total = prix * quantité

#if total > 50:
 #   print("Le total est supérieur à 50.")
#else:
 #   print("Le total est inférieur ou égal à 50.")    

#compteur = 0
#while compteur < 5:
    #print("compteur:", compteur)
   # compteur += 1

print("---------------------------------------------------------")

utilisateur = input("Entrez votre nom : ")
if utilisateur == "Admin":
    print("Accès autorisé")
else:
    print("Accès refusé")

