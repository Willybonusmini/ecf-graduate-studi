#Qu'est-ce qu'une fonction en programmation ?

#Fonction pour additionner deux nombres
#Def additionner(a, b): #def : c’est le mot-clé utilisé pour définir une fonction en Python. additionner : c'est le nom de la fonction.
    #return a + b #return : cette instruction renvoie le résultat du calcul effectué par la fonction (dans ce cas, la somme de a et b).

print("---------------------------------------------")

#FONCTION additionner(a, b)
#    RETOURNER (= renvoyer, donner le résultat) a + b
#FIN FONCTION
 
#// Utilisation de la fonction
#resultat1 ← additionner(3, 5)
#resultat2 ← additionner(10, 20)
#resultat3 ← additionner(1.5, 2.5)
 
#AFFICHER resultat1  // Affichera 8
#AFFICHER resultat2  // Affichera 30
#AFFICHER resultat3  // Affichera 4.0

print("-----------------------------------------------------------")

#def additionner(a, b):
    #return a + b
#appel de la fonction avec des arguments
#resultat = additionner(5, 3)
#print(resultat) Affichera : 8 

#resultat2 = additionner(10, 20)
#print(resultat2) affichera : 30

#Les fonctions en programmation

#def dire_bonjour():
    #print("bonjour !")

#dire_bonjour()

#def dire_bonjour_prenom(prenom):
    #print("bonjour " + prenom + " !")

#dire_bonjour_prenom("jean")

#def afficher_bienvenue():
    #print("bienvenue !")

#def accueil_utilisateur(prenom):
    #afficher_bienvenue()
    #dire_bonjour_prenom(prenom)

#accueil_utilisateur("Marie")
#accueil_utilisateur("Bruno")

#Réduction de la duplication de code
#Calcul de la somme à plusieurs endroits
#x1 = 5 + 3
#x2 = 10 + 4
x3 = 7 + 9
#print(x1, x2, x3)

#print("---------------------------------------")
#def additionner(a, b):
    #return a + b
#appels à la fonction
#x1 = additionner(5, 3)
#x2 = additionner(10, 4)
#x3 = additionner(7, 9)
#print(x1, x2, x3)

#print("---------------------------------------------------")
#Amélioration de la lisibilité sans fonction

#birth_year = 1990
#birth_month = 5
#birth_day = 17

#current_year = 2025
#current_month = 3 
#current_day = 26

#age = current_year - birth_year
#if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    #age -= 1
#print(age)

#print("--------------------------------------")
#Amélioration de la lisibilité avec fonction
#FONCTION calculer_age(jour_naissance, mois_naissance, annee_naissance)
#    // Obtenir la date actuelle (supposons qu'elle est disponible)
#    jour_actuel ← JOUR_ACTUEL
#    mois_actuel ← MOIS_ACTUEL
#    annee_actuelle ← ANNEE_ACTUELLE
   
#    // Calculer l'âge de base
#    age ← annee_actuelle - annee_naissance
#   
#    // Vérifier si l'anniversaire est déjà passé cette année
#    SI (mois_actuel < mois_naissance) OU
#       (mois_actuel = mois_naissance ET jour_actuel < jour_naissance) ALORS
#        age ← age - 1
#    FIN SI
   
#    RETOURNER age
#FIN FONCTION
 
#// Utilisation de la fonction
#age ← calculer_age(15, 5, 1990)
#AFFICHER « L'utilisateur a » , age, « ans. »

#def calculer_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    #age = current_year - birth_year
    #if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        #age -= 1
    #return age

# Appel à la fonction
#age = calculer_age(1990, 5, 17, 2025, 3, 26)
#print(age)

#print("----------------------------------------------------")
#Exemple de test unitaire
#def calculer_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    #age = current_year - birth_year
    #if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        #age -= 1
    #return age

# Appel à la fonction
#age = calculer_age(1990, 5, 17, 2025, 3, 26)
#print(age)

# Test de la fonction calculer_age
# assert calculer_age(1990, 5, 17, 2025, 3, 26) == 34
# assert calculer_age(2000, 1, 1, 2025, 3, 26) == 25

#print("-----------------------------------------------------")
#Exemple de modification dans une fonction
#def calculer_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    #if birth_year <= 0:
        #raise ValueError("L'année de naissance doit être positive.")
    #age = current_year - birth_year
    #if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        #age -= 1
    #return age

# ptint("----------------------------------------------")
# Fonctions prédéfinies (bibliothèques standard)
# Utilisation de la fonction prédéfinie len()
# ma_chaine = "Bonjour"
# print(len(ma_chaine)) # Affiche 7

