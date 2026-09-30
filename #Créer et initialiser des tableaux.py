#Créer et initialiser des tableaux


jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
#tableau = [] parfois on a besoin de faire une tableau vide pour le remplir plus tard
taille = len(jours)

produits = ["Pommes", "Bananes", "Oranges", "Poires"]
stocks = [0] * len(produits)  # Crée un tableau de stocks initialisé à 0 pour chaque produit

print("stock: ", stocks)

#matrice pour organizer des tableaux: Déclarer matrice ← [
#    [15, 14, 16],  // Élève 1
#    [12, 10, 14],  // Élève 2
#    [18, 17, 19]   // Élève 3
#]
#Afficher matrice[1][1]  // Affiche : 10

#declarer une matrice : Déclarer matrice[3][3] ← [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#matrice[0][0] ← 5
#matrice[1][1] ← 10
#matrice[2][2] ← 15

#déclarer notes tableaux tridimensionnel : Déclarer notes_classes ← [
#    [
#        [15, 14, 16],
#        [12, 10, 14],
#        [18, 17, 19]
#    ],
#    [
#        [11, 13, 12],
#        [14, 15, 16],
#        [10, 9, 8]
#    ]
#]

#Afficher notes_classes[1][1][2]  // Affiche : 16

# listes equivalentes à des tableaux multidimensionnels
#Déclarer notes_classes ← [
#    [
#        [15, 14, 16],
#        [12, 10, 14],
#        [18, 17, 19]
#    ],
#    [
#        [11, 13, 12],
#        [14, 15, 16],
#        [10, 9, 8]
#    ]
#]

#Afficher notes_classes[1][1][2]  // Affiche : 16

#access a une liste: 
#Déclarer fruits ← ["Pomme", "Banane", "Cerise", "Orange", "Mangue"]

#Afficher fruits[0]     // Affiche : Pomme
#Afficher fruits[2]     // Affiche : Cerise
#Afficher fruits[longueur(fruits) - 1]   // Affiche : Mangue (dernier élément)

#Si 10 < longueur(fruits) alors
#    Afficher fruits[10]
#Sinon
#    Afficher "L'index est hors des limites du tableau."

#exemple d'erreur
#Si 10 < longueur(fruits) alors
#    Afficher fruits[10]
#Sinon
#    Afficher "L'index est hors des limites du tableau."

#longueur de tableau
#Déclarer index ← 3
#Si index ≥ 0 et index < longueur(fruits) alors
#    Afficher fruits[index]
#Sinon
#    Afficher "Index invalide !"
#Fin Si


#acces a un tableau 1D unidimensionnel
#Déclarer produits ← ["Téléphone", "Ordinateur", "Tablette"]

#Afficher produits[1]         // Affiche : "Ordinateur"
#Afficher produits[longueur(produits) - 1]  // Affiche : "Tablette" (dernier élément)

#Acces a un tableau 2D Bidimensionnel

#Déclarer matrice ← [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#Afficher matrice[1][2]   // Affiche : 6 (2e ligne, 3e colonne)

#Déclarer matrice ← [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#Afficher matrice[1][2]   // Affiche : 6 (2e ligne, 3e colonne)

#acces a un tableau 3D Tridimensionnel 
#Déclarer tableau_3d ← [
#    [[1, 2], [3, 4]],
#    [[5, 6], [7, 8]]
#]

#Afficher tableau_3d[1][0][1]  // Affiche : 6 (2e bloc, 1re ligne, 2e colonne)

#Exemples plus complexes de notes
#Déclarer notes_classes ← [
#    [   // Classe 1
#        [15, 14, 16],  
#        [12, 10, 14],
#        [18, 17, 19]
#    ],
#    [   // Classe 2
#        [11, 13, 12],  
#        [14, 15, 16],
#        [10, 9, 8]
#    ]
#]

#Afficher notes_classes[1][1][2]  
#// Affiche : 16 (2e classe, 2e élève, 3e matière)

# modifier un valeur simple
# Déclarer scores ← [10, 15, 20, 25]
# scores[2] ← 30
# Afficher scores  // Affiche : [10, 15, 30, 25]

# modifier un valeur dans une matrice
# Déclarer matrice ← [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

# matrice[1][2] ← 99
# Afficher matrice
# // Affiche : [[1, 2, 3], [4, 5, 99], [7, 8, 9]]

# ajouter une element
# Ajouter "Casque" à produits
# Afficher produits  // ['Smartphone', 'Ordinateur', 'Tablette', 'Casque']

# supprimer un element
# Supprimer "Ordinateur" de produits
# Afficher produits  // ['Smartphone', 'Tablette', 'Casque']

# Gestion de stock avec des tableaux
#produits = ["baguette", "confiture", "fromage"]
#stock = [20, 15, 8]

#print("stock confiture: ", stock[1])

#stock[0] = stock[0] - 2

#print("stock baguette: ", stock[0])

#produits.append("miel")
#stock.append(5)

#for in range(len(produits)):
#    print("produit: ", produits[i])
#    print("stock: ", stock[i])

#Déclarer notes[5] // Crée un tableau de 5 cases

