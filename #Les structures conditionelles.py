#Les structures conditionelles

#Si condition Alors
 #   Exécuter bloc d'instructions
#Sinon
 #   Exécuter un autre bloc d'instructions
#Fin Si

print("-------------------------------------------------")

#age = 20

#if age >= 18:
 #   print("vous êtes majeur.")
#else:
#    print("vous êtes mineur.")

print("----------------------------------------------------")

#Il est possible d’utiliser une condition Si sans Sinon

#si la température dépasse 25 °C, un message est affiché. Si ce n'est pas le cas, le programme ne fait rien.

#temperature = 30

#if temperature > 25:
#    print("Il fait chaud aujourd'hui !")

print("-------------------------------------------------")

#age = 28
#montant_achat = 120

#if age > 25 and montant_achat > 100:
 #   print("Vous avez droit à une réduction de 10%")
#else:
   # print("Pas de réduction disponible")

print("-------------------------------------------")

#Si condition Alors
#    Exécuter bloc d'instructions
#Sinon
#    Exécuter un autre bloc d'instructions
#Fin Si

print("------------------------------------")

#age = 20 

#if age >= 18:
#    print("Vous êtes majeur.")
#else:
#    print("Vous êtes mineur.")

print("-------------------------------------")

#cas particulier: si sans sinon

#temperature = 30 

#if temperature > 25:
#    print("Il fait chaud aujourd'hui !")

#si la température dépasse 25 °C, un message est affiché. Si ce n'est pas le cas, le programme ne fait rien.

print("-----------------------------------------------")

#Implementation de condition

#age = 22
#montant_achat = 120

#if age > 25 and montant_achat > 100:
#    print("Vous avez droit à une réduction de 10%")
#else:
#    print("Pas de réduction disponible")


print("-----------------------------------------")

#Si condition1 Alors
#    Si condition2 Alors
#        Exécuter bloc A
#    Sinon
#        Exécuter bloc B
#    Fin Si
#Sinon
#    Exécuter bloc C

#statut = "premium"
#montant_achat = 150
#article_bonus = 150
#article_gemini = 55
#
#if statut == "Premium":
#    if montant_achat > 100:
#        article_bonus = 150
#        print("Remise de 20% appliquée")
#    else:
#        print("Remise de 10% appliquée")
#else:
#   if montant_achat < 80:
#    article_gemini = 80
#    print("Remise de 5% appliquée")
#   else:
#       print("Pas de remise")


print("---------------------------------------------------")

#Selon variable Faire
#    Cas valeur1 :
#        Exécuter bloc A
#    Cas valeur2 :
#        Exécuter bloc B
#    Cas valeur3 :
#        Exécuter bloc C
#    Sinon :
#        Exécuter bloc par défaut
#Fin Selon

#categorie_client = "Gold"

#match categorie_client:
#    case "Bronze":
#        print("Réduction de 5%")
#    case "silver":
#        print("Réduction de 10%")
#    case "Gold":
#        print("Réduction de 15%")
#    case _:
#        print("Pas de réduction")    

print("---------------------------------------------------")

#cas d'usage en entreprise

#import re

#email = input("Entrez votre email : ")
#mot_de_passe = input("Entrez votre mot de passe : ")

# Vérification de l'email
#if "@" in email and "." in email.split("@")[-1]:
#    email_valide = True
#else:
#    email_valide = False

# Vérification du mot de passe
#mot_de_passe_valide = bool(re.search(r"^(?=.*[A-Z])(?=.*\d).{8,}$", mot_de_passe))

#if email_valide and mot_de_passe_valide:
#    print("Inscription réussie !")
#else:
#    print("Erreur : Veuillez saisir un email et un mot de passe valides.")

print("-----------------------------------------")

#quantité_stock = 5
#quantité_demandee = int(input("combien d'articles souhaitez-vous commander ? "))

#if quantité_demandee <= quantité_stock:
#    print("commande validée.")
#else:
#    print("Stock insuffisant !")    