#Fonctions personnalisées
# def calculer_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    #age = current_year - birth_year
    #if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        #age -= 1
    #return age

#Procédures (sans retour de valeur)
#def afficher_message(message):
    #print(message)

# Appel de la procédure
# afficher_message("Bonjour tout le monde!")

#Méthodes (liées à des objets)
# Class personne:
    #def_init_(self, nom, age):
        #self.nom = nom
        #self.age = age

    #def afficher_details(self):
        #print(f"nom : {self.nom}, Âge : {self.age}")

# création d'un objet de la classe personne
#personne1 = personne("Alice", 30)
#personne1.afficher_details() # Appel de la méthode

#print("---------------------------------------------------")
#Exemple d’utilisation des fonctions prédéfinies
## Liste des produits vendus avec prix
#ventes = [
#    {'produit': 'Ordinateur', 'prix': 1200},
#    {'produit': 'Smartphone', 'prix': 800},
#    {'produit': 'Tablette', 'prix': 600},
#]

# Calcul du total des ventes
#total_ventes = sum([article['prix'] for article in ventes])

# Nombre d'articles vendus
#nombre_articles = len(ventes)

# Prix moyen
#prix_moyen = total_ventes / nombre_articles

#print(f"Total des ventes : {total_ventes} €")
#print(f"Nombre d'articles vendus : {nombre_articles}")
#print(f"Prix moyen par produit : {prix_moyen:.2f} €")

#print("----------------------------------------------------------")
#utiliser des fonctions prédéfinies
#ventes = [100.5, 230.0, 89.99, 145.0, 210.25]

#total = sum(ventes)

#print("Le total des ventes est de : ", total)

#moyenne = sum(ventes) / len(ventes)
#plus_grande_vente = max(ventes)
#print("La plus grand vente est de : ", plus_grande_vente)
#plus_petit_vente = min(ventes)
#print("La plus petite vente est de : " plus_petite_vente)

#total = round(total, 2)
#print("Le total des vendes arrondi est de : ", total)

#print("-----------------------------------------------------")
#Mathématiques
#math.sqrt(x) : calcule la racine carrée de x.
#	math.pow(x, y) : calcule x à la puissance y.

#import math

#x = 16
#print(math.sqrt(x))  # Affiche 4.0
#print(math.pow(x, 2))  # Affich 256.0

#print("------------------------------------------------------")
#Chaînes de caractères (strings)
#texte = "Bonjour tout le monde"
#print(texte.upper())  # Affiche "BONJOUR TOUT LE MONDE"
#print(texte.split())  # Affiche ['Bonjour', 'tout', 'le', 'monde']

#print("----------------------------------------------------------------")
#Dates et heures
#import datetime
 
# Date et heure actuelles
#maintenant = datetime.datetime.now()
#print(maintenant)
 
# Calculer la différence entre deux dates
#date1 = datetime.datetime(2025, 3, 26)
#date2 = datetime.datetime(2025, 4, 1)
#difference = date2 - date1
#print(difference.days)  # Affiche 6 (nombre de jours entre les deux dates)

#print("----------------------------------------------------")
# Tableaux et collections
#python
#CopierModifier
#fruits = ["pomme", "banane", "orange"]
#fruits.append("kiwi")
#fruits.sort()
#print(fruits)  # Affiche ['banane', 'kiwi', 'orange', 'pomme']

#print("----------------------------------------------------------")
# Entrées et sorties
# # Lire une entrée utilisateur
#nom = input("Entrez votre nom : ")
#print(f"Bonjour, {nom} !")

#print("-------------------------------------------------------------------")
#Signaler les erreurs
#def diviser(a, b):
#    if b == 0:
#        return None  # Code d'erreur si la division par zéro est tentée
#    return a / b

#resultat = diviser(10, 0)
#if resultat is None:
#    print("Erreur : division par zéro")

#print("--------------------------------------------------------------")
#lancer des exceptions.
#FONCTION diviser(a, b)
#    // Vérifier si la division est possible
#    SI b = 0 ALORS
#        RETOURNER "ERREUR: Division par zéro impossible"
#    SINON
#        RETOURNER a / b
#    FIN SI
#FIN FONCTION
 
#// Utilisation de la fonction
#resultat ← diviser(10, 0)
#SI resultat COMMENCE_PAR "ERREUR:" ALORS
#    AFFICHER resultat
#SINON
#    AFFICHER "Résultat de la division :", resultat
#FIN SI

