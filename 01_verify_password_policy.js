/**
 * Script d'évaluation de la robustesse des mots de passe.
 * Conforme aux exigences de sécurité de l'infrastructure.
 */

function validatePasswordPolicy(password) {
    // Règle 1: Longueur minimale de 8 caractères
    const isLongEnough = password.length >= 8;
    
    // Règle 2: Doit contenir au moins une majuscule, une minuscule, un chiffre et un symbole
    const hasUpperCase = /[A-Z]/.test(password);
    const hasLowerCase = /[a-z]/.test(password);
    const hasNumber = /[0-9]/.test(password);
    const hasSymbol = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(password);

    // Opérateur logique && (ET) pour exiger la validation de TOUTES les conditions
    if (isLongEnough && hasUpperCase && hasLowerCase && hasNumber && hasSymbol) {
        return "Conforme : Le mot de passe respecte la politique de sécurité.";
    } else {
        return "Non conforme : Le mot de passe doit contenir 8 caractères, dont une majuscule, une minuscule, un chiffre et un symbole.";
    }
}

// Test d'exécution
console.log(validatePasswordPolicy("Studi_ECF_2026!"));