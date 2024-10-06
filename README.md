
# Préparation de Données pour un Organisme de Santé Publique

## Contexte

Ce projet vise à aider Santé publique France à améliorer la base de données Open Food Facts. La mission principale est de nettoyer et d'explorer les données pour prédire les valeurs nutritionnelles manquantes et fournir des visualisations utiles. Le projet comprend deux étapes principales : nettoyage des données (`01_nettoyage.ipynb`) et exploration/visualisation des données (`02_exploration.ipynb`).

## Jeu de Données

Le jeu de données utilisé provient de la plateforme [Open Food Facts](https://world.openfoodfacts.org/) et peut être téléchargé [ici](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip). Il contient des informations sur les produits alimentaires, notamment :
- Informations générales : nom, date de modification, etc.
- Catégories : type de produit, origine, pays de distribution, etc.
- Ingrédients et additifs.
- Valeurs nutritionnelles pour 100g de produit.

Les variables du dataset sont documentées [ici](https://world.openfoodfacts.org/data/data-fields.txt).

## Structure du Répertoire

- `data/` : Dossier contenant les fichiers de données, suivis avec Git LFS.
- `.gitattributes` : Configuration pour le suivi des fichiers volumineux avec Git LFS.
- `.gitignore` : Liste des fichiers à ignorer par Git.
- `01_nettoyage.ipynb` : Notebook dédié au nettoyage des données et au traitement des valeurs manquantes.
- `02_exploration.ipynb` : Notebook d'exploration des données, incluant des analyses univariées, bivariées et multivariées.
- `utils.py` : Fonctions utilitaires pour le traitement des données.

## Nettoyage des Données

Le nettoyage des données est réalisé dans `01_nettoyage.ipynb`. Les étapes incluent :
- **Suppression des colonnes avec plus de 50% de valeurs manquantes.**
- **Analyse des colonnes importantes :** Inspection des champs `pnns_groups_1` et `pnns_groups_2` pour déterminer leur utilité.
- **Traitement des doublons et valeurs aberrantes :** Utilisation du code-barre comme identifiant unique et correction des valeurs aberrantes (`energy_100g`).
- **Comblage des valeurs manquantes :** Remplacement des valeurs nulles dans les colonnes nutritionnelles par des estimations calculées ou par KNN Imputation.

Le notebook crée plusieurs versions nettoyées du jeu de données :
- `data_relevant.csv` : Sélection des colonnes pertinentes.
- `data_cleaned_by_calculation.csv` : Valeurs manquantes comblées par calcul direct.
- `data_cleaned_auto.csv` : Jeu de données complet, traité par KNN Imputation.

## Exploration des Données

Le notebook `02_exploration.ipynb` réalise des analyses statistiques et visualisations :
- **Analyse univariée :** Distribution des valeurs des variables nutritionnelles, proportions des `nutrition_grade_fr`.
- **Analyse bivariée :** Étude des relations entre les variables, création de pair plots, et analyse de corrélation entre variables quantitatives et qualitatives.
- **Analyse multivariée :** Analyse en composantes principales (ACP), visualisation des groupes nutritionnels selon leurs caractéristiques.

## Résultats Principaux

Les résultats incluent des visualisations telles que :
- **Boxplots et histogrammes** des valeurs nutritionnelles avant et après nettoyage.
- **Diagrammes en barres et pie charts** pour la distribution des grades nutritionnels (`nutrition_grade_fr`).
- **Analyse des corrélations** entre les nutriments via des matrices de corrélations et ACP.