#print("--------------------------------------------------------------")
#En Python, vous pouvez utiliser try et except
#def diviser(a, b):
#    if b == 0:
#        raise ValueError("Division par zéro impossible")  # Lève une exception
#    return a / b

#try:
#    resultat = diviser(10, 0)
#except ValueError as e:
#    print(f"Erreur : {e}")

#print("--------------------------------------------------------------")
#Gestion des erreurs dans des fonctions prédéfinies
#try:
#    with open("fichier_inexistant.txt", "r") as f:
#        contenu = f.read()
#except FileNotFoundError:
#    print("Le fichier spécifié n'a pas été trouvé.")

#print("--------------------------------------------------------")
#Exemple de pseudo-code avec paramètre :
#fonction saluer(nom)
#    afficher "Bonjour, " + nom

# Exemple en Python avec un paramètre :
#def saluer(nom):
#    print(f"Bonjour, {nom} !")

# Exemple en Python avec plusieurs paramètres :
#def additionner(a, b):
#    return a + b
#👉 Ici, a et b sont des paramètres.

#Appel de la fonction avec des arguments :
#resultat = additionner(5, 3)
#print(resultat)  # Affichera 8

#print("----------------------------------------------------------------")
#Corps de la fonction (instructions exécutées)
#de pseudo-code 
#surface ← longueur × largeur
#    retourner surface

#Exemple en Python :
#def calculer_surface(longueur, largeur):
#    surface = longueur * largeur
#    return surface

#Appel de la fonction en Python :
#resultat = calculer_surface(5, 3)
#print(resultat)  # Affichera 15
#👉 Ici, calculer_surface prend deux paramètres, effectue un calcul, puis retourne le résultat.

#Valeur de retour (return)
# Exemple en pseudo-code sans retour :
#fonction afficherMessage()
#    afficher "Bienvenue !"

# Exemple en Python sans retour :
#def afficher_message():
#    print("Bienvenue !")

#Exemple en pseudo-code avec retour :
#fonction multiplier(x, y)
#    retourner x × y

#Exemple en Python avec retour :
#def multiplier(x, y):
#    return x * y

#Appel et récupération du retour :
#resultat = multiplier(4, 5)
#print(resultat)  # Affichera 20
#👉 Ici, return x * y renvoie le résultat au programme principal.

#Résumé : structure d’une fonction en Python
#def nom_de_fonction(param1, param2):
    # Instructions exécutées par la fonction
#    resultat = param1 + param2  
#    return resultat  # Retourne un résultat

#Principes de base pour bien nommer une fonction
#Exemple ❌ Mauvais nom vs ✅ Bon nom :
# Mauvais : trop vague
#def traite():
#    pass  

# Bon : explicite
#def traiter_commande():
#    pass  
#✅ Ici, traiter_commande est bien plus compréhensible que traite, qui ne dit pas ce qu'il traite.

#Utiliser des verbes d’action
#def envoyer_email(adresse, sujet, message):
#    """
#    Envoie un e-mail à l'adresse spécifiée.
    
#    :param adresse : adresse email du destinataire
#    :param sujet : sujet de l'email
#    :param message : contenu du message
#    """
#    print(f"Envoi d'un email à {adresse} avec pour sujet : {sujet}")
#👉 Grâce au nom envoyer_email, on comprend immédiatement l’objectif de la fonction.

#Éviter les noms ambigus et génériques
# Exemples à éviter :
#def traiter(): # Traiter quoi ? Trop flou

#def faire_calcul(): # Quel type de calcul ?

# Exemples améliorés :
#def traiter_paiement(): # On comprend mieux !

#def calculer_reduction(prix, pourcentage):  # Précise bien le type de calcul effectué

#Structure d’une bonne documentation de fonction
#Format recommandé en pseudo-code :
#/*
# * NOM_DE_FONCTION
# * --------------
# * Description: Brève description du rôle de la fonction.
# *
# * Paramètres:
# *   - param1 (type): Description du premier paramètre.
# *   - param2 (type): Description du deuxième paramètre.
# *
# * Résultat:
# *   (type) Description de la valeur renvoyée.
# *
# * Erreurs possibles:
# *   - Description des erreurs qui peuvent survenir
# *   - Comportements spéciaux dans certains cas
# */
#FONCTION NOM_DE_FONCTION(param1, param2)
#    // Corps de la fonction
#    ...
#    RENVOYER resultat
#FIN FONCTION

#Format python :
#def nom_de_fonction(param1, param2):
#    """
#    Brève description du rôle de la fonction.
 
