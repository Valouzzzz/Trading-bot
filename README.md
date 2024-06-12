# Trading Bot

Ce projet est un bot de trading automatisé qui utilise des indicateurs techniques, à savoir la Moyenne Mobile Exponentielle (EMA) et la Moyenne Mobile Simple (SMA), pour prendre des décisions de trading. Le bot est codé en Python et utilise les bibliothèques `numpy`, `yfinance`, `pandas`, et `ta`.

## Fonctionnalités

- **Récupération des données financières** : Utilisation de `yfinance` pour obtenir les données historiques des prix des actions.
- **Calcul des indicateurs techniques** : Utilisation des bibliothèques `numpy`, `pandas`, et `ta` pour calculer les EMA et SMA.
- **Génération de signaux de trading** : Création de signaux d'achat et de vente basés sur les croisements des EMA et SMA.
- **Exécution des trades** : Mise en œuvre de la logique de trading basée sur les signaux générés.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques suivantes :

```bash
pip install numpy yfinance pandas ta
