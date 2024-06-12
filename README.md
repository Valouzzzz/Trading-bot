# Trading Bot

Ce projet est un bot de trading automatisé qui utilise des indicateurs techniques, à savoir la Moyenne Mobile Exponentielle (EMA) et la Moyenne Mobile Simple (SMA), pour prendre des décisions de trading. Le bot est codé en Python et utilise les bibliothèques `yfinance`, `pandas`, `ta`, et `datetime`.


## Fonctionnalités

- **Récupération des données financières** : Utilisation de `yfinance` pour obtenir les données historiques du prix de action CAL.L (peut etre changer a la ligne 7).
- **Calcul des indicateurs techniques** : Utilisation des bibliothèques `pandas`, et `ta` pour calculer les EMA et SMA.
- **Génération de signaux de trading** : Création de signaux d'achat et de vente basés sur les croisements des EMA et SMA.
- **Enregistrement des donnes** : Les donnes sont enregistrer dans le fichier bot1_{date}.csv
- **Exécution des trades** : Mise en œuvre de la logique de trading basée sur les signaux générés.


## Objectifs 

- **Amelioration** : rajouter de meilleur signaux pour le rendre plus fiable.
- **Fonctionnelle** : Créer une version fonctionnelle avec du vrai argent.


## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques suivantes :

```bash
pip install yfinance pandas ta datetime
```