#    Args:
#        param1 (type): description du premier paramètre.
#        param2 (type) : description du deuxième paramètre.
 
#    Returns:
#        type : description de la valeur retournée.
 
#    Raises:
#        TypeError: si le paramètre n’est pas du bon type.
#        ValueError: si la valeur fournie est hors des limites acceptables.
#    """
#    pass

#Documentation d’une fonction de calcul d’intérêts
#Sans documentation (à éviter)
#FONCTION calcul_interets(c, t, d)
#    RENVOYER c * (t / 100) * d
#FIN FONCTION

#Avec documentation claire (recommandé)
#/*
# * CALCUL_INTERETS
# * --------------
# * Description : calcule les intérêts simples sur un capital donné.
# *
# * Paramètres :
# *   - capital (nombre décimal) : montant initial investi ou emprunté.
# *   - taux_annuel (nombre décimal) : taux d'intérêt annuel en pourcentage (ex : 5 pour 5%).
# *   - duree (nombre entier) : durée en années.
# *
# * Résultat :
# *   (nombre décimal) Montant total des intérêts générés.
# *
# * Erreurs possibles :
# *   - Si le capital est négatif : impossible d'avoir un capital négatif
# *   - Si la durée est inférieure à 1 : la durée doit être d'au moins un an
# */
#FONCTION calcul_interets(capital, taux_annuel, duree)
#    // Vérification des paramètres
#    SI capital < 0 ALORS
#        AFFICHER "Erreur : le capital ne peut pas être négatif."
#        RENVOYER 0
#    FIN SI
   
#    SI duree < 1 ALORS
#        AFFICHER "Erreur : la durée doit être d'au moins un an."
#        RENVOYER 0
#    FIN SI
   
#    // Calcul et renvoi des intérêts
#    RENVOYER capital * (taux_annuel / 100) * duree
#FIN FONCTION

#Exemple d'utilisation avec la documentation
#// Utilisation de la fonction
#interets ← calcul_interets(1000, 5, 3)
#AFFICHER "Les intérêts générés sont de:", interets, "€"

# Sans documentation :
# def calcul_interets(c, t, d):
#    return c * (t / 100) * d

#Avec documentation claire :
#def calcul_interets(capital: float, taux_annuel: float, duree: int) -> float:
#    """
#    Calcule les intérêts simples sur un capital donné.

#    Args:
#        capital (float) : montant initial investi ou emprunté.
#        taux_annuel (float) : taux d’intérêt annuel en pourcentage (ex: 5 pour 5%).
#        duree (int) : durée en années.

#    Returns:
#        float: montant total des intérêts générés.

#    Raises:
#        ValueError: si le capital est négatif ou si la durée est inférieure à 1.
#    """
#    if capital < 0:
#        raise ValueError("Le capital ne peut pas être négatif.")
#    if duree < 1:
#        raise ValueError("La durée doit être d'au moins un an.")

#    return capital * (taux_annuel / 100) * duree

#Exemple d'une documentation de fonction
#Documentation inutile (à éviter)
#/*
# * AJOUTER
# * -------
# * Fonction qui ajoute a et b.
# */
#FONCTION ajouter(a, b)
#    RENVOYER a + b
#FIN FONCTION

#Documentation améliorée (recommandée)
#/*
# * AJOUTER
# * -------
# * Description : retourne la somme de deux nombres.
# *
# * Paramètres :
# *   - a (nombre décimal) : premier nombre à additionner.
# *   - b (nombre décimal) : deuxième nombre à additionner.
# *
# * Résultat :
# *   (nombre décimal) Résultat de l'addition des deux nombres.
# *
# * Exemple d’utilisation :
# *   resultat ← ajouter(5.2, 3.8)  // renvoie 9.0
# */
#FONCTION ajouter(a, b)
#    RENVOYER a + b
#FIN FONCTION

#print("----------------------------------------")
#conception de fonctions efficaces
#def traiter_commande(nom, produits):
    #print("bonjour ", nom)
    #total = sum(produits)
    #if total > 100:
    #return total

#print("---------------------------------------------------")
#def calculer_total(produits):
    #return sum(produits)

#def afficher_message_bienvenue(nom):
#    print("Bienvenue ", nom)

#def verifier_reduction(total):
    #if total > 100:
    #print("Vous avez droit à une réduction de 10% !")

#def generer_recu(client, produits):
    #total = calculer_total(produits)
    #afficher_message_bienvenue(client)
    #vérifier_réduction(total)
    #print("total à payer : ", total)

