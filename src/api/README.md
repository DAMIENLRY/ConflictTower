# ConflictTower
Lâche ton meilleur "C'est Ciao" à ton ennemi en détruisant sa tour avec tes troupes

## 🎲 Règles du jeu 
Les deux joueurs possèdent un terrain qu'il choisi au début du jeu. il choisi le haut ou le bas de l'arène. Tout le monde choisit 8 cartes afin de les utiliser pour attaquer la tour adversaire. La partie se termine si le temps est écoulé ou par la destruction d'une tour, le joueur dont la tour est toujours debout en ressort vainqueur.

## 🎮 Use cases : classe Arbiter
**Paramétrer son jouer**
- selectTeam(EnumSide side) # sélectionner son terrain : il y a deux côtés (side) sur la zone de jeu.
- launch_game() # permet de démarrer une partie (le jeu est en 1vs1, les deux joueurs doivent lancer cette méthode).
- get_team() # permet de récupérer son équipe

**Gestion du deck**
- generateDeck() # permet au joueur de lui générer son Deck (sa liste de toutes ses cartes).
- set_deck(deck:List[EnumCard]) # permet au joueur de créer son deck
- add_deck_card(EnumCard troop) # permet d'ajouter une carte à son Deck, troop est une carte
- remove_deck_card(EnumCard troop) # permet de retirer une carte de son Deck, troop est une carte
- get_deck() # permet de récupérer son deck
- get_card_slot(self, card: EnumCard) # permet de prendre une carte de son deck

**Gestion de sa main**
- get_hand() # permet de récupérer sa main
- get_hand_slot(slot: int) # permet de recupérer dans sa main, une carte à un slot précis
- 
- card_is_in_hand(self, card: EnumCard) -> bool # permet de vérifier si une carte est dans sa main

**Prendre des informations du jeu**
- get_copper() # permet de récupérer son nombre de cuivre
- get_cost_card() # permet de récupéré le prix d'une carte
- get_my_tower_life() # permet de récupérer la vie de sa tour
- get_enemy_tower_life() # permet de récupérer la vie de la tour énnemie
- get_troops_stats() # permet de récupérer les statistiques des troupes
- get_troops_on_map() # permet de récupérer toutes les troupes présentes sur la carte
- get_allied_troops() # permet de récuépérer toutes les troupes alliées
- get_enemy_troops() # permet de récupérer toutes les troupes ennemies
  
**Intérargir avec le jeu**
- place_card(Int slot, Int x, Int y) # permet de placer une carte depuis son slot "slot" sur le terrain à la position "x" et "y" de SON terrain.
- update() # permet de mettre à jour son joueur

## ✅ Pré-requis
- Python 3
- API ConflictTower
- Editeur de code ou en ligne avec Replit

## ⚙️ Installation 
- Paquets nécessaires
  - Turtle
  - python-dotenv

- Commandes à exécuter
  - python3 conflictTowers.py

## 🧑‍💻 Auteurs
- Développeur Pytactx API : Julien ARNE
- Développeurs ConflictTowers :
  - Damien Leroy
  - Thibaud Lebrasseur
  - Gaëtan Langlois

## ⚖️ License
Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)
