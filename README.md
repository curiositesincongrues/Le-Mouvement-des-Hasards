# 🟢 Puissance Dobble Pong

## 🎭 Introduction

Nous aimons les jeux hybrides.

Comme dans le chess boxing, ce moment où deux mondes se rencontrent et créent un espace inattendu.  
Ici, nous prenons des jeux simples, connus de tous, et nous les déplaçons légèrement.

Pas pour les améliorer.  
Pas pour les compliquer.  
Mais pour les rendre disponibles autrement.

Puissance Dobble Pong est un jeu qui ne demande rien :  
ni règles, ni expérience, ni performance.  

Seulement d’entrer dedans.

---

## 🌿 Cheminement

Une balle tombe.  
Un capteur écoute.  
Un signe apparaît.  
Un geste répond.  
Un objet chute.  
Une résonance naît.  
Un symbole circule.  
Un corps se déplace.  
Un contact valide.  
Et le jeu continue.

---

## 🧠 Intention

Créer une expérience :

- accessible immédiatement  
- collective  
- physique  
- légère  
- éphémère  

Un jeu qui se découvre sans explication,  
et qui se retient comme un souvenir.

---

## 🏗️ Architecture

```text
PING PONG → ACTION → PUISSANCE 4 → SYMBOLE → DOBBLE → EFFET → PARCOURS → SELFIE
```

---

# 🧰 MATÉRIEL

## Base complète

| Élément | Quantité | Budget |
|---|---:|---:|
| Raspberry Pi 4/5 | 1 | 70–100€ |
| Carte microSD 32 Go | 1 | 8–12€ |
| Alimentation Pi | 1 | 10–15€ |
| Écran HDMI | 1 | 50–100€ |
| Enceinte / haut-parleur | 1 | 15–30€ |
| Webcam / caméra Pi | 1 | 20–40€ |
| Makey Makey | 1 | 50–70€ |

## Électronique additionnelle

| Élément | Quantité | Budget |
|---|---:|---:|
| Capteurs vibration SW-420 | 7 | 10–20€ |
| Breadboard | 1 | 5–8€ |
| Fils Dupont | 1 pack | 8–12€ |
| Câbles crocodiles | 1 pack | 8–12€ |
| Ruban conducteur / aluminium | 1 | 5–15€ |

## Construction

| Élément | Budget |
|---|---:|
| Carton plume / mousse EVA | 10–30€ |
| Bois fin (optionnel) | 20–50€ |
| Colle / scotch / attaches | 10–20€ |
| Protection sol / renforts | 10–30€ |

## Budget total

### Version complète
**300€ à 500€**

### Version complémentaire si tu as déjà :
- Raspberry Pi
- Makey Makey
- cartes Dobble XXL
- webcam
- écran
- enceinte

| Élément manquant | Budget |
|---|---:|
| 7 capteurs SW-420 | 10–20€ |
| breadboard + fils | 13–20€ |
| crocodiles + aluminium | 13–27€ |
| matériaux / fixation | 10–30€ |

**Budget complémentaire réaliste : 46€ à 97€**  
**Version très serrée / prototype : 30€ à 75€**

---

# 🔌 CÂBLAGE

## Ping pong

| Zone | GPIO |
|---|---|
| 1 | GPIO17 |
| 2 | GPIO27 |
| 3 | GPIO22 |

## Puissance 4

| Colonne | GPIO |
|---|---|
| 1 | GPIO5 |
| 2 | GPIO6 |
| 3 | GPIO13 |
| 4 | GPIO19 |

## Capteur SW-420

```text
VCC → 3.3V
GND → GND
DO  → GPIO
```

## Makey Makey / Dobble XXL

| Carte | Touche |
|---|---|
| Carte 1 | flèche haut |
| Carte 2 | flèche bas |
| Carte 3 | flèche gauche |
| Carte 4 | flèche droite |
| Carte 5 | espace |
| Carte 6 | entrée |

---

## 🟡 Symboles -> Enigmes sonores