#print("-----------------------------------------")
#Définir les paramètres d'une fonction
#Exemple simple en Python :
#def bonjour(nom):
#    print(f"Bonjour, {nom} !")
#👉 Ici, nom est un paramètre qui sera remplacé par une valeur lors de l’appel de la fonction.

#print("--------------------------------------------------------")
#Appel de la fonction avec un argument (= utilisation de la fonction en lui donnant une information précise à traiter) :
#bonjour("Alice")  # Affiche : Bonjour, Alice !
#bonjour("Paul")   # Affiche : Bonjour, Paul !

#print("-----------------------------------------------")
#Paramètres optionnels (avec valeur par défaut)
#Appels valides :
#saluer("Marie")  # Affiche : Bonjour, Marie !
#saluer()         # Affiche : Bonjour, visiteur !
#👉 Ici, si aucun argument n'est fourni, nom prend la valeur "visiteur".

#print("----------------------------------------------------")
#Comment fonctionne return ?
#def doubler(n):
#    return n * 2

#resultat = doubler(5)  # Appel de la fonction
#print(resultat)  # Affichera 10

#print("------------------------------------------")
#def infos_utilisateur(nom, age):
#    return nom, age

#nom, age = infos_utilisateur("Alice", 30)
#print(f"Nom : {nom}, Âge : {age}")
#💡 Ici, la fonction retourne deux valeurs sous forme de tuple (nom, age).

#print("-------------------------------------------------------------")
#Exemple : vérifier une division par zéro
#def division(a, b):
#    if b == 0:
#        return "Erreur : division par zéro"
#    return a / b

#print(division(10, 2))  # 5.0
#print(division(5, 0))   # "Erreur : division par zéro"
#💡 Plutôt que de provoquer une erreur fatale, la fonction retourne un message clair.

#print("------------------------------------------------------------------")
#def dire_bonjour(nom):
#    print(f"Bonjour, {nom} !") 
#dire_bonjour("Alice")  # Affichera « Bonjour, Alice ! »

#print("---------------------------------------------------")
#Exemples de fonctions pour un système de facturation
#Vérifier les informations client
#def validerClient(client):
#    """ Vérifie que le client a un nom et une adresse valides. """
#    if "nom" in client and "adresse" in client:
#        return True
#    return False

#Calculer le sous-total des articles
#def calculerSousTotal(articles):
#    """ Calcule le total des articles avant taxes. """
#    total = 0
#    for article in articles:
#        total += article["prix"] * article["quantite"]
#    return total

# Exemple d’utilisation :
#articles = [
#    {"nom": "Ordinateur", "prix": 800, "quantite": 1},
#    {"nom": "Clavier", "prix": 50, "quantite": 2}
#]
#print(calculerSousTotal(articles))  # Affichera 900

#Appliquer les taxes (TVA, etc.)
#def appliquerTaxes(sousTotal, tauxTVA=20):
#    """ Applique la TVA au sous-total. """
#    return sousTotal * (1 + tauxTVA / 100)

#Exemple d’utilisation :
#sousTotal = 900
#totalTTC = appliquerTaxes(sousTotal)
#print(totalTTC)  # Affichera 1080 (900 + 20%)

#Générer la facture finale
#def genererFacture(client, articles):
#    """ Génére une facture détaillée. """
#    if not validerClient(client):
#        return "Erreur : informations client invalides"
 
#    sousTotal = calculerSousTotal(articles)
#    totalTTC = appliquerTaxes(sousTotal)
 
#    facture = f"Facture pour {client['nom']}\n"
#    facture += f"Adresse : {client['adresse']}\n\n"
   
#    facture += "Articles :\n"
#    for article in articles:
#        facture += f"- {article['nom']} x{article['quantite']} : {article['prix']}€\n"
   
#    facture += f"\nSous-total : {sousTotal}€\n"
#    facture += f"Total (TTC) : {totalTTC}€\n"
 
#    return facture

# Exemple d’utilisation :
#client = {"nom": "Jean Dupont", "adresse": "10 rue de Paris, 75000 Paris"}
#print(genererFacture(client, articles))

#Code sans réutilisation (redondant)
## Validation de l'inscription
#email = "jean.dupont@exemple.com"
#if "@" not in email or "." not in email:
#    print("Email invalide")
 
#telephone = "0612345678"
#if not telephone.isdigit() or len(telephone) != 10:
#    print("Numéro de téléphone invalide")
 
#mot_de_passe = "Azerty123!"
#if len(mot_de_passe) < 8:
#    print("Mot de passe trop court")

