#Exercicio

nom_product = str("geminiwilson_peças") #nom du produit
price = float(100.0) # le prix du produit 
stock = int(50) #quantité en stock
tva = 0.2 #tva 20% 
print(f"Le produit {nom_product} est disponible.")

if price > 10 and stock > 2:
    print(f"Le produit {nom_product} est disponible à {price}€ avec un stock de {stock} unités.")
    prix_total = round(price * (1 + tva), 2) #prix total avec tva
    print("Le prix du produit avec TVA est: " + str(prix_total) + "€")






    