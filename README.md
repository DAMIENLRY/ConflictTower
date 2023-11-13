# ⚔️ Plan d'attaque de la conception du jeu
## 2023-11-13 TD
- [x] Comprendre les bonnes pratiques à utiliser pour votre jeu
- [x] Comprendre les interactions entre les end points d'un jeu robotique réseau
- [x] Définir un groupe de 3-4 personnes
- [x] Créer un projet github et partager les droits à toute l'équipe
- [ ] Partir de l'API, définir tous les use cases des utilisateurs joueurs sur un readme
- [ ] Faire une maquette à insérer dans votre readme (figma, paint, powerpoint ...)
- [ ] Lire le champs des possibles de votre arbitre sur tutos.jusdeliens
- [ ] Définir et répartir les tâches dans un kanban (trello ou issues sur github) 
- [ ] Rédiger le diagramme de séquence pour chaque use case
## 2023-11-14 TD
- [ ] Choisir interface/méthodes de votre API en Python
- [ ] Réaliser les tests unitaires et fonctionnels de l'API
- [ ] Noyau du serveur pytactX : définir les responsabilités du jeu et les classes évènements et méthodes associées 

# 📂 Arborescence projet Github
- votrejeu
    - doc
        - *.svg
    - src
        - api
            - j2l           -> *lib jusdeliens à récupérer sur tutos.jusdeliens.com* 
            - votrejeu.py   -> *interface API de votre jeu côté client*
            - readme.md     -> *explique au joueur les actions possibles de l'api*
        - server
            - main.py       -> *logique backend implémentant les règles du jeu*
        - gui
            - ...
    - tests
        - api
            - test_votrejeu.py
        - server
            - test_main.py
        - gui
            - ...
    - readme.md             -> *inclus diagramme de conception du dossier doc*

# 🤔 Vos README.md
## A la racine du projet : pour l'administrateur
- **Titre** du jeu
- **Description** courte du jeu
- **🎯 Contexte & cahier des charges** : développé dans le cadre d'une formation, pour un formateur pour monter en compétence en Python ...
- **🎲 Règles** du jeu : maquette, déroulé d'une partie, conditions de victoire
- **🎮 Use cases**: 
    - pour l'administrateur : expliquer ce que peut/doit faire un administrateur qui souhaite lancer/administrer une arène de jeu avec des apprenants 
    - pour le joueur : renvoyer vers README API
    - pour le joueur : poser une carte dans son camp du côté gauche ou du côté droit
    - pour le joueur : connaître la position de toutes les entités (alliées et ennemies)
    - pour le joueur : bouger chaque carte du camp allié
    - pour le joueur : modifier la portée et la vitesse de chaque troupe de combat
    - pour le joueur : modifier les points de vies et les points d'attaque de chaque carte de combat
    - pour le joueur : choisir les cartes de combat par défaut (ou laisser par défaut : attribution de cartes aléatoire)
    - pour le joueur : accès à toutes les cartes de son inventaire
- **🖧 Architecture matériel** (optionnel, peut être décrit avec le diagramme de séquence) : schéma overview présentant les machines et protocoles (serveurs, clients, broker) avec texte expliquant le choix des technologies 
- **📞 Diagramme de séquence**: expliquer le déroulé d'une partie, les principales étapes à faire dans l'ordre et qui/quoi/comment, les couches s'échangent quelles données pour qui/pour quoi
- **✅ Pré-requis** 
    - matériel et logiciel requis pour executer votre projet, pour l'administrateur 
    - pour les apprenants rediriger vers README API
- **⚙️ Installation** : step by step (commandes à executer par l'administrateur, paquets à installer ...)
- **🧪 Tests**: 
    - définition du plan de test ce qu'on attend quand on fait quoi 
    - step by step pour lancer les tests
- **🛣️ Roadmap**
- **🧑‍💻 Auteur**
- **⚖️ License**

## Dans le dossier API : pour les joueurs
- **Titre** ConflictTower
- **Description** Jeu de course de F1 en vue du dessus.
- **🎲 Règles du jeu** :  Faites la courses et arrivez en premier pour gagner.
- **🎮 Use cases**: actions possibles du joueur via l'API
- **✅ Pré-requis** : matériel et logiciel requis pour executer votre projet
- **⚙️ Installation** : step by step (commandes à executer, paquets à installer ...)
- **🧑‍💻 Auteur** Gaëtan LANGLOIS, Thibaud LEBRASSEUR, Damien LEROY
- **⚖️ License** © Copyright Bagnoles Rapides. Tous droits réservés.
