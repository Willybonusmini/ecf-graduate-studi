# --- ANALYSE DES VENTES MENSUELLES ---

ventes = [1200, 1500, 900, 2100, 1800, 2500, 3000, 2800, 2200, 1700, 1900, 2400]
mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

# 1. Calcul du total annuel (Utiliser la fonction native d'addition)
total_annuel = sum(ventes)
# 2. Calcul de la moyenne mensuelle (Diviser par la longueur du tableau)
moyenne_mensuelle = total_annuel / len(ventes)
# 3. Identification du mois avec le plus fort volume de ventes
vente_max = max(ventes)
index_max = ventes.index(vente_max)
mois_max = mois[index_max]

#--- EXÉCUTION DU SCRIPT ---
print("--- RAPPORT DE VENTES ---")
print(f"Total annuel : {total_annuel} €")
print(f"Moyenne mensuelle : {moyenne_mensuelle:.2f} €")
print(f"Meilleur mois : {mois_max} avec {vente_max} €")






