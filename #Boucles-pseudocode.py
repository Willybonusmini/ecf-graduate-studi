#Boucles-pseudocode

boucle POUR
POUR i DE 1 A 5 FAIRE
	AFFICHER i
FIN POUR

Print("--------------------------------------------------------------------")

boucle POUR
Déclarer Nombre comme Entier
Lire Nombre
 
POUR i DE 1 A Nombre FAIRE
	AFFICHER i
FIN POUR

print("----------------------------------------------------------------")

la boucle TANT QUE.
Déclarer Destination comme Chaine de caractères
Déclarer VilleActuelle comme Chaine de caractères
 
Destination <- ‘Paris’
VilleActuelle <- ‘Marseille’
 
TANT QUE VilleActuelle != Destination FAIRE
Écrire "Non, pas encore"
    	
// Simuler un changement de ville à chaque itération (par exemple)
// Ici, la ville actuelle se rapproche progressivement de la destination
SI VilleActuelle = ‘Marseille’ ALORS
VilleActuelle <- ‘Lyon’
SINON SI VilleActuelle = ‘Lyon’ ALORS
VilleActuelle <- ‘Dijon’
SINON SI VilleActuelle = ‘Dijon’ ALORS
VilleActuelle <- ‘Paris’
FIN SI
FINTANTQUE
 
Écrire "Oui, vous êtes arrivé à Paris !"

print("---------------------------------------------------------------")

La boucle POUR CHAQUE
Déclarer listeInvités comme tableau de chaînes
Déclarer invité comme chaîne
 
// Liste des invités
listeInvités <- ["Alice", "Bob", "Charlie", "David"]
 
POUR chaque invité DANS listeInvités FAIRE
message <- "Bonjour " + invité + ", vous êtes invité à notre événement !"
Écrire message
FIN POUR

print("----------------------------------------------------------------")








