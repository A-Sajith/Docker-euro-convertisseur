# Euro Convertisseur

Application Python containerisée avec Docker qui convertit un montant en euros vers différentes devises en temps réel.

## Pourquoi ce projet ?

Ce projet a été réalisé dans le but de mettre en pratique l’utilisation de Docker sur une application simple.
L’objectif est de comprendre comment containeriser une application, gérer ses dépendances et faciliter son exécution sur différents environnements.

Le choix d’un convertisseur d’euros permet de manipuler des appels à une API externe, de traiter des données JSON et de construire une application concrète tout en restant simple.

## Technologies utilisées

- Python 3.11
- Docker
- API ExchangeRate (https://exchangerate-api.com)

## Fonctionnement

1. L'utilisateur entre un montant en euros
2. L'application appelle l'API ExchangeRate en temps réel
3. Le résultat est affiché en USD, INR et JPY

## Lancer le projet avec Docker

### 1. Cloner le repo
git clone https://github.com/A-Sajith/Docker-euro-convertisseur
cd Docker-euro-convertisseur

### 2. Builder l'image
docker build -t Docker-euro-convertisseur .

### 3. Lancer le container
docker run -it Docker-euro-convertisseur

## Structure du projet

Docker-euro-convertisseur/
├── convertisseur.py   # Code principal
└── Dockerfile         # Configuration Docker

## Ce que j'ai appris

- Appeler une API REST avec Python
- Parser une réponse JSON
- Dockeriser une application Python
- Différence entre docker build et docker run
- Utilisation du flag -it pour les apps interactives
