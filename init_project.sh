#!/bin/bash
# Automação da arborescência do projeto web (Questão 1)
mkdir -p app/assets app/src/vendor log
touch app/assets/style.css app/assets/index.js
echo "Arborescence de l'application initialisée avec succès."
ls -R .