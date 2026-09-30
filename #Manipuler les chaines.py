#Manipuler les chaines  

prenom = "camille"
nom = "dupont"
année = 2025

debut = prenom [:3].lower()

longueur_nom = len(nom)

identifiant = debut + str(longueur_nom) + "-" + str(année)
print(identifiant)

print("-------------------------------------------------------------")

message = "Bonjour"
longueur = len(message)
print(longueur)  # Affiche : 7

print("-------------------------------------------------------------")

mot_de_passe = "abc123"
if len(mot_de_passe) < 8:
    print("Mot de passe trop court !")

print("-------------------------------------------------------------")

description = "Ceci est une longue description..."
if len(description) > 20:
    description = description[:20] + "..."
print(description)  # Affiche : Ceci est une longue...

print("-------------------------------------------------------------")

texte = "Python"
print(texte[0])  # Affiche : P
print(texte[2])  # Affiche : t
print(texte[-1]) # Affiche : n (dernier caractère)

print("-------------------------------------------------------------")

mot = "python"
for lettre in mot:
    print(lettre)

print("-------------------------------------------------------------")

phrase = "Bienvenue en Python"
if "P" in phrase:
    print("La lettre P est présente !")

print("-------------------------------------------------------------")

mot = "programmation"
print(mot.count("m"))  # Affiche : 2

print("-------------------------------------------------------------")
#extraction et recherche

adresse = "10 Rue de la paix, 75001 Paris"
code_postal = adresse[19:24] #extraction du code postal
print(code_postal) # Affiche : 75001

print("-------------------------------------------------------------")

texte = "Extraction de sous-chaîne"
print(texte[:10])# Affiche : Extraction
print(texte[14:])# Affiche : de sous-chaîne

print("-------------------------------------------------------------")

adresse = "10 Rue de la paix, 75001 Paris"
pos_code = adresse.find("75001") #trouver la position du code postal 
code_postal = adresse[pos_code:pos_code + 5]

print(code_postal) # Affiche : 75001

print("-------------------------------------------------------------")

chemin = "/home/user/document.txt"
nom_fichier = chemin.split("/")[-1] #extraction du nom de fichier
print(nom_fichier) # Affiche : document.txt

print("-------------------------------------------------------------")
nom_complet = "Alice Dupont"
prenom = nom_complet.split()[0] #extraction du prénom
print(prenom) # Affiche : Alice

print("-------------------------------------------------------------")

phrase = "Bienvenue sur notre site web."
if "site" in phrase:
    print("Le mot 'site' est présent !")#affiché

print("-------------------------------------------------------------")

message = "Votre commande #12345 a été expédiée."
pos = message.find("#12345") #trouver la position du #
print(pos) # Affiche : 16

print("-------------------------------------------------------------")

texte = "Python est un langage. Python est utilisé partout."
print(texte.count("Python")) # Affiche : 2

print("-------------------------------------------------------------")

email = "Gagnez 1000€ immédiatement ! Cliquez ici ! pour offre exclusive."
if "1000€" in email or "offre exclusive" in email:
    print("Spam détecté !") #affiché

print("-------------------------------------------------------------")

description = "cet ordinateur est rapide et performant."
mots_cles = ["rapide", "performant", "puissant"]
for mot in mots_cles:
    if mot in description:
        print(f"Le mot-clé détecté : {mot}") #affiché

print("-------------------------------------------------------------")

message = "Référence du ticket : #T12345"
pos = message.find("#T")
ticket = message[pos:] if pos != -1 else "Aucun ticket trouvé"
print(ticket) # Affiche : #T12345

print("-------------------------------------------------------------")

nom_client = "jean dupont"
nom_client = nom_client.upper()  # Conversion en majuscules
print(nom_client)

print("-------------------------------------------------------------")

e-mail_utilisateur = "Contact@Entreprise.com"
#e-mail_normalise = e-mail_utilisateur.lower()  # Conversion en minuscules
#if e-mail_utilisateur : "lettres majuscules:"  
#print(e-mail_normalise)
 
print("-------------------------------------------------------------")

titre = "introduction à la programmation"
titre = titre.capitalize()
print(titre)

