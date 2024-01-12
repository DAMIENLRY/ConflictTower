# ConflictTower
Jeu de défense de tour en 1vs1, utilisez vos cartes pour se défendre ou attaquer.

## 🎲 Règles du jeu 
Les deux joueurs possèdent un terrain, celui du haut ou du bas de l'arène. Chacun reçoit des cartes et peuvent les utiliser dans le but d'attaquer la tour adversaire. La partie se termine par la destruction d'une tour, le joueur dont la tour est toujours debout en ressort vainqueur.

## 🎮 Use cases
- generateDeck() # permet au joueur de lui générer son Deck (sa liste de toutes ses cartes).
- selectTeam(EnumSide side) # sélectionner son terrain : il y a deux côtés (side) sur la zone de jeu.
- launchGame() # permet de démarrer une partie (le jeu est en 1vs1, les deux joueurs doivent lancer cette méthode).
- getDeck() # permet de récupérer le contenu de son Deck.
- placeCard(Int slot, Int x, Int y) # permet de placer une carte depuis son slot <slot> sur le terrain à la position <x> et <y> de SON terrain.

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