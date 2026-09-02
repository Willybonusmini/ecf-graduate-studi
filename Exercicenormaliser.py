
# 1. Définition de la fonction (Logique métier uniquement)
def normaliser_client(nom, code_postal, telephone, email):
    
    # Mettre le nom en majuscules
    nom_propre = nom.upper()
    
    # Nettoyer le code postal (enlever les espaces inutiles autour)
    cp_propre = code_postal.strip()
    
    # Uniformiser le numéro de téléphone (enlever les tirets puis les espaces)
    tel_propre = telephone.replace("-", "").replace(" ", "").strip()
    
    # Nettoyer l'email (enlever les espaces autour ET mettre en minuscules)
    email_propre = email.strip().lower()
    
    # Renvoyer les données propres
    return nom_propre, cp_propre, tel_propre, email_propre


# 2. Entrées utilisateur (Exécution du script)
print("--- SYSTÈME DE NORMALISATION ---")
saisie_nom = input("Entrez votre nom : ")
saisie_cp = input("Entrez votre code postal : ")
saisie_tel = input("Entrez votre téléphone : ")
saisie_email = input("Entrez votre email : ")

# 3. Appel de la fonction et stockage des résultats
nom_final, cp_final, tel_final, email_final = normaliser_client(saisie_nom, saisie_cp, saisie_tel, saisie_email)

# 4. Affichage final
print("\n--- Informations normalisées ---")
print("Nom :", nom_final)
print("Code Postal :", cp_final)
print("Téléphone :", tel_final)
print("Email :", email_final)

git commit -m "feat: add client normalization function and user input handling" 