# --- MODULE D'ANALYSE DE DONNÉES (STRUCTURES DE DONNÉES) ---

# Tableau unidimensionnel de données financières
ventes_mensuelles = [1500, 1800, 1700, 1600, 1750]

# 1. Calculs Statistiques de Base
somme_ventes = sum(ventes_mensuelles)
moyenne_ventes = somme_ventes / len(ventes_mensuelles)

# 2. Recherche d'Extrêmes et Indexation
meilleur_mois_valeur = max(ventes_mensuelles)
indice_meilleur_mois = ventes_mensuelles.index(meilleur_mois_valeur)

#3. Filtrage dynamique (Compréhension de liste conditionnelle)[cite: 3]
mois_faibles = [valeur for valeur in ventes_mensuelles if valeur < moyenne_ventes]

# --- EXÉCUTION ET AFFICHAGE ---
print("--- RAPPORT D'ANALYSE DES VENTES ---")
print(f"Total des ventes : {somme_ventes} €")
print(f"Moyenne des ventes : {moyenne_ventes:.2f} €")
print(f"Mois le plus performant (indice {indice_meilleur_mois}) : {meilleur_mois_valeur} €")
print(f"Ventes sous la moyenne : {mois_faibles}")







