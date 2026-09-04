#--SYSTÈME DE GESTION DE BIBLIOTHÈQUE--#
#Base de données (liste globale pour stocker les dicitionaires de livres) 
livres = []

#1. fonction pour ajouter un livre (create)
def ajouter_livre(livre):
    """ 
    Ajoute un nouveau livre au catalogue.
    Args: livre (dict) - les informations du livre.
    """
#Utiliser la méthode des listes pour insérer à la fin
    livres.append(livre)
    print(f"livre ajouté : {livre['titre']}")

    #2. Fonction pour rechercher un livre (read)
def rechercher_livre(critere, valeur):
    """ 
    Recherche un livre selon un critère précis.
    Args:
        critere (str): La clé de recherche (ex: 'titre', 'auteur')
        valeur (str): La valeur à recherchée.
    Returns: List - Liste des résultats correspondants.
    """
    resultats = []

# Parcourir la liste Globale des livres
    for livre in livres:
# Vérifier si le critère existe et si la valeur correspond (en ignorant la casse)
        if critere in livre and valeur.lower() in str(livre[critere]).lower():
            resultats.append(livre)
#Renvoyer la liste des résultats au programme principal
    return resultats
#--- EXÉCUTION DU PROGRAMME ---
print("--- INITIALISATION DU CATOLOGUE ---")

#Création d'un livre (Dictionnaire)
livre1 = {
    "titre": "La Bicyclette Bleue",
    "auteur": "Régine Deforges",
    "isbn": "978-2859564124",
    "année": 1981,
    "categorie": "Fiction",
    "disponible": True
}

#Appel des focntions
ajouter_livre(livre1)

print("\n--- Recherche en cours ---")
recherche = rechercher_livre("auteur", "Deforges")
print("Résultat de la recherche :", recherche)