print("----------------------------------------------")

#stock = 8

#if stock > 10:
#    print("stock critique")
#elif stock < 20:
#    print("stock moyen")
#elif stock < 25:
#    print("stock moyen")    
#else:
#    print("stock suffisant")

print("----------------------------------------------")

#role_utilisateur = input("Entrez votre rôle (admin / employé) : ").lower()

#if role_utilisateur == "admin":
#    print("Affichage du tableau de bord administrateur avec accès complet.")
#elif role_utilisateur == "employé":
#    print("Affichage du tableau de bord employé avec accès restreint.")
#else:
#    print("Accès refusé.")        

print("----------------------------------------------------")

#salaire = float(input("Entrez votre salaire mensuel : "))
#score_credit = int(input("Entrez votre score de crédit (0-100) : "))
#historique_dettes = input("Avez-vous des dettes impayées ? (oui/non) ").lower()

#if salaire >= 3000 and score_credit >= 70 and historique_dettes == "non":
#    print("crédit approuvé !")
#elif score_credit < 50 or historique_dettes == "oui":
#    print("crédit refusé.")
#else:
#    print("crédit en attente de validation manuelle.")        

print("---------------------------------------------------------------------")

#Si dernier_achat == "ordinateur" Alors
#    Suggérer "souris", "clavier", "sac pour ordinateur"
#Sinon Si dernier_achat == "téléphone" Alors
#    Suggérer "écouteurs", "chargeur", "coque de protection"
#Sinon
#    Suggérer "Produits populaires"
#Fin Si

print("-------------------------------------------------------")

#âge = 18
#citoyen = 17

#Avant (condition répétée) :
#if âge >= 18 and citoyen == True:
#    print("Vous pouvez voter.")
#elif âge >= 18 and citoyen == False:
 #   print("Vous êtes majeur, mais vous ne pouvez pas voter.")

#Après (condition factorisée) :
#if âge >= 18:
#   if citoyen:
#    print("Vous pouvez voter.")
#else:
#    print("Vous êtes majeur, mais vous ne pouvez pas voter.")

print("------------------------------------------------------------")

#score = 50
#temps_reponse = 45

#Avant (longue condition peu lisible) :
#if (score > 80 and temps_reponse < 30) or (score > 90 and temps_reponse < 60):
#    print("Vous obtenez un bonus.")

#Après (avec variables intermédiaires) :
#bonus_rapide = score > 80 and temps_reponse < 30
#bonus_exceptionnel = score > 90 and temps_reponse < 60

#if bonus_rapide or bonus_exceptionnel:
#    print("Vous obtenez un bonus.")

print("------------------------------------------------------------------")

#Avant (condition trop détaillée) :
#if actif == True:
#    print("Compte actif.")
#else:
#    print("Compte inactif.")

#Après (condition simplifiée) :
#print("Compte actif." if actif else "Compte inactif.")

print("-------------------------------------------------------------------")

#Le concept de répétition en programmation
#ignoreEn programmation, il est fréquent de devoir répéter une même opération un certain nombre de fois. Plutôt que d'écrire plusieurs fois la même ligne de code, on utilise des boucles qui exécutent un bloc d’instructions : # type: ignore # type: ignore

# ignoreUn nombre défini de fois : par exemple, parcourir une liste d'éléments ou afficher un message plusieurs fois.# type:Un nombre défini de fois : par exemple, parcourir une liste d'éléments ou afficher un message plusieurs fois.# type:
# ignoreJusqu'à ce qu'une condition soit remplie : par exemple, demander à un utilisateur de saisir une valeur correcte.# type: ignore

#Exemple simple : affichage de 5 nombres

#for i in range(1, 6):

#    print(i)
# type: ignoreExemple d’une boucle qui s’exécute jusqu’à ce qu’une condition soit remplie# type: ignore

print("--------------------------------------------------------------")