print("-------------------------------------------------------------")

titre = "introduction à la programmation"
titre = titre.title()
print(titre)

print("-------------------------------------------------------------")

Nom = "durand"
Code_postal = "7500"
Téléphone = "06 12 34 56 78"
email = "   jean.durand@gmail.com"

Nom = Nom.upper()

Code_postal = Code_postal.strip().zfill(5)

Téléphone = Téléphone.replace(" ", "")

email = email.strip()

print("Nom :", Nom)
print("Code postal :", Code_postal)
print("Téléphone :", Téléphone)
print("Email :", email)

print("-------------------------------------------------------------")

texte = "Bonjour tout le monde. Bonne journée tout le monde."
nouveau_texte = texte.replace("monde", "groupe")
print(nouveau_texte)

print("-------------------------------------------------------------")

numero = "06 12-34 56 78"
numero = numero.replace(" ", "").replace("-", "")
print(numero)

print("-------------------------------------------------------------")

numero = "06 12-34 56 78"
numero = numero.replace(" ", "").replace("-", "")
print(numero)

print("-------------------------------------------------------------")

e-mail = "   contact@exemple.com   "
#e-mail = e-mail.strip()
#print(e-mail)

print("-------------------------------------------------------------")

texte = "   Bonjour"
print(texte.lstrip())  # Supprime uniquement à gauche 
texte = "Bonjour   "
print(texte.rstrip())  # Supprime uniquement à drote

print("-------------------------------------------------------------")

phrase = "Bonjour    tout   le    monde"
phrase = " ".join(phrase.split())  # Séparation en mots et réassemblage
print(phrase)

print("-------------------------------------------------------------")

#import re
#def valider_e-mail(e-mail):
#pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#return re.match(pattern, e-mail) is not None

# Test
#print(valider_e-mail("contact@entreprise.com"))  # True
#print(valider_e-mail("contact@entreprise"))      # False

print("-------------------------------------------------------------")

def valider_numero(numero):
    pattern = r"^0[67]\d{8}$"
    return re.match(pattern, numero) is not None

print(valider_numero("0612345678"))  # True
print(valider_numero("0812345678"))  # False

print("-------------------------------------------------------------")

def valider_code_postal(cp):
    return cp.isdigit() and len(cp) == 5

print(valider_code_postal("75001"))  # True
print(valider_code_postal("ABC12"))  # False

print("-------------------------------------------------------------")

def valider_code_postal(cp):
    return cp.isdigit() and len(cp) == 5

print(valider_code_postal("75001"))  # True
print(valider_code_postal("ABC12"))  # False

print("-------------------------------------------------------------")

def generer_message(nom, produit):
    message = f"Bonjour {nom},\n\nMerci pour votre achat ! Votre commande pour '{produit}' a bien été enregistrée.\n\nCordialement,\nL'équipe e-commerce"
    return message
print(generer_message("Jean Dupont", "Ordinateur Portable"))

print("-------------------------------------------------------------")

with open("data.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)

print("-------------------------------------------------------------")

with open("clients.csv", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        infos = ligne.strip().split(";")
        print(f"Client: {infos[0]}, E-mail: {infos[1]}")

print("-------------------------------------------------------------")

import re

def generer_identifiant(nom, code_postal):
    nom = nom.replace(" ", "").upper()
    return f"{nom[:5]}-{code_postal}"

def valider_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def generer_confirmation(nom, email, code_postal):
    if not valider_email(email):
        return "Erreur : Email invalide."
    
    identifiant = generer_identifiant(nom, code_postal)
    message = f"Bonjour {nom},\n\nVotre réservation a été confirmée !\nIdentifiant : {identifiant}\n\nCordialement,\nHôtel Parisien"
    return message

# Test
print(generer_confirmation("Jean Dupont", "jean.dupont@mail.com", "75001"))

print("-------------------------------------------------------------")

# Mauvais exemple
#sql = "SELECT * FROM users WHERE name = '" + user_input + "'"

#🔹 Correction sécurisée
# Utilisation de requêtes paramétrées
#cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))

print("-------------------------------------------------------------")























