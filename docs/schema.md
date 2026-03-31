# Schéma de câblage détaillé

Voir aussi `images/schema-visuel-puissance-dobble-pong.png`.

## Raspberry Pi → capteurs ping-pong
- GPIO17 → zone 1
- GPIO27 → zone 2
- GPIO22 → zone 3

## Raspberry Pi → capteurs Puissance 4
- GPIO5  → colonne 1
- GPIO6  → colonne 2
- GPIO13 → colonne 3
- GPIO19 → colonne 4

## Pour chaque module SW-420
- VCC → 3.3V
- GND → GND
- DO  → GPIO concerné

## Makey Makey
- flèche haut    → carte Dobble 1
- flèche bas     → carte Dobble 2
- flèche gauche  → carte Dobble 3
- flèche droite  → carte Dobble 4
- espace         → carte Dobble 5
- entrée         → carte Dobble 6
- EARTH          → bande conductrice commune / joueur
