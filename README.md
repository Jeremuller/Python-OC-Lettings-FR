# Orange County Lettings 

## Présentation du projet 

Orange County Lettings est une application web développée avec Django pour une start-up spécialisée dans la location de biens immobiliers aux États-Unis. 

Dans un contexte de croissance de son activité, l'entreprise souhaite faire évoluer son application afin d'améliorer sa maintenabilité, sa fiabilité et son processus de déploiement. L'application était initialement organisée sous la forme d'un monolithe. 

Dans le cadre de son évolution, elle a été restructurée afin de séparer les fonctionnalités métier en applications Django indépendantes (lettings et profiles). Le module oc_lettings_site conserve désormais les responsabilités de configuration globale du projet (paramétrage, routage principal, serveur WSGI et ressources communes). 

Ce projet met l'accent sur l'industrialisation d'une application Django. L'infrastructure a été modernisée afin d'intégrer une chaîne complète d'intégration et de déploiement continus (CI/CD), comprenant la conteneurisation avec Docker, l'automatisation des tests et des déploiements avec GitHub Actions, la publication des images sur DockerHub et un déploiement automatisé sur Render avec une base de données PostgreSQL en production. 

Cette documentation présente l'architecture de l'application, les technologies employées, les procédures d'installation, ainsi que les étapes de déploiement et de maintenance du projet.

## Fonctionnalités 

L’application vise à fournir une interface simple de consultation de contenus immobiliers, structurée autour de deux modules principaux : les annonces et les profils utilisateurs. 

### Consultation des annonces immobilières 
- Affichage de la liste des annonces disponibles (lettings) 
- Consultation du détail d’une annonce (adresse complète et informations associées) 

### Gestion des profils utilisateurs 
- Affichage de la liste des profils utilisateurs 
- Consultation du détail d’un profil (nom d’utilisateur et informations associées) 

### Page d’accueil 
- Page d’entrée de l’application présentant une navigation vers les principales sections 

### Interface d’administration 
- Accès à l’interface d’administration Django 
- Gestion des données (profils et annonces) via l’admin intégré

## Architecture globale 

L’application Orange County Lettings repose sur une architecture Django modulaire organisée autour de plusieurs composants indépendants. 

### Architecture applicative Django Le projet est structuré en trois éléments principaux : 
- oc_lettings_site : projet Django principal contenant la configuration globale (settings, urls, wsgi) ainsi que les ressources communes. 
- lettings : application métier dédiée à la gestion des annonces immobilières. 
- profiles : application métier dédiée à la gestion des profils utilisateurs. 

Cette séparation permet une meilleure modularité et une évolution indépendante des fonctionnalités. 

### Architecture de déploiement L’application est conçue pour fonctionner dans un environnement conteneurisé et automatisé : 
- L’application est exécutée dans un conteneur Docker. 
- L’image Docker est construite et versionnée via une pipeline CI/CD. 
- Les images sont stockées sur DockerHub. 
- Le déploiement est automatisé sur la plateforme Render. 

### Base de données 
L'application s'appuie sur une stratégie de gestion des données adaptée aux différents environnements d'exécution (développement, intégration continue et production). Cette approche permet de concilier simplicité d'utilisation, reproductibilité des environnements et cohérence avec la production.

La configuration de la base de données est gérée via des variables d’environnement, permettant d’adapter automatiquement le comportement de l’application selon le contexte d’exécution.

Les technologies employées et leur répartition sont détaillées dans la section Stack technique.

### Vue d’ensemble du flux applicatif 
Code source → GitHub Actions → Docker Image → DockerHub → Render → Application déployée avec PostgreSQL

## Stack technique 

### Langage et framework principal 
- Python 3.10 : langage principal du projet 
- Django 3.0 : framework web utilisé pour structurer l’application selon une architecture MVC 

### Base de données 
- SQLite : utilisé pour les tests et scénarios de démarrage rapide 
- PostgreSQL : utilisé en développement (Docker Compose) et en production (Render) 

### Conteneurisation 
- Docker : containerisation de l’application 
- Docker Compose : orchestration des services en environnement de développement 
- DockerHub : registre d’images Docker 

