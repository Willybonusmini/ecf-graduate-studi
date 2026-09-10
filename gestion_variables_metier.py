# --- MODULE DE GESTION DES VARIABLES ET DU STOCK (MODEFRANÇAISE) ---

def simuler_panier_client():
    """
    Simule la gestion d'un article, son prix, son stock dynamique
    et la mise à jour des indicateurs de la boutique en ligne.
    """
    print("--- SIMULATION E-COMMERCE : MODEFRANÇAISE ---")
    
    # 1. Déclaration et Initialisation des variables typées
    nom_produit = "Robe élégante"  # Type : str
    prix_unitaire = 79.99          # Type : float
    stock_actuel = 15              # Type : int
    en_stock = True                # Type : bool
    
    # 2. Traitement des quantités (Achat client de 3 articles)
    quantite_demandee = 3
    
    if en_stock and quantite_demandee <= stock_actuel:
        # Décrémentation du stock via l'opérateur combiné
        stock_actuel -= quantite_demandee

        # Calcul du prix total avec précision (arrondi pour éviter les dérives IEEE 754)
        prix_total = round(prix_unitaire * quantite_demandee, 2)

        # 3. Sortie formatée (Conversion explicite de types pour la concaténation)
        print("Produit : " + nom_produit)
        print("Prix total pour " + str(quantite_demandee) + " unités : " + str(prix_total) + " €")
        print("Stock restant après vente : " + str(stock_actuel))
    else:
        print("Rupture de stock ou quantité indisponible.")

# Exécution du programme
if __name__ == "__main__":
    simuler_panier_client()