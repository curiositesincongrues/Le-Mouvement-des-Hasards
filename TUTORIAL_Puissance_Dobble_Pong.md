# README — Puissance Dobble Pong

Guide débutant complet pour concevoir, prototyper et monter **Puissance Dobble Pong** sur **Ubuntu + Raspberry Pi**.

---

## Sommaire

- [1. Présentation du projet](#1-présentation-du-projet)
- [2. Objectif du dispositif](#2-objectif-du-dispositif)
- [3. Vue d’ensemble du jeu](#3-vue-densemble-du-jeu)
- [4. Matériel nécessaire](#4-matériel-nécessaire)
- [5. Logiciels à installer sur Ubuntu](#5-logiciels-à-installer-sur-ubuntu)
- [6. Logiciels à installer sur Raspberry Pi](#6-logiciels-à-installer-sur-raspberry-pi)
- [7. Organisation recommandée des fichiers](#7-organisation-recommandée-des-fichiers)
- [8. Câblage des capteurs](#8-câblage-des-capteurs)
- [9. Étape 1 — Préparer Ubuntu](#9-étape-1--préparer-ubuntu)
- [10. Étape 2 — Préparer le Raspberry Pi](#10-étape-2--préparer-le-raspberry-pi)
- [11. Étape 3 — Tester un seul capteur](#11-étape-3--tester-un-seul-capteur)
- [12. Étape 4 — Construire les 3 zones Ping Pong](#12-étape-4--construire-les-3-zones-ping-pong)
- [13. Étape 5 — Construire les 4 colonnes Puissance 4](#13-étape-5--construire-les-4-colonnes-puissance-4)
- [14. Étape 6 — Afficher un symbole à l’écran](#14-étape-6--afficher-un-symbole-à-lécran)
- [15. Étape 7 — Tester le Makey Makey](#15-étape-7--tester-le-makey-makey)
- [16. Étape 8 — Fabriquer les cartes Dobble XXL](#16-étape-8--fabriquer-les-cartes-dobble-xxl)
- [17. Étape 9 — Ajouter les sons](#17-étape-9--ajouter-les-sons)
- [18. Étape 10 — Relier tous les modules](#18-étape-10--relier-tous-les-modules)
- [19. Étape 11 — Ajouter la fin selfie](#19-étape-11--ajouter-la-fin-selfie)
- [20. Ordre de travail conseillé](#20-ordre-de-travail-conseillé)
- [21. Dépannage](#21-dépannage)
- [22. Checklist finale](#22-checklist-finale)
- [23. Planning réaliste pour débutant](#23-planning-réaliste-pour-débutant)

---

## 1. Présentation du projet

**Puissance Dobble Pong** est une installation-jeu hybride.

Le principe général est de faire vivre une chaîne d’actions physiques et symboliques :

**Ping Pong → Action → Puissance 4 → Symbole → Dobble → Effet → Parcours → Selfie**

Le projet mélange :
- impact de balle
- détection par capteur
- interaction physique
- apparition d’un symbole
- réponse tactile avec Makey Makey
- effets sonores ou visuels
- déplacement du corps dans l’espace
- final collectif sous forme de selfie

L’objectif n’est pas de faire un jeu vidéo classique, mais une **expérience collective, légère, physique et immédiate**.

---

## 2. Objectif du dispositif

Le projet doit être :

- **simple à comprendre**
- **rapide à tester**
- **jouable sans longues explications**
- **physique**
- **collectif**
- **modulaire**
- **prototypable par étapes**

En tant que débutant, il ne faut surtout pas essayer de tout réussir d’un coup.

Il faut construire le projet **bloc par bloc** :

1. lire un capteur
2. lire plusieurs capteurs
3. afficher une réaction
4. jouer un son
5. tester le Makey Makey
6. relier tous les blocs
7. construire le décor physique
8. faire la version finale

---

## 3. Vue d’ensemble du jeu

Voici la logique générale recommandée :

1. une balle de ping-pong tombe sur une zone
2. un capteur détecte le choc
3. une action démarre
4. le joueur interagit avec la partie Puissance 4
5. un symbole apparaît
6. le joueur doit répondre via une carte Dobble XXL
7. un effet visuel ou sonore se joue
8. les joueurs avancent dans le parcours
9. le jeu se termine par une image ou un selfie final

---

## 4. Matériel nécessaire

## 4.1 Matériel principal

- 1 Raspberry Pi 4 ou 5
- 1 carte microSD 32 Go minimum
- 1 alimentation adaptée au Raspberry Pi
- 1 écran HDMI
- 1 câble HDMI
- 1 haut-parleur ou petite enceinte
- 1 webcam USB ou caméra Raspberry Pi
- 1 Makey Makey
- 1 ordinateur sous Ubuntu pour préparer le projet

## 4.2 Électronique additionnelle

- 7 capteurs de vibration **SW-420**
- 1 breadboard
- 1 lot de fils Dupont
- 1 lot de câbles crocodiles
- 1 rouleau de ruban conducteur ou d’aluminium
- serre-câbles ou adhésif de fixation

## 4.3 Matériaux de fabrication

- carton plume
- mousse EVA
- carton fort
- bois fin en option
- colle
- scotch solide
- attaches
- renforts
- protection pour le sol
- feutres / impressions / habillage visuel

## 4.4 Matériel conseillé en plus

- multiprise
- rallonges
- double-face fort
- tapis antidérapant
- cutter
- règle métallique
- pistolet à colle
- pinces
- tournevis
- petits serre-joints si structure bois

---

## 5. Logiciels à installer sur Ubuntu

Ubuntu sert à :

- écrire le code
- tester l’interface
- préparer les médias
- vérifier le Makey Makey
- organiser les fichiers du projet

## 5.1 Installation système

Ouvre un terminal et exécute :

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git vlc ffmpeg
```

## 5.2 Créer le dossier de travail

```bash
mkdir -p ~/projets/puissance-dobble-pong
cd ~/projets/puissance-dobble-pong
python3 -m venv .venv
source .venv/bin/activate
```

## 5.3 Installer les bibliothèques Python utiles

```bash
python3 -m pip install --upgrade pip
python3 -m pip install pygame
```

## 5.4 À quoi sert chaque élément

- `python3` : exécuter les scripts
- `pip` : installer des bibliothèques Python
- `venv` : isoler proprement le projet
- `git` : cloner et sauvegarder le travail
- `vlc` : tester audio / vidéo
- `ffmpeg` : convertir ou préparer les médias
- `pygame` : affichage, clavier, audio, boucle du jeu

---

## 6. Logiciels à installer sur Raspberry Pi

Le Raspberry Pi servira à :

- lire les GPIO
- connecter les capteurs
- lancer la version finale du projet

## 6.1 Installation recommandée

Sur le Raspberry Pi :

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-gpiozero
```

## 6.2 Recommandation importante

Le plus simple est :

- **Ubuntu sur ton PC**
- **Raspberry Pi OS sur le Pi**

Cela évite de compliquer inutilement la gestion des GPIO.

---

## 7. Organisation recommandée des fichiers

Tu peux organiser ton projet comme ceci :

```text
puissance-dobble-pong/
├── README.md
├── main.py
├── config.py
├── capteurs.py
├── affichage.py
├── dobble.py
├── selfie.py
├── captures/
├── assets/
│   ├── images/
│   ├── symboles/
│   └── video/
├── sons/
│   ├── metal/
│   ├── concret/
│   ├── pop/
│   ├── enfant/
│   ├── clown/
│   └── calme/
└── tests/
    ├── test_gpio.py
    ├── test_pygame.py
    ├── test_makey.py
    └── test_audio.py
```

---

## 8. Câblage des capteurs

## 8.1 Principe d’un capteur SW-420

Chaque capteur SW-420 se branche ainsi :

```text
VCC -> 3.3V
GND -> GND
DO  -> GPIO
```

## 8.2 Répartition recommandée

### Partie Ping Pong
- zone 1 → GPIO17
- zone 2 → GPIO27
- zone 3 → GPIO22

### Partie Puissance 4
- colonne 1 → GPIO5
- colonne 2 → GPIO6
- colonne 3 → GPIO13
- colonne 4 → GPIO19

## 8.3 Attention

Les vibrations peuvent se propager d’une zone à l’autre.

Donc il faut :
- isoler mécaniquement les surfaces
- éviter une grande planche unique
- renforcer les zones
- tester chaque capteur séparément

---

## 9. Étape 1 — Préparer Ubuntu

## 9.1 Installer les outils

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git vlc ffmpeg
```

## 9.2 Créer le projet

```bash
mkdir -p ~/projets/puissance-dobble-pong
cd ~/projets/puissance-dobble-pong
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install pygame
```

## 9.3 Vérifier Python

```bash
python3 --version
```

## 9.4 Vérifier pygame

```bash
python3 -c "import pygame; print(pygame.ver)"
```

Si cela affiche une version, c’est bon.

---

## 10. Étape 2 — Préparer le Raspberry Pi

## 10.1 Installer le système

Le plus simple est d’utiliser **Raspberry Pi OS**.

## 10.2 Mettre à jour

```bash
sudo apt update
sudo apt upgrade -y
```

## 10.3 Installer les bibliothèques utiles

```bash
sudo apt install -y python3 python3-pip python3-gpiozero
```

## 10.4 Vérifier la bibliothèque GPIO

```bash
python3 -c "from gpiozero import Button; print('GPIO OK')"
```

Si tu vois `GPIO OK`, la base logicielle fonctionne.

---

## 11. Étape 3 — Tester un seul capteur

Ne branche pas tout d’un coup.

Commence par **un seul capteur**.

## 11.1 Script de test simple

Crée `tests/test_gpio.py` :

```python
from gpiozero import Button
from signal import pause

capteur = Button(17)

capteur.when_pressed = lambda: print("Impact détecté sur GPIO17")

print("Tape doucement sur la zone reliée au capteur.")
pause()
```

## 11.2 Lancer le test

```bash
python3 tests/test_gpio.py
```

## 11.3 Résultat attendu

Quand tu tapes ou fais vibrer la zone :
- un message doit apparaître
- le déclenchement doit être lisible
- il ne doit pas se produire tout seul sans raison

## 11.4 Si ça ne marche pas

Vérifie :
- le 3.3V
- la masse GND
- la broche GPIO
- le contact du capteur
- la fixation mécanique

---

## 12. Étape 4 — Construire les 3 zones Ping Pong

Cette partie sert d’entrée physique dans le jeu.

## 12.1 Objectif

Créer 3 zones d’impact distinctes :

- zone 1
- zone 2
- zone 3

## 12.2 Recommandation de construction

Pour chaque zone :

- une petite surface indépendante
- un matériau léger mais pas trop souple
- un capteur SW-420 fixé dessous
- un support suffisamment stable

## 12.3 Matériaux conseillés

- carton plume épais
- mousse EVA
- petite plaque fine rigide
- ruban adhésif solide
- renfort sur les bords

## 12.4 Conseils très importants

- ne fais pas une grande plaque unique
- isole les 3 zones
- teste avec une vraie balle
- évite que la vibration d’une zone déclenche les autres

## 12.5 Test complet de la zone Ping Pong

Crée ou remplace `tests/test_gpio.py` :

```python
from gpiozero import Button
from signal import pause

zones = {
    "ping_1": Button(17),
    "ping_2": Button(27),
    "ping_3": Button(22),
}

for nom, capteur in zones.items():
    capteur.when_pressed = lambda n=nom: print(f"Déclenchement : {n}")

print("Teste les 3 zones Ping Pong.")
pause()
```

---

## 13. Étape 5 — Construire les 4 colonnes Puissance 4

Cette étape correspond à la seconde interaction physique.

## 13.1 Objectif

Créer 4 zones ou colonnes distinctes :

- colonne 1 → GPIO5
- colonne 2 → GPIO6
- colonne 3 → GPIO13
- colonne 4 → GPIO19

## 13.2 Principe

Le joueur ou l’objet provoque une vibration :
- par chute
- par impact
- par contact

Le système doit détecter dans quelle colonne l’action s’est produite.

## 13.3 Construction recommandée

- une colonne = une zone indépendante
- placer le capteur sous ou derrière la zone d’impact
- mettre des renforts
- séparer physiquement chaque colonne

## 13.4 Test complet de tous les capteurs

```python
from gpiozero import Button
from signal import pause

zones = {
    "ping_1": Button(17),
    "ping_2": Button(27),
    "ping_3": Button(22),
    "p4_1": Button(5),
    "p4_2": Button(6),
    "p4_3": Button(13),
    "p4_4": Button(19),
}

for nom, capteur in zones.items():
    capteur.when_pressed = lambda n=nom: print(f"Déclenchement : {n}")

print("Teste toutes les zones.")
pause()
```

## 13.5 But de ce test

Tu dois vérifier :
- que la bonne zone répond
- qu’une autre zone ne répond pas en même temps
- qu’il n’y a pas de faux positifs

---

## 14. Étape 6 — Afficher un symbole à l’écran

Une fois les capteurs fonctionnels, il faut une réaction visible.

Le plus simple est d’afficher un **symbole** ou un **mot** à l’écran.

## 14.1 Liste de symboles simple

Exemple :

- ZEBRE
- POMME
- CLOWN
- CLEF
- SOLEIL
- LUNE
- CHAT
- ARBRE
- TORTUE
- DRAGON
- FLEUR
- ECLAIR

## 14.2 Test pygame de base

Crée `tests/test_pygame.py` :

```python
import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Puissance Dobble Pong - Test symbole")
font = pygame.font.SysFont(None, 96)
clock = pygame.time.Clock()

SYMBOLS = [
    "ZEBRE", "POMME", "CLOWN", "CLEF", "SOLEIL", "LUNE",
    "CHAT", "ARBRE", "TORTUE", "DRAGON", "FLEUR", "ECLAIR"
]

current_symbol = random.choice(SYMBOLS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            current_symbol = random.choice(SYMBOLS)

    screen.fill((20, 20, 20))
    text = font.render(current_symbol, True, (240, 240, 240))
    rect = text.get_rect(center=(640, 360))
    screen.blit(text, rect)

    pygame.display.flip()
    clock.tick(60)
```

## 14.3 Lancer le test

```bash
python3 tests/test_pygame.py
```

## 14.4 Résultat attendu

Quand tu appuies sur une touche :
- le symbole change
- l’écran reste stable
- la fenêtre ne plante pas

---

## 15. Étape 7 — Tester le Makey Makey

Le Makey Makey se comporte comme un clavier USB.

## 15.1 Mapping conseillé

- Carte 1 → flèche haut
- Carte 2 → flèche bas
- Carte 3 → flèche gauche
- Carte 4 → flèche droite
- Carte 5 → espace
- Carte 6 → entrée

## 15.2 Test le plus simple

1. branche le Makey Makey en USB
2. ouvre un éditeur de texte
3. relie une entrée à un objet conducteur
4. touche `EARTH`
5. vérifie qu’une touche est envoyée

## 15.3 Test Python avec pygame

Crée `tests/test_makey.py` :

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Test Makey Makey")
font = pygame.font.SysFont(None, 54)
clock = pygame.time.Clock()

message = "Appuie sur une touche Makey Makey"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            message = f"Touche détectée : {pygame.key.name(event.key)}"

    screen.fill((30, 30, 30))
    text = font.render(message, True, (240, 240, 240))
    rect = text.get_rect(center=(450, 250))
    screen.blit(text, rect)

    pygame.display.flip()
    clock.tick(60)
```

## 15.4 Lancer

```bash
python3 tests/test_makey.py
```

---

## 16. Étape 8 — Fabriquer les cartes Dobble XXL

## 16.1 Objectif

Créer de grandes cartes tactiles reliées au Makey Makey.

## 16.2 Matériel conseillé

- carton plume
- impression du symbole
- aluminium ou ruban conducteur
- câble crocodile
- scotch fort
- adhésif de protection

## 16.3 Méthode simple

1. découper une grande carte
2. coller le visuel du symbole
3. ajouter une partie conductrice
4. relier cette partie à une entrée du Makey Makey
5. tester la conduction
6. protéger la carte

## 16.4 Conseils

- éviter les cartes trop fragiles
- renforcer les bords
- bien fixer les câbles
- protéger les zones conductrices

---

## 17. Étape 9 — Ajouter les sons

Tu peux préparer plusieurs univers sonores :

- métal
- concret
- pop
- enfant
- clown
- calme

## 17.1 Structure audio

```text
sons/
├── metal/
├── concret/
├── pop/
├── enfant/
├── clown/
└── calme/
```

## 17.2 Script de test audio

Crée `tests/test_audio.py` :

```python
import pygame
import random
import os

pygame.init()
pygame.mixer.init()

dossier = "sons/calme"
fichiers = [
    os.path.join(dossier, f)
    for f in os.listdir(dossier)
    if f.endswith(".wav") or f.endswith(".mp3")
]

if fichiers:
    son = random.choice(fichiers)
    print("Lecture :", son)
    pygame.mixer.music.load(son)
    pygame.mixer.music.play()
    input("Appuie sur Entrée pour quitter...")
else:
    print("Aucun son trouvé dans", dossier)
```

## 17.3 Lancer

```bash
python3 tests/test_audio.py
```

---

## 18. Étape 10 — Relier tous les modules

Quand chaque bloc marche séparément, tu peux les relier.

## 18.1 Objectif minimal

- détecter une zone Ping Pong
- attendre une action Puissance 4
- afficher un symbole
- accepter une réponse via Makey Makey
- jouer un son
- passer à la suite

## 18.2 Script principal simple

Crée `main.py` :

```python
import random
import time
from gpiozero import Button

ping = [Button(17), Button(27), Button(22)]
p4 = [Button(5), Button(6), Button(13), Button(19)]

SYMBOLS = [
    "ZEBRE", "POMME", "CLOWN", "CLEF", "SOLEIL", "LUNE",
    "CHAT", "ARBRE", "FLEUR", "DRAGON", "ECLAIR", "TORTUE"
]

def attendre_ping():
    while True:
        for i, zone in enumerate(ping, start=1):
            if zone.is_pressed:
                print(f"Ping pong détecté sur zone {i}")
                time.sleep(0.25)
                return i

def attendre_p4():
    while True:
        for i, col in enumerate(p4, start=1):
            if col.is_pressed:
                print(f"Puissance 4 détecté sur colonne {i}")
                time.sleep(0.25)
                return i

while True:
    print("En attente d'une balle...")
    zone_ping = attendre_ping()

    print("ACTION")
    col_p4 = attendre_p4()

    symbole = random.choice(SYMBOLS)
    print(f"SYMBOLE : {symbole}")
```

## 18.3 Première réussite concrète

Tu peux considérer que ton prototype fonctionne déjà si :

- une balle déclenche une entrée
- une colonne déclenche une seconde action
- un symbole s’affiche ou s’imprime
- le système ne plante pas

C’est déjà une base solide.

---

## 19. Étape 11 — Ajouter la fin selfie

## 19.1 Version la plus simple

Ne commence pas par automatiser la photo.

Commence par :
- afficher un message final
- demander aux joueurs de se regrouper
- prendre la photo manuellement

Exemple :
- afficher `Rassemblez-vous pour le selfie final`

## 19.2 Version automatisée plus tard

Quand le reste fonctionne, tu pourras :
- brancher une webcam
- capturer une image
- enregistrer la photo dans `captures/`

## 19.3 Conseils

- ne fais pas de la partie selfie le point bloquant
- termine d’abord le cœur du jeu
- ajoute la photo seulement après stabilisation

---

## 20. Ordre de travail conseillé

Voici l’ordre recommandé si tu veux vraiment réussir :

### Phase 1 — Préparation
1. installer Ubuntu
2. installer Python et pygame
3. préparer le Raspberry Pi

### Phase 2 — Capteurs
4. tester 1 capteur
5. tester 3 capteurs Ping Pong
6. tester 4 capteurs Puissance 4
7. corriger les vibrations parasites

### Phase 3 — Affichage et audio
8. afficher un symbole
9. jouer un son
10. garder une boucle propre

### Phase 4 — Interaction tactile
11. brancher le Makey Makey
12. tester les touches
13. fabriquer les cartes Dobble XXL

### Phase 5 — Assemblage
14. relier ping-pong + puissance 4 + symbole
15. relier Makey Makey
16. ajouter les effets
17. ajouter le final selfie

### Phase 6 — Installation physique
18. construire le parcours
19. fixer les câbles
20. sécuriser le sol
21. faire tester à de vraies personnes

---

## 21. Dépannage

## 21.1 Le capteur ne détecte rien

Vérifie :
- alimentation 3.3V
- masse GND
- bon GPIO
- fixation du capteur
- script lancé sur le Raspberry Pi

## 21.2 Le capteur détecte tout le temps

- la structure est trop sensible
- le capteur est mal fixé
- les vibrations se propagent trop
- il faut isoler la zone

## 21.3 Plusieurs zones se déclenchent en même temps

- les plaques sont trop proches
- la structure est trop souple
- il manque des renforts
- il faut séparer les zones mécaniquement

## 21.4 pygame ne se lance pas

Vérifie :
- que `pygame` est bien installé
- que ton environnement virtuel est activé
- que Python est bien celui du projet

Commande utile :

```bash
source .venv/bin/activate
python3 -m pip show pygame
```

## 21.5 Le Makey Makey ne répond pas

Vérifie :
- le câble USB
- que tu touches aussi `EARTH`
- que la zone est conductrice
- que l’entrée choisie correspond bien à la touche attendue

## 21.6 Les sons ne se jouent pas

Vérifie :
- que les fichiers existent
- qu’ils sont dans le bon dossier
- que le volume système est activé
- que `pygame.mixer.init()` ne renvoie pas d’erreur

## 21.7 La structure bouge trop

- ajoute des renforts
- fixe au sol
- ajoute un tapis antidérapant
- limite les surfaces flottantes

---

## 22. Checklist finale

## 22.1 Logiciel

- [ ] Ubuntu prêt
- [ ] Python installé
- [ ] environnement virtuel créé
- [ ] pygame installé
- [ ] Raspberry Pi prêt
- [ ] gpiozero installé
- [ ] scripts testés sans erreur

## 22.2 Électronique

- [ ] 7 capteurs branchés
- [ ] chaque GPIO testé
- [ ] pas de faux positifs massifs
- [ ] câblage propre
- [ ] alimentation stable

## 22.3 Construction

- [ ] 3 zones Ping Pong solides
- [ ] 4 colonnes Puissance 4 distinctes
- [ ] structure renforcée
- [ ] cartes Dobble XXL prêtes
- [ ] zones conductrices protégées
- [ ] câbles sécurisés

## 22.4 Expérience utilisateur

- [ ] la balle déclenche bien une action
- [ ] le joueur comprend quoi faire
- [ ] le symbole est lisible
- [ ] le Makey Makey répond
- [ ] le son fonctionne
- [ ] la fin est claire
- [ ] le public peut circuler sans danger

---

## 23. Planning réaliste pour débutant

Voici un planning raisonnable.

## 23.1 Préparation logicielle
- 2 à 4 heures

## 23.2 Tests capteurs
- 4 à 8 heures

## 23.3 Construction Ping Pong
- 4 à 8 heures

## 23.4 Construction Puissance 4
- 6 à 12 heures

## 23.5 Affichage / sons
- 4 à 8 heures

## 23.6 Makey Makey + cartes
- 4 à 8 heures

## 23.7 Assemblage final
- 6 à 12 heures

## 23.8 Installation sur site
- 4 à 8 heures

## Total réaliste
Entre **34 et 68 heures** selon ton niveau, le matériel disponible et les retouches physiques.

---

## Conclusion

La meilleure méthode pour réussir est très simple :

1. tester chaque bloc séparément
2. ne rien assembler trop tôt
3. renforcer la structure physique
4. simplifier au maximum la première version
5. faire un prototype jouable avant de chercher une belle finition

Le vrai secret de réussite ici n’est pas d’écrire beaucoup de code.

C’est de faire un système :
- **stable**
- **lisible**
- **testé étape par étape**
- **physiquement robuste**
- **simple à comprendre pour le public**

---

## Commandes utiles récapitulatives

### Ubuntu

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git vlc ffmpeg
mkdir -p ~/projets/puissance-dobble-pong
cd ~/projets/puissance-dobble-pong
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install pygame
```

### Raspberry Pi

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-gpiozero
```

### Lancer un test

```bash
python3 tests/test_gpio.py
python3 tests/test_pygame.py
python3 tests/test_makey.py
python3 tests/test_audio.py
```

### Lancer le projet

```bash
python3 main.py
```

---

## Version ultra-courte du projet

Le jeu fonctionne si tu arrives à faire ceci :

- une balle touche une zone
- un capteur réagit
- une action démarre
- une colonne de Puissance 4 est détectée
- un symbole apparaît
- une carte Dobble XXL est touchée
- un effet se joue
- les joueurs avancent
- la fin est marquée par un selfie ou une image finale

C’est cette chaîne qu’il faut réussir, dans cet ordre, sans brûler d’étapes.
