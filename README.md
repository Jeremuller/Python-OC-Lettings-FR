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

## Tests et qualité du code

Le projet intègre plusieurs outils destinés à garantir la qualité du code et le bon fonctionnement de l'application. Les commandes ci-dessous sont à exécuter depuis la racine du projet, après activation de l'environnement virtuel :

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`

### Linting

La conformité du code aux règles de style (PEP 8) peut être vérifiée à l'aide de la commande suivante :

- `flake8`

### Tests unitaires

Les tests unitaires sont exécutés avec `pytest` :

- `pytest`

### Couverture de tests

La couverture des tests peut être mesurée avec :

- `pytest --cov`

Ces vérifications sont exécutées automatiquement par la pipeline d'intégration continue à chaque `push` et à chaque ouverture ou mise à jour d'une Pull Request. Les différentes étapes de cette pipeline sont détaillées dans la section suivante.

## Pipeline CI/CD

Le projet intègre une pipeline d'intégration et de déploiement continus (CI/CD) mise en œuvre avec GitHub Actions.

À chaque `push` ou ouverture de Pull Request, la pipeline exécute automatiquement les étapes nécessaires pour vérifier la qualité du code. Lorsqu'une modification est intégrée à la branche `master`, elle poursuit le processus jusqu'à la construction de l'image Docker et au déploiement automatique de l'application sur Render.

### Vue d'ensemble

```text
Push / Pull Request
        │
        ▼
GitHub Actions
        │
        ▼
Job "compile"
        │
        ├── Installation des dépendances
        ├── Analyse statique (flake8)
        └── Tests unitaires + couverture
        │
        └──────────────► Validation réussie
                          │
                          ▼
                 (push sur master uniquement)
                          │
                          ▼
                 Job "containerize"
                          │
                          ├── Build Docker
                          ├── Tag SHA
                          ├── Tag latest
                          └── Push DockerHub
                          │
                          ▼
                    Job "deploy"
                          │
                          ▼
                         Render
```

### Job `compile`

Ce premier job est exécuté à chaque `push` et à chaque Pull Request.

Il réalise les opérations suivantes :

* récupération du dépôt Git ;
* installation de Python 3.10 ;
* installation des dépendances du projet ;
* exécution de l'analyse statique avec `flake8` ;
* exécution des tests unitaires avec `pytest` ;
* vérification d'un seuil minimal de 80 % de couverture de tests.

Le job compile s'exécute dans un environnement GitHub Actions éphémère. À chaque exécution, une nouvelle machine virtuelle est provisionnée, les dépendances du projet sont installées, puis les opérations de linting et de tests sont exécutées. Une fois le job terminé, cet environnement est automatiquement détruit, garantissant des exécutions indépendantes et reproductibles sans impact sur les environnements de développement ou de production.

Pour cette étape, l'application est configurée pour utiliser SQLite afin de disposer d'un environnement de test léger et reproductible.

### Job `containerize`

Ce job est exécuté uniquement lors d'un `push` sur la branche `master`.

Après authentification auprès de DockerHub, il :

* construit l'image Docker de l'application ;
* applique deux tags (`latest` et le SHA du commit) ;
* publie les deux images sur DockerHub.

Cette stratégie permet de disposer à la fois d'une image représentant la dernière version stable et d'une image correspondant exactement à un commit donné.

### Job `deploy`

Une fois l'image publiée, le dernier job déclenche automatiquement le **Deploy Hook** de Render.

Render télécharge alors la dernière image disponible sur DockerHub et redéploie l'application sans intervention manuelle.

### Gestion des secrets

Les informations sensibles utilisées par la pipeline sont stockées dans les **GitHub Actions Secrets**.

Cette approche permet de ne jamais versionner les secrets dans le dépôt Git tout en les rendant accessibles aux différentes étapes de la pipeline.

Les secrets utilisés comprennent notamment :

* `SECRET_KEY`
* `SENTRY_DSN`
* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`
* `RENDER_DEPLOY_HOOK`


Cette architecture permet de garantir qu'aucun déploiement en production n'est réalisé tant que les étapes de validation (linting, tests unitaires et couverture de code) n'ont pas été exécutées avec succès.

## Déploiement sur Render

L’application est déployée automatiquement sur la plateforme **Render**, qui héberge le service web ainsi que la base de données PostgreSQL en environnement de production.

Le déploiement est entièrement automatisé et s’appuie sur la pipeline CI/CD ainsi que sur une architecture conteneurisée via Docker.

### Architecture de déploiement

Le déploiement repose sur le flux suivant :

- GitHub Actions construit et publie une image Docker sur DockerHub
- Render récupère automatiquement cette image via un **Deploy Hook**
- L’application est redéployée sans intervention manuelle

### Service web Render

Le service web Render est configuré pour :

- exécuter un conteneur Docker basé sur l’image publiée sur DockerHub
- exposer l’application via un port dynamique fourni par Render
- exécuter automatiquement le script `start.sh` au démarrage

### Script de démarrage (`start.sh`)

Au lancement du conteneur, le script `start.sh` est exécuté automatiquement.

Il effectue les opérations suivantes :

- application des migrations Django sur la base de données PostgreSQL
- lancement du serveur WSGI via Gunicorn

Ce mécanisme garantit que la base de données est toujours synchronisée avec le schéma de l’application au moment du déploiement.

### Base de données PostgreSQL

En production, l’application utilise une base de données PostgreSQL managée par Render. Les informations de connexion sont fournies via des variables d’environnement injectées directement dans le service Render. Ces variables ne sont jamais versionnées dans le dépôt Git.

### Variables d’environnement

Render gère la configuration de l’application via des variables d’environnement définies dans son interface.

Elles permettent notamment de :

- Configurer la connexion à la base de données PostgreSQL
- Activer ou désactiver le mode debug
- Fournir les clés de services externes (Sentry, etc.)

### Healthcheck

Render effectue un **healthcheck HTTP** sur l’application afin de vérifier que le service répond correctement après déploiement.

Ce mécanisme permet de s’assurer que :

- le conteneur démarre correctement
- le serveur Gunicorn est opérationnel
- l’application est accessible avant d’exposer le service

En cas d’échec du healthcheck, le déploiement est considéré comme non valide.

### Déclenchement du déploiement

Le déploiement est automatiquement déclenché lorsqu’un commit (ou une pull request) est validé(e) sur la branche principale (master).

Le job deploy de la pipeline CI/CD envoie une requête HTTP au Deploy Hook Render, ce qui provoque :

- La récupération de la dernière image Docker
- Le redémarrage du service
- Exécution automatique du healthcheck
- La mise en production immédiate des modifications si le healthcheck est un succès

Une fois le déploiement terminé, l’application est accessible publiquement via l’URL fournie par Render.

## Autres commandes utiles

### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## Liens utiles

Les documentations officielles suivantes permettent d'approfondir les technologies utilisées dans ce projet :

- GitHub : https://docs.github.com/fr
- Docker : https://docs.docker.com/
- GitHub Actions : https://docs.github.com/fr/actions
- Render : https://render.com/docs

## Documentation complète

La documentation technique du projet est générée avec **Sphinx** et publiée via **Read the Docs**.

Elle est accessible ici :  
👉 

## Auteur

Jérémy Muller, étudiant en développement applicatif python chez OpenClassrooms.

GitHub : https://github.com/Jeremuller/