1. **Zèbre** — Rayures noir blanc
2. **Pomme** — Fruit rond croquant
3. **Bonhomme** — Tête bras jambes
4. **Goutte d’eau** — Tombe fait ploc
5. **Clown** — Nez rouge rigolo
6. **Ampoule** — Éclaire idée lumière
7. **Fromage** — Jaune sent fort
8. **Clef** — Ouvre porte serrure
9. **Dauphin** — Nage saute mer
10. **Biberon** — Bébé boit lait
11. **Cadenas** — Ferme avec clé
12. **Araignée** — Huit pattes tisse
13. **Coccinelle** — Rouge points noirs
14. **Toile d’araignée** — Filet fin collant
15. **Dinosaure** — Géant ancien rugit
16. **Soleil** — Brille chauffe ciel
17. **Cœur** — Bat dans poitrine
18. **Sens interdit** — Stop passage interdit
19. **Cactus** — Plante verte piquante
20. **Point d’interrogation** — Signe pour question
21. **Lune** — Brille pendant nuit
22. **Flocon** — Froid blanc léger
23. **Horloge** — Tic tac heure
24. **Fleur** — Pétales tige parfum
25. **Yin et yang** — Noir blanc équilibre
26. **Dobble** — Logo du jeu
27. **Fantôme** — Blanc flotte peur
28. **Bouche** — Parle mange souffle
29. **Chien jaune** — Aboie queue remue
30. **Crayon** — Écrit dessine papier
31. **Clef de sol** — Signe note musique
32. **Cible** — Rond viser centre
33. **Tête de mort** — Crâne danger pirate
34. **Bombe** — Boum mèche danger
35. **ART / Oiseau** — Oiseau vole chante
36. **Flamme** — Feu chaud danse
37. **Igloo** — Maison glace ronde
38. **Chat** — Miaule moustaches griffes
39. **Peinture verte** — Tache verte peinture
40. **Voiture** — Roule fait vroum
41. **Marteau orange** — Tape clou fort
42. **Trèfle à 4 feuille** — Porte bonheur vert
43. **Carotte** — Orange lapin croque
44. **Lunette de soleil** — Protège yeux soleil
45. **Ciseaux** — Coupent papier tissu
46. **Feuille rouge** — Tombe arbre automne
47. **Point d’exclamation** — Surprise forte émotion
48. **Dragon** — Crache feu aile
49. **Bougie** — Petite flamme cire
50. **Bonhomme de neige** — Neige carotte hiver
51. **Glaçon** — Cube eau froid
52. **Ancre** — Bateau mer lourd
53. **Arbre** — Tronc feuilles branches
54. **Œil violet** — Regarde voit cligne
55. **Petit cheval d’échec** — Cavalier jeu stratégie
56. **Éclair** — Flash ciel orage
57. **Tortue** — Lente carapace verte

---

## 🎧 Ambiances sonores

Chaque jeton du Puissance 4 peut déclencher une ambiance différente.

### Modes simples à coder
- **Mode métal** : sons saturés, impacts, pulsations
- **Mode concret** : bruits, textures, objets, grains
- **Mode pop fragmentée** : extraits courts, cuts, collages
- **Mode enfant** : voix, syllabes, percussions simples
- **Mode clown** : sons décalés, surprises, glissements
- **Mode calme** : nappes, souffles, cloches, lenteur

### Implémentation simple
- créer un dossier `sons/metal`, `sons/concret`, etc.
- tirer un son au hasard avec `random.choice`
- jouer avec `pygame.mixer` ou `aplay`

---

# 🛠️ Conception

## Ping pong
- créer 3 zones
- placer 1 capteur sous chaque surface
- ajouter mousse ou plaque légère
- tester avec de vraies balles

## Puissance 4
- placer 1 capteur derrière ou sous chaque zone de chute
- renforcer la structure pour éviter les vibrations parasites

## Dobble XXL
- fixer une surface conductrice
- relier chaque carte au Makey Makey
- protéger les contacts

---

# ⏱️ TEMPS DE RÉALISATION

## Débutant

### Programmation
| Module | Temps |
|---|---:|
| Lecture capteurs ping-pong | 2–4 h |
| Lecture capteurs Puissance 4 | 2–4 h |
| Affichage action / symbole | 2–5 h |
| Lecture Makey Makey | 2–4 h |
| Gestion parcours / score | 3–6 h |
| Gestion selfie final | 1–3 h |
| Assemblage du code complet | 4–8 h |

### Fabrication
| Module | Temps |
|---|---:|
| Zones ping-pong | 4–8 h |
| Structure Puissance 4 | 6–12 h |
| Cartes Dobble XXL interactives | 4–6 h |
| Câblage et fixation | 3–6 h |

### Mise en place sur lieu réel
| Tâche | Temps |
|---|---:|
| transport / installation | 1–3 h |
| montage sur site | 2–4 h |
| calibration / tests | 1–3 h |
| ajustements public / sécurité | 1–2 h |

**Total débutant réaliste : 40 à 78 heures**

## Profil expert / artiste numérique habitué au prototypage
**16 à 32 heures** selon finition et qualité de scénographie.

---

# 📸 Selfie final

Le jeu se termine par une invitation.

On appelle les autres.  
On attrape ce qui est là :  
costumes, objets, fragments de ludothèque, accessoires un peu absurdes.

On se rapproche.  
On partage l’image.  
On n’est plus seulement joueur : on devient groupe.

Le selfie n’est pas une preuve.  
C’est une trace collective.  
Une manière de dire : ce jeu a eu lieu, ici, avec nous.

---

# 💻 Code minimal

```python
import random
import time
from gpiozero import Button

ping = [Button(17), Button(27), Button(22)]
p4 = [Button(5), Button(6), Button(13), Button(19)]

SYMBOLS = ["SOLEIL", "LUNE", "FEU", "ARBRE", "EAU", "ECLAIR"]

def detect_ping():
    while True:
        for z in ping:
            if z.is_pressed:
                time.sleep(0.2)
                return

def detect_p4():
    while True:
        for c in p4:
            if c.is_pressed:
                time.sleep(0.2)
                return

while True:
    detect_ping()
    print("ACTION")
    detect_p4()
    print(random.choice(SYMBOLS))
```

---

# 🌿 Conclusion

Ce projet ne cherche pas la maîtrise.  
Il cherche la présence.

Un espace où l’on peut jouer sans savoir,  
et où quelque chose se crée, simplement.
