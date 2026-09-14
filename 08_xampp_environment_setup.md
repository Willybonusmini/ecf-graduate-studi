# Configuration et Exploitation de l'Environnement Local (XAMPP)

## Stack Technologique Locale
L'environnement de développement local est provisionné via la suite XAMPP pour simuler un comportement de serveur de production sous Apache/PHP/MySQL.

## Paramètres et Chemins d'Accès
- **Serveur HTTP :** Apache gérant l'écoute sur le port standard `80` (ou configuration locale).
- **Répertoire Racine (Document Root) :** `C:\xampp\htdocs` (sous Windows).
- **Variables d'Environnement :** Injection des chemins des exécutables `php` et `mysql\bin` dans le `PATH` système pour un accès CLI direct.
- **Administration BDD :** Interface graphique `phpMyAdmin` connectée au SGBD MariaDB.