# Infrastructure et Écosystème Cloud

## Fournisseurs et Services Provisionnés
Dans le cadre du déploiement et de la gestion du projet ECF, les services suivants ont été activés via le GitHub Student Developer Pack :

- **IDE & Développement :** Suite JetBrains (IntelliJ Ultimate / PhpStorm) pour un débogage avancé et une intégration Git native.
- **Hébergement & PaaS :** 
  - Heroku (déploiement back-end / base de données).
  - Netlify / GitHub Pages (déploiement front-end statique).
- **IaaS & Cloud Computing :** Accès provisionné sur DigitalOcean et Microsoft Azure pour la scalabilité future de la base de données et des machines virtuelles.
- **Gestion de Version :** Client GitKraken pour la résolution des conflits de fusion (merge conflicts) via interface graphique.

*Note : Les accès et clés API de ces services sont strictement isolés dans des variables d'environnement (`.env`) et ignorés par Git (`.gitignore`).*