#Code optimisé avec une fonction (réutilisable)
#def valider_utilisateur(email, telephone, mot_de_passe):
#    """ Vérifie si les informations utilisateur sont valides """
#    erreurs = []
   
#    if "@" not in email or "." not in email:
#        erreurs.append("Email invalide")
   
#    if not telephone.isdigit() or len(telephone) != 10:
#""        erreurs.append("Numéro de téléphone invalide")
   
#    if len(mot_de_passe) < 8:
#        erreurs.append("Mot de passe trop court")
   
#    return erreurs if erreurs else "Données valides"
 
# Vérification pour l'inscription
#print(valider_utilisateur("jean.dupont@exemple.com", "0612345678", "Azerty123!"))
 
# Vérification pour la mise à jour du profil
#print(valider_utilisateur("jean.dupont@", "061234", "123"))

#Utiliser un test unitaire automatisé
#import unittest

#class TestFonctions(unittest.TestCase):
#    def test_appliquer_tva(self):
#        self.assertEqual(appliquer_tva(100), 120)  # Test avec taux par défaut
#        self.assertEqual(appliquer_tva(200, 10), 220)  # Test avec un autre taux
#        self.assertEqual(appliquer_tva(0), 0)  # Cas limite : montant nul
#        self.assertAlmostEqual(appliquer_tva(99.99), 119.99, places=2)  # Test de précision

# Exécuter les tests
#if __name__ == "__main__":
#    unitest.main()

#Test unitaire simplifié en pseudo-code :
#FONCTION tester_appliquer_tva()
#    // Test avec taux par défaut (20%)
#    resultat1 ← appliquer_tva(100)
#    SI resultat1 = 120 ALORS
#        AFFICHER "Test 1 réussi : 100€ + 20% = 120€"
#    SINON
#        AFFICHER "Test 1 échoué : attendu 120, obtenu ", resultat1
#    FIN SI
    
#    // Test avec un taux personnalisé (10%)
#    resultat2 ← appliquer_tva(200, 10)
#    SI resultat2 = 220 ALORS
#        AFFICHER "Test 2 réussi : 200€ + 10% = 220€"
#    SINON
#        AFFICHER "Test 2 échoué : attendu 220, obtenu ", resultat2
#    FIN SI
    
#    // Test avec un montant nul
#    resultat3 ← appliquer_tva(0)
#    SI resultat3 = 0 ALORS
#        AFFICHER "Test 3 réussi : 0€ + 20% = 0€"
#    SINON
#        AFFICHER "Test 3 échoué : attendu 0, obtenu ", resultat3
#    FIN SI
    
#    // Test de précision
#    resultat4 ← appliquer_tva(99.99)
#    SI ARRONDIR(resultat4, 2) = 119.99 ALORS
#        AFFICHER "Test 4 réussi : 99.99€ + 20% = 119.99€"
#    SINON
#        AFFICHER "Test 4 échoué : attendu 119.99, obtenu ", resultat4
#    FIN SI
#FIN FONCTION

#// Exécute les tests
#tester_appliquer_tva()

#Validation d'entrées
#Vérifier si une adresse e-mail est correcte
#FONCTION valider_email(email)
#    // Vérification simplifiée d'un email
#    SI email CONTIENT "@" ET email CONTIENT "." ALORS
#        // Vérifier que le @ est avant le dernier point
#        position_arobase ← TROUVER_POSITION("@", email)
#        position_dernier_point ← TROUVER_DERNIERE_POSITION(".", email)
        
#        SI position_arobase < position_dernier_point ALORS
#            RETOURNER VRAI
#        SINON
#            RETOURNER FAUX
#        FIN SI
#    SINON
#        RETOURNER FAUX
#    FIN SI
#FIN FONCTION

#// Tests
#AFFICHER valider_email("contact@entreprise.com")  // Affichera VRAI
#AFFICHER valider_email("invalide@@exemple.com")  // Affichera FAUX

#Exemple en Python
#import re

#def valider_email(email):
#    """ Vérifie si une adresse e-mail est valide """
#    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#    return bool(re.match(pattern, email))

# Tests
#print(valider_email("contact@entreprise.com"))  # ✅ True
#print(valider_email("invalide@@exemple.com"))   # ❌ False