#mot_de_passe = ""
#while mot_de_passe != "secret":
#    mot_de_passe = input("Entrez le mot de passe : ")
#print("Accès autorisé.")

print("---------------------------------------------------------")

#les différences types de boucles
#boucle for
#pour i de 0 à 4 faire
#    Afficher "boite" + i 
#fin faiire 

#boucle python

#for i in range(5):
#    print("boite", i)

#boucle niveau de remplissage

#niveau = 0

#while niveau < 100:
#    print("remplissage... niveau actuel:", niveau)
#    niveau += 10
#print("niveau maximum atteint !", niveau)

print("------------------------------------------------------")

#commandes = ["commande 1", "commande 2", "commande 3", "commande 4", "commande 5"]

#for commande in commandes:
#    print(f"Traitement de {commande}")

print("---------------------------------------")

#for i in range(1, 11):
#    print(i)

print("---------------------------------------------")

#numero = 0
#while numero < 1 or numero > 5:
#    numero = int(input("Entrez un numéro entre 1 et 5 : "))
#print("numéro valide :", numero)

print("---------------------------------------------------------")

#Boucle infinie

#Problème : sans une condition d’arrêt, cette boucle ne s’arrêtera jamais.

#Il faut toujours s’assurer qu’une boucle while a une condition de sortie pour éviter un blocage du programme.

#while true:
#    print("ceci est une boucle infinie.")

print("-------------------------------------------------------")

#ventes = [
#    [1500, 2000, 2500],  # Région 1 (Janvier, Février, Mars)
#    [1800, 2200, 2700],  # Région 2
#    [1600, 2100, 2600]   # Région 3
#]

#for region in range(len(ventes)):
#    print(f"Ventes pour la région {region + 1} :")
#    for mois in range(len(ventes[region])):
#        print(f"  - Mois {mois + 1} : {ventes[region][mois]}€")

print("-----------------------------------------------------")

#resoudre des problemes avec boucles 

#somme = 0
#bn_mag = 5

#for i in range(1, nb_mag + 1): I
#note = float(input(f"note du magasin {i} (entre 1 et 5 ):"))
#somme += note

print("------------------------------------------------------------------------")

#nombres = [10, 20, -5, 30, 40]

#for nombre in nombres:
#    if nombre < 0:
#        print("nombre négatif détecté, arrêt du traitement.")
#        break
#    print(nombre)

print("------------------------------------------------------------")

#Ignorer les nombres pairs (continue)

#for i in range(10):
#    if i % 2 == 0:
#        continue # ignore les nombres pairs
#    print(i)

print("------------------------------------------------------")

#i = 1
#while i < 10:
#    print(i)

print("---------------------------------------------------------")

#i = 1
#while i < 10:
#    print(i)
#    i += 1

print("----------------------------------------------------------------")

#i = 10
#while i > 0:
#    print(i)
#boucle infinie
#for i in range(1, 6, 2):
#    print(i)

print("--------------------------------------------------------------------")

#x = 3
#while x > 0:
#    print(x)
#    x -= 1
#else:
#    print("Boucle terminée")

print("--------------------------------------------------------------")

#for i in range(4):
#    if i == 2:
#        continue
#    print(i)

print("----------------------------------------------------------------------------")

#x = 0
#while x < 5:
#    print(x)
#    x += 1
#else:
#    print("Terminé")
print("--------------------------------------------------------------------------")

#i = 10
#while i > 0:
#    print(i)
#    i -= 1
#print("Terminée")

#ventes = [
#    [1500, 2000, 2500],  # Région 1 (Janvier, Février, Mars)
#    [1800, 2200, 2700],  # Région 2
#    [1600, 2100, 2600]   # Région 3
#]

#for region in range(len(ventes)):
#    print(f"Ventes pour la région {region + 1} :")
#    for mois in range(len(ventes[region])):
#            print(f"  - Mois {mois + 1} : {ventes[region][mois]}€")
print("-------------------------------------------------------------")

