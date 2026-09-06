#--- MODULE DE VALIDATION DES DONNÉES (EXPRESSIONS RÉGULIÈRES)
import re

#1. constantes (Patterns Regex)
PATTERN_EMAIL = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
PATTERN_TELEPHONE = r"^0[67]\d{8}$"

#2. Fonctions de validation métier
def valider_format_email(email):
    """
    Valide formellement une adresse email selon la norme métier.
    Assainit la chaîne avant validation (espaces supprimés, minuscules).
    """
#Nettoyage préalable (Data Sanitization)
    email_propre = email.strip().lower()

#validation stricte via Regex[cite: 2]
    return re.match(PATTERN_EMAIL, email_propre) is not None
def valider_format_telephone(numero):
    """
    Valide les numéros de téléphone mobile français (06/07).
    Supprime les séparateurs visuels avant analyse.
    """

#Suppression des séparateurs (espaces et tirets) [cite: 2]
    numero_propre = numero.replace(" ", "").replace("-", "")
    return re.match(PATTERN_TELEPHONE, numero_propre) is not None

#3. Exécution et Tests (Uniquement à des fins de validation locale)
email_test = " Contact@Entreprise.com "
tel_test = "06-12-34-56-78"

print("--- RÉSULTATS DE VALIDATION ---")
print(f"Email '{email_test}' valide : {valider_format_email(email_test)}")
print(f"Téléphone '{tel_test}' valide : {valider_format_telephone(tel_test)}")




