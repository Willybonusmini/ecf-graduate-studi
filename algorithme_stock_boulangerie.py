# --- CONTRÔLE DE STOCK (BOULANGERIE DUPAIN) ---

def verifier_stock_ingredient():
    """
    Algorithme de vérification des stocks.
    Traduction d'un besoin métier (alerte rupture) en instructions machine.
    """
print("--- SYSTÈME DE GESTION DES STOCKS ---")

#1. Entrée des données (Conversion explicite pour éviter les erreurs de type)
nom_ingredient = input("Entrez le nom de l'ingredient : ")

# Sécurisation des entrées numériques via la fonction de conversion[cite: 8]
quantite_actuelle = int(input("Entrez la quantité actuelle (en kg) :"))
seuil_critique = int(input("Entrez le seuil critique d'alerte (en kg) : "))

# 2. Traitement logique (Structure conditionnelle)[cite: 8]
if quantite_actuelle <= seuil_critique:
    # 3. Sortie : Alerte d'approvisionnement[cite: 8]
    print(f"ALERTE : Le stock de {nom_ingredient} est critique {quantite_actuelle} kg restants).")
    print("Action requise : Commander immédiatement.")
else:
    # Sortie : Stock nominal[cite: 8]
    print(f"INFO : Le stock de {nom_ingredient} est suffisant.")

# Exécution du programme
if __name__ == "__main__":
    verifier_stock_ingredient()


