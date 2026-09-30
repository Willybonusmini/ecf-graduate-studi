



# Dados do exercício
prix_article = 49.99
taux_remise = 15.75

# Cálculo da remessa (percentagem)
article_remise = prix_article * (taux_remise / 100)

# Cálculo do preço final
prix_final = prix_article - article_remise

# Exibição do resultado
print(f"Le prix final est : {prix_final:.2f}")
