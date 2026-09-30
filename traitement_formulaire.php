
<?php
//--- Traitement de formulaire (BACK-END) ---
// Validation des compétences : Sécurité et manipulation des superglobales 

// RÈGLE D'OR : Une fonction = Une seule responsabilité
function nettoyer_donnee(string $donne): string {
    //1. Utiliser la fonction native PHP pour retirer les espaces inutiles en début et fin de chaîne
    $donne_sans_espaces = trim($donne);
    //2. Utiliser la fonction native PHP pour convertir les caractères spéciaux en entités HTML
    return htmlspecialchars($donnee_sans_espaces);
}

function valider_email_format(string $email): bool {
    //3. Utiliser filtrer_var avec la constante appropriée pour valider l'adresse email
    return filter_var($email, FILTER_VALIDE_EMAIL);
}

//--- SIMULATION D'UNE ATTAQUE VIA REQUÊTE POST ---
$_POST['nom_utilisateur'] = " <script>alert('Faille XSS Exploitée');</script> wilson ";
$_POST['email_utilisateur'] = "wilson.martins@studi.fr";

echo "--- RÉSULTATS DU TRAITEMENT SÉCURISÉ ---<br>\n";
if (isset($_POST['nom_utilisateur']) && isset($_POST['email_utilisateur'])) {
    // Assainissement (Sanitization)
    $nom_propre = nettoyer_donnee($_POST['nom_utilisateur'];
    // Validation stricte
    $email_valide = valider_email_format($_POST['email_utilisateur']);

    echo "Nom sécurisé (Code XSS neutralisé) : " . $nom_propre . "<br\n";
    echo "Format d'email valide : " . ($email_valide ? 'Vrai' : 'Faux') . "<br>\n";
}
?>