#notes[0] ← 15

#notes[1] ← 18

#notes[2] ← 12

#notes[3] ← 10

#notes[4] ← 14

#Déclarerjours_semaine ← ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

# remplissage avec une boucle
#Déclarer carres ← tableau vide

#Pour i de 1 à 5, faire :

#Ajouter (i × i) à carres

#Fin Pour

#tableau à 2 dimensions (matrice)
#Déclarer matrice ← [
#    [15, 14, 16],  // Élève 1
#    [12, 10, 14],  // Élève 2
#    [18, 17, 19]   // Élève 3
#]
#Afficher matrice[1][1]  // Affiche : 10

#On crée une matrice vide ou pré-remplie avec une valeur (ex. : 0), puis on peut la modifier ensuite.
#Déclarer matrice[3][3] ← [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#matrice[0][0] ← 5
#matrice[1][1] ← 10
#matrice[2][2] ← 15

#Un tableau à 3 dimensions contient plusieurs matrices. Cela permet de représenter des données plus complexes (ex : plusieurs classes).
#Déclarer notes_classes ← [
#    [
#        [15, 14, 16],
#        [12, 10, 14],
#        [18, 17, 19]
#    ],
#    [
#        [11, 13, 12],
#        [14, 15, 16],
#        [10, 9, 8]
#    ]
#]

#Afficher notes_classes[1][1][2]  // Affiche : 16


#Déclarer notes_classes ← [
#    [
#        [15, 14, 16],
#        [12, 10, 14],
#        [18, 17, 19]
#    ],
#    [
#        [11, 13, 12],
#        [14, 15, 16],
#        [10, 9, 8]
#    ]
#]

#Afficher notes_classes[1][1][2]  // Affiche : 16

#indexation 
#Exemple d'accès aux éléments d'une liste :

#Déclarer fruits ← ["Pomme", "Banane", "Cerise", "Orange", "Mangue"]

#Afficher fruits[0]     // Affiche : Pomme
#Afficher fruits[2]     // Affiche : Cerise
#Afficher fruits[longueur(fruits) - 1]   // Affiche : Mangue (dernier élément)

#Exemple d’erreur et de prévention :
#Si 10 < longueur(fruits) alors
#    Afficher fruits[10]
#Sinon
#    Afficher "L'index est hors des limites du tableau."

#Toujours vérifier la longueur du tableau avant d’accéder à un indice
#Utiliser len() pour éviter les erreurs
#Déclarer index ← 3
#Si index ≥ 0 et index < longueur(fruits) alors
#    Afficher fruits[index]
#Sinon
#    Afficher "Index invalide !"
#Fin Si

#Accès à un tableau 1D (unidimensionnel)
#Déclarer produits ← ["Téléphone", "Ordinateur", "Tablette"]

#Afficher produits[1]         // Affiche : "Ordinateur"
#Afficher produits[longueur(produits) - 1]  // Affiche : "Tablette" (dernier élément)

# Accès à un tableau 2D (bidimensionnel)
#Déclarer matrice ← [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#Afficher matrice[1][2]   // Affiche : 6 (2e ligne, 3e colonne)

#Accès à un tableau 3D (tridimensionnel)
#Déclarer tableau_3d ← [
#    [[1, 2], [3, 4]],
#    [[5, 6], [7, 8]]
#]

#Afficher tableau_3d[1][0][1]  // Affiche : 6 (2e bloc, 1re ligne, 2e colonne)

#Exemple plus complexe - notes de classes
#Déclarer notes_classes ← [
#    [   // Classe 1
#        [15, 14, 16],  
#        [12, 10, 14],
#        [18, 17, 19]
#    ],
#    [   // Classe 2
#        [11, 13, 12],  
#        [14, 15, 16],
#        [10, 9, 8]
#    ]
#]

#Afficher notes_classes[1][1][2]  
#// Affiche : 16 (2e classe, 2e élève, 3e matière)

#Modifier une valeur simple :
#Déclarer scores ← [10, 15, 20, 25]
#scores[2] ← 30
#Afficher scores  // Affiche : [10, 15, 30, 25]

#Modifier une valeur dans une matrice :
#Déclarer matrice ← [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#matrice[1][2] ← 99
#Afficher matrice
#// Affiche : [[1, 2, 3], [4, 5, 99], [7, 8, 9]]

#Ajouter un élément
#Ajouter "Casque" à produits
#Afficher produits  // ['Smartphone', 'Ordinateur', 'Tablette', 'Casque']

#Supprimer un élément
#Supprimer "Ordinateur" de produits
#Afficher produits  // ['Smartphone', 'Tablette', 'Casque']

#Gestion de stock avec des tableaux 
#Produits = ["baguette", "confiture", "fromage"]
#stock = [20, 15, 8]

#print("stock confiture: ", stock[1])
#stock[0] = stock[0 - 2]
#print("stock baguette: ", stock[0])
#produits.append("miel")
#stock.append(5)

#Parcourir un tableau avec une boucle
#Boucle for sur une liste

#    Afficher élément
#Fin pour