#Transformation de formats
#Exemple : reformater un numéro de téléphone français
#/*
#* FORMATER_TELEPHONE
#* -----------------
#* Description: Reformate un numéro de téléphone français en affichage standard
#* 
#* Paramètres:
#*   - numero (texte): Le numéro de téléphone à formater
#* 
#* Résultat:
#*   (texte) Le numéro formaté ou "Numéro invalide"
#*/
#FONCTION formater_telephone(numero)
#   // Supprimer les espaces et tirets
#   numero_propre ← REMPLACER(numero, " ", "")
#   numero_propre ← REMPLACER(numero_propre, "-", "")
   
#   // Vérifier si le numéro est valide
#   SI LONGUEUR(numero_propre) = 10 ET SEULEMENT_CHIFFRES(numero_propre) ALORS
#       // Formatter le numéro avec des espaces
#       resultat ← ""
#       resultat ← resultat + SOUS_CHAINE(numero_propre, 0, 2) + " "
#       resultat ← resultat + SOUS_CHAINE(numero_propre, 2, 4) + " "
#       resultat ← resultat + SOUS_CHAINE(numero_propre, 4, 6) + " "
#       resultat ← resultat + SOUS_CHAINE(numero_propre, 6, 8) + " "
#       resultat ← resultat + SOUS_CHAINE(numero_propre, 8, 10)
#       RENVOYER resultat
#   SINON
#       RENVOYER "Numéro invalide"
#   FIN SI
#FIN FONCTION

#// Tests
#AFFICHER formater_telephone("0612345678")    // Affiche "06 12 34 56 78"
#AFFICHER formater_telephone("01-23-45-67-89") // Affiche "01 23 45 67 89" 
#AFFICHER formater_telephone("12345")         // Affiche "Numéro invalide"

#Exemple en Python 
#def formater_telephone(numero):
#    """ Reformate un numéro de téléphone français en affichage standard """
#    numero = numero.replace(" ", "").replace("-", "")
#    if len(numero) == 10 and numero.isdigit():
#        return f"{numero[:2]} {numero[2:4]} {numero[4:6]} {numero[6:8]} {numero[8:]}"
#    return "Numéro invalide"

# Tests
#print(formater_telephone("0612345678"))  # ✅ "06 12 34 56 78"
#print(formater_telephone("01-23-45-67-89"))  # ✅ "01 23 45 67 89"
#print(formater_telephone("12345"))  # ❌ "Numéro invalide"

#Validation des saisies
#Exemple : vérifier qu'une date de réservation est valide
#/*
# * VERIFIER_DATE_RESERVATION
# * ------------------------
# * Description : vérifie qu'une date de réservation est valide et dans le futur
# * 
# * Paramètres :
# *   - date_str (texte): La date à vérifier au format "AAAA-MM-JJ"
# * 
# * Résultat :
# *   (booléen) VRAI si la date est valide et future, FAUX sinon
# */
#FONCTION verifier_date_reservation(date_str)
#    // Essayer de convertir la chaîne en date
#    ESSAYER
#        // Convertir la chaîne de texte en date
#        date_resa ← CONVERTIR_EN_DATE(date_str, format: "AAAA-MM-JJ")
        
#        // Obtenir la date d'aujourd'hui
#        date_aujourd_hui ← OBTENIR_DATE_ACTUELLE()
        
#        // Vérifier si la date est dans le futur
#        SI date_resa ≥ date_aujourd_hui ALORS
#            RENVOYER VRAI
#        SINON
#            RENVOYER FAUX
#        FIN SI
    
#    // Si la conversion échoue (format incorrect)
#    ATTRAPER ERREUR
#        RENVOYER FAUX
#    FIN ESSAYER
#FIN FONCTION

#// Tests
#AFFICHER verifier_date_reservation("2025-06-15")     // Affiche VRAI (date valide)
#AFFICHER verifier_date_reservation("2022-01-01")     // Affiche FAUX (date passée)
#AFFICHER verifier_date_reservation("invalid-date")   // Affiche FAUX (format incorrect)

#Exemple en Python :
#from datetime import datetime

#def verifier_date_reservation(date_str):
#    """ Vérifie que la date de réservation est valide et dans le futur """
#    try:
#        date_resa = datetime.strptime(date_str, "%Y-%m-%d")
#        if date_resa >= datetime.today():
#            return True
#        else:
#            return False
#    except ValueError:
#        return False

# Tests
#print(verifier_date_reservation("2025-06-15"))  # ✅ True (date valide)
#print(verifier_date_reservation("2022-01-01"))  # ❌ False (date passée)
#print(verifier_date_reservation("invalid-date"))  # ❌ False (format incorrect)

