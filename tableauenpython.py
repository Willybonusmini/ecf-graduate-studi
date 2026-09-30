#tableaux en python.



nombres = [10, 20, 30, 40, 50]

print(nombres[0])  # affiche 10 (l'élement à l'indice 0)

#Regrouper des données liées
# Tableau des notes d'une classe
notes = [12, 15, 14, 10, 18]

#Accès rapide aux éléments via un indice
# Accéder au troisième élément du tableau des notes
print(notes[2]) # Affiche 14, car l'élément à l'indice 2 est 14

#calcule de la moyenne des notes
notes ← liste de notes
    somme ← 0

    Pour chaque note dans notes faire
        somme ← somme + note
    Fin Pour
    moyenne ← somme / nombre d'éléments dans notes
    Afficher moyenne

#gérer des collections d'éléments de taille variable
# Ajouter une note au tableau
notes.append(16)
print(notes) # Affiche [12, 15, 14, 10, 18, 16]

#introduction aux tableaux 
noms = ["Alice", "Bob", "Charlie"]

print(noms[0])  # Affiche "Alice" (l'élément à l'indice 0)
print(noms[2])  # Affiche "Charlie" (l'élément à l'indice 2)

for nom in noms:
    print(nom)  # Affiche chaque nom dans le tableau

clients = ["nina@exemple.fr", "jean@exemple.fr", "ema@exemple.fr"]
for email in clients:
    print("envoi d'un message à: " ,email)  # Affiche chaque email dans le tableau

#tableaux multidimensionnels
tableau_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
#tableau inidimensionnels(vecteurs)
vecteur = [10, 20, 30, 40, 50]

#tableau bidimensionnels (Matrices)
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#exemple d'accès à un élément spécifique dans une matrice
print(matrice[0][1])  # Affiche 2 (élément à la première ligne et deuxième colonne)

#Accès à un élément dans un tableau 3D
print(tableau_3d[1][0][1])  # Affiche 6 (élément au deuxième "bloc", première ligne, deuxième colonne)

#creer et initialiser des tableaux

jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
taille = len(jours)

produits = ["pomme", "poire", "orange", "banane", "fraise"]
stocks = [0] * len(produits)

print("stock: ", stocks)

#matrices de tableau 
Déclarer matrice ← [
    [15, 14, 16],  // Élève 1
    [12, 10, 14],  // Élève 2
    [18, 17, 19]   // Élève 3
]
Afficher matrice[1][1]  // Affiche : 10

#creation d'un tableau 2D
Déclarer matrice[3][3] ← [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrice[0][0] ← 5
matrice[1][1] ← 10
matrice[2][2] ← 15

#tableau a 3 dimensions
Déclarer notes_classes ← [
    [
        [15, 14, 16],
        [12, 10, 14],
        [18, 17, 19]
    ],
    [
        [11, 13, 12],
        [14, 15, 16],
        [10, 9, 8]
    ]
]

Afficher notes_classes[1][1][2]  // Affiche : 16

#