#Boucle for avec index
#Pour i allant de 0 à longueur(tableau) - 1 faire
#    Afficher "Élément à position", i, ":", tableau[i]
#Fin pour

#Parcours avec index et valeur (comme enumerate)
#Pour i allant de 0 à longueur(tableau) - 1 faire
#    valeur ← tableau[i]
#    Afficher i, valeur
#Fin pour

#Boucle while pour parcourir un tableau
#i ← 0
#Tant que i < longueur(tableau) faire
#    Afficher tableau[i]
#    i ← i + 1
#Fin tant que

#Calculer la somme et la moyenne
#somme ← 0
#Pour chaque valeur dans tableau faire
#    somme ← somme + valeur
#Fin pour

#Si longueur(tableau) > 0 alors
#    moyenne ← somme / longueur(tableau)
#Sinon
#    moyenne ←0
#Fin si

#Trouver le minimum et le maximum
#min ← tableau[0]
#max ← tableau[0]

#Pour chaque valeur dans tableau faire
#    Si valeur < min alors
#        min ← valeur
#    Fin si
#    Si valeur > max alors
#        max ← valeur
#    Fin si
#Fin pour

#Calculer la médiane
#Trier tableau
#n ← longueur(tableau)

#Si n est impair alors
#    médiane ← tableau[n // 2]
#Sinon
#    médiane ← (tableau[n // 2 - 1] + tableau[n // 2]) / 2
#Fin si

#Recherche et filtrage dans un tableau
#trouvé ← Faux
#Pour chaque valeur dans tableau faire
#    Si valeur = cible alors
#        trouvé ← Vrai
#        Sortir de la boucle
#    Fin si
#Fin pour

#Si trouvé alors
#    Afficher "Élément trouvé"
#Sinon
#    Afficher "Pas trouvé"
#Fin si

#Trouver l’indice d’un élément
#Pour i allant de 0 à longueur(tableau) - 1 faire
#    Si tableau[i] = cible alors
#        Afficher "Indice :", i
#        Sortir de la boucle
#    Fin si
#Fin pour

#Filtrage des éléments selon un critère
#nouveau_tableau ← tableau vide

#Pour chaque valeur dans tableau faire
#    Si valeur respecte la condition alors
#        Ajouter valeur à nouveau_tableau
#    Fin si
#Fin pour

#Différences entre liste et tableau
## Liste contenant différents types de données
#ma_liste ← [42, "Texte", 3.14, Vrai]Afficher ma_liste

#comprendre les listes

#clients = ("alice ", "bob ", "charlie", 2)

#clients.append("David") # Ajoute "David" à la fin de la liste

#clients.remove("Bob")#supprime bob de la liste 

#Liste dynamique (type classique)
#ma_liste ← [1, 2, 3]
#Ajouter 4 à la fin de ma_liste
#Afficher ma_liste  # Résultat : [1, 2, 3, 4]

#Cas 1 : file d’attente de clients (exemple d’une banque 🏦)
#file_clients ← liste vide

#Ajouter client1
#Ajouter client2
#Retirer premier client quand il est servi

#Cas 2 : historique d'actions utilisateur (exemple d’un site web
#historique ← liste vide

#Ajouter action1
#Ajouter action2
#Annuler dernière action (retirer le dernier élément)

#Cas 3 : catalogue de produits d’une boutique en ligne
#catalogue ← ["Chaussures", "Veste", "Sac"]

#Ajouter "Chapeau"
#Retirer "Veste"
#Afficher catalogue

#Déclarer et initialiser une liste
## Créer une liste vide
#ma_liste ← []

# Créer une liste avec des valeurs
#fruits ← ["Pomme", "Banane", "Orange"]

#Ajouter et supprimer des éléments
#Ajout d'éléments

## Ajouter à la fin
#fruits.append("Kiwi")

# Insérer à une position spécifique
#fruits.insert(1, "Mangue")  # insère "Mangue" à l'indice 1

#Suppression d'éléments
## Supprimer une valeur spécifique (la première trouvée)
#fruits.remove("Pomme")

# Supprimer par position et récupérer l’élément
#element_supprimé ← fruits.pop(2)

# Supprimer un élément sans le récupérer
#del fruits[0]

#Tri d’une liste

## Trier la liste (modifie la liste originale)
#ma_liste.sort()

# Créer une nouvelle liste triée (ne modifie pas l’originale)
#liste_triée ← sorted(ma_liste)

# Inverser l’ordre des éléments
#ma_liste.reverse()

#Recherche dans une liste
## Vérifier la présence d’un élément
#si "Banane" in fruits :
#    afficher("Présent")

# Obtenir l’indice d’un élément
#indice ← fruits.index("Banane")

#manipuler les listes 

#taches = ["envoyer un email", "préparer une reunion", "appeler un client"]
#taches.append("commander les fournitures")
#print(taches)
#taches.remove("envoyer un email")
#print(taches)
#taches[0], taches[1] = taches[1], taches[0]
#print(taches)
#if "appeler un client" in taches:
#    print("La tâche 'appeler un client' est présent dans la liste.")

#taches.clear()
#print("vide", taches)