### CI/CD 
- GitHub Actions : pipeline d’intégration et de déploiement continus 
- Automatisation des étapes de test, linting, build et déploiement 

### Qualité de code et tests 
- pytest / pytest-django : tests unitaires de l’application Django 
- coverage : mesure de la couverture de tests 
- flake8 : analyse statique du code (PEP8) 
- black : formattage automatique du code 

### Monitoring 
- sentry-sdk : monitoring des erreurs en production 

### Production 
- Render : plateforme d’hébergement et de déploiement automatisé 
- Gunicorn : serveur WSGI utilisé pour l’exécution de l’application en environnement de production 
- whitenoise : gestion des fichiers statiques en production 


### Variables d’environnement 
- python-dotenv : gestion des variables d’environnement en développement

## Usage local 

### Prérequis 

Avant de lancer l'application, assurez-vous que les outils suivants sont installés sur votre machine : 
- Compte GitHub avec accès en lecture à ce repository 
- Git CLI pour cloner le dépôt et gérer le code source. 
- Interpréteur Python (version 3.10 recomandée pour des raisons de compatibilité) uniquement si vous souhaitez exécuter l'application hors conteneur ou contribuer au développement. 
- Docker (incluant Docker Compose) : pour exécuter l'application dans un environnement conteneurisé. 

Dans le reste de la documentation sur le développement local, il est supposé que la commande python de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé). 

### Cloner le repository 

- `cd /path/to/put/project/in `
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

### Créer l'environnement virtuel 

Pour le développement local, il est recommandé d'utiliser un environnement virtuel Python : 
- `cd /path/to/Python-OC-Lettings-FR `
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu) 
- Activer l'environnement: Linux / macOS: `source venv/bin/activate` ou `.\venv\Scripts\Activate.ps` pour Windows (PowerShell) 
- Confirmer que la commande python exécute l'interpréteur Python dans l'environnement virtuel `which python `
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version `
- Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel, `which pip `
- Pour désactiver l'environnement, `deactivate `

Les sections suivantes présentent les différentes méthodes d'exécution de l'application, selon que vous souhaitiez simplement la découvrir ou contribuer à son développement. 

### Exécuter le site (quick start) 
- `cd /path/to/Python-OC-Lettings-FR `
- `source venv/bin/activate `
- `pip install --requirement requirements.txt `
- `python manage.py runserver `
- Aller sur http://localhost:8000 dans un navigateur. 
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

### Développement avec Docker Compose

Pour reproduire un environnement proche de la production, le projet fournit une configuration Docker Compose permettant d'exécuter simultanément l'application Django et une base de données PostgreSQL.

### Configuration

Avant le premier lancement, créez un fichier `.env` à la racine du projet.

Ce fichier contient les variables d'environnement nécessaires à la configuration de l'application et de la base de données. Pour des raisons de sécurité, il n'est pas versionné dans le dépôt Git.

Les variables suivantes sont notamment requises :

* `DEBUG`=False
* `USE_SQLITE`=False
* `POSTGRES_DB`=oc_lettings
* `POSTGRES_USER`=oc_user
* `POSTGRES_HOST`=db
* `POSTGRES_PORT`=5432

Les variables suivantes contiennent des informations sensibles. Leurs valeurs ne sont pas versionnées dans le dépôt Git et doivent être fournies séparément.

* `SECRET_KEY`
* `POSTGRES_PASSWORD`
* `SENTRY_DSN`

### Démarrage de l'environnement

Une fois le fichier `.env` créé, démarrez les services à l'aide de Docker Compose :


docker compose up --build

Au démarrage, le conteneur de l'application applique automatiquement les migrations de la base de données avant de lancer le serveur Gunicorn.

L'application est ensuite accessible à l'adresse :

http://localhost:8000

Les services sont exécutés au premier plan. Pour arrêter l'environnement, utilisez Ctrl + C ou lancez Docker Compose en mode détaché avec docker compose up -d.

### Données de démonstration

L'environnement de développement démarre avec une base PostgreSQL vide.

Si vous souhaitez disposer d'un jeu de données d'exemple, les fixtures fournies avec le projet peuvent être chargées à l'aide de la commande `loaddata`. Cette procédure est décrite dans la documentation technique.

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