#Exemple : afficher une confirmation de réservation bien formatée
#def afficher_confirmation(nom, date, personnes):
#    """ Génère un message formaté confirmant la réservation """
#    return f"✅ Réservation confirmée pour {nom} le {date} pour {personnes} personne(s)."

# Test
#print(afficher_confirmation("Dupont", "2025-06-15" 2))

#Solution en pseudo-code :
#// Système de comptabilité simplifié en pseudo-code

#// 1. Enregistrement d'une transaction
#FONCTION enregistrer_transaction(transactions, date, description, montant, type_op)
#    // Ajoute une transaction à la liste des transactions
#    nouvelle_transaction ← [date, description, montant, type_op]
#    AJOUTER nouvelle_transaction À transactions
#    RETOURNER transactions
#FIN FONCTION

#// 2. Calcul de la TVA
#FONCTION calculer_tva(montant, taux)
#    // Si aucun taux n'est spécifié, utiliser 20%
#    SI taux EST VIDE ALORS
#        taux ← 20
#    FIN SI
    
#    // Calculer et arrondir la TVA
#    tva ← montant * (taux / 100)
#    tva ← ARRONDIR(tva, 2)  // Arrondir à 2 décimales
    
#    RETOURNER tva
#FIN FONCTION

#// 3. Génération de rapport
#FONCTION generer_rapport(transactions)
#    revenus ← 0
#    depenses ← 0
    
#    POUR CHAQUE transaction DANS transactions FAIRE
#        montant ← transaction[2]
#        type_op ← transaction[3]
        
#        SI type_op = "revenu" ALORS
#            revenus ← revenus + montant
#        SINON
#            depenses ← depenses + montant
#        FIN SI
#    FIN POUR
    
#    bilan ← revenus - depenses
    
#    rapport ← "Revenus: " + revenus + "€\n"
#    rapport ← rapport + "Dépenses: " + depenses + "€\n"
#    rapport ← rapport + "Bilan: " + bilan + "€"
    
#    RETOURNER rapport
#FIN FONCTION

#// Exemple d'utilisation
#transactions ← []
#transactions ← enregistrer_transaction(transactions, "2025-03-27", "Vente produit X", 150.0, "revenu")
#transactions ← enregistrer_transaction(transactions, "2025-03-27", "Achat fournitures", 50.0, "dépense")

#tva ← calculer_tva(150)
#AFFICHER "TVA sur 150€ :", tva

#apport ← generer_rapport(transactions)
#AFFICHER rapport

#Solution en Python
#import csv
#from datetime import datetime

# 1️. Enregistrement d'une Transaction
#def enregistrer_transaction(fichier, date, description, montant, type_op):
#    """ Enregistre une transaction dans un fichier CSV """
#    with open(fichier, "a", newline='', encoding="utf-8") as f:
#        writer = csv.writer(f)
#        writer.writerow([date, description, montant, type_op])

# 2️. Calcul de la TVA
#def calculer_tva(montant, taux=20):
#    """ Calcule la TVA sur un montant donné """
#    return round(montant * (taux / 100), 2)

# 3️. Génération de Rapport
#def generer_rapport(fichier):
#    """ Génère un rapport des revenus et dépenses """
#    revenus = 0
#    depenses = 0

#    with open(fichier, newline='', encoding="utf-8") as f:
#        reader = csv.reader(f)
#        for ligne in reader:
#            montant = float(ligne[2])
#            if ligne[3] == "revenu":
#                revenus += montant
#            else:
#                depenses += montant

#    return f"💰 Revenus: {revenus:.2f}€\n💸 Dépenses: {depenses:.2f}€\n📊 Bilan: {revenus - depenses:.2f}€"

# 4️. Archivage des Données
#def archiver_donnees(fichier, archive):
 #   """ Copie les données actuelles vers un fichier d'archive """
#    with open(fichier, "r", encoding="utf-8") as f_source, open(archive, "w", encoding="utf-8") as f_dest:
#        f_dest.write(f_source.read())

# 🔥 Utilisation du Système Comptable
#fichier_transactions = "comptabilite.csv"

# Exemple d'ajout de transactions
#enregistrer_transaction(fichier_transactions, "2025-03-27", "Vente produit X", 150.0, "revenu")
#enregistrer_transaction(fichier_transactions, "2025-03-27", "Achat fournitures", 50.0, "dépense")

# Calcul de TVA
#print("TVA sur 150€ :", calculer_tva(150))

# Génération du rapport
#print(generer_rapport(fichier_transactions))

# Archivage
#archiver_donnees(fichier_transactions, "archive_compta.csv")

#
#






