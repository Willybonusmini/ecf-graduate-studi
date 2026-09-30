

#les operations arithmetiques


#Début

prix_heure <- 50 
heures_travail <- 8

total_ht <- prix_heure * heures_travail
Tva <-total_ht * 0.2

total_ttc <- total_ht + Tva

Afficher ("Le total_ht est : "), total_ht
Afficher ("La tva est : ",) Tva 
Afficher ("Le total_ttc est : "), total_ttc

#Fin

print("-------------------------------------------------------------")

#utiliser les opérateurs de comparaison

Début 

    age_utilisateur <- 17
    age_utilisateur2 <- 17

    si age_utilisateur = age_utilisateur2 alors
        Afficher "vous avez le même âge"
    sinon
        Afficher "vous n'avez pas le même âge"

    fin Si 
fin