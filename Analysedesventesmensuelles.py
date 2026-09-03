print("--Analyse des ventes Mensuelles--")

#Déclaration du tableau de données
ventes = [1500, 1800, 1700, 1600, 1750]

#calcul de la somme totale des ventes
somme_totale = sum(ventes)

#calcul de la moyenne (somme diviséé par la taille du tableau)
moyenne_ventes = somme_totale / len(ventes)

#identification de la meilleure vente 
meilleure_mois_valeur = max(ventes)

#trouver l'indice du mois correspondant au meilleure mois
meilleure_mois_indice = ventes.index(meilleure_mois_valeur)

#filtrer les ventes inférieures à la moyenne
mois_faibles = []
for vente in ventes:
    if vente < moyenne_ventes:
        mois_faibles.append(vente)

#affichage des résultats pour l'entreprise
print(f"Total des ventes : {somme_totale} €")
print(f"Moyenne des ventes : {moyenne_ventes} €")
print(f"Mois le plus performant : Mois n°{meilleure_mois_indice + 1} avec {meilleure_mois_valeur} €")
print(f"Ventes sous la moyenne : {mois_faibles}")