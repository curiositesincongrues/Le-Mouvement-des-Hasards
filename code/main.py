#!/usr/bin/env python3
import random
import time
from gpiozero import Button

PING = [Button(17, pull_up=True, bounce_time=0.2),
        Button(27, pull_up=True, bounce_time=0.2),
        Button(22, pull_up=True, bounce_time=0.2)]

P4 = [Button(5, pull_up=True, bounce_time=0.2),
      Button(6, pull_up=True, bounce_time=0.2),
      Button(13, pull_up=True, bounce_time=0.2),
      Button(19, pull_up=True, bounce_time=0.2)]

ACTIONS = [
    "Joue 1 jeton",
    "Joue 2 jetons",
    "Joue 3 jetons",
    "Retire 1 jeton",
    "Retire 2 jetons",
    "Retire 3 jetons",
]

SYMBOLS = ["SOLEIL", "LUNE", "FEU", "ARBRE", "EAU", "ECLAIR"]

def detect_ping():
    while True:
        for i, sensor in enumerate(PING, start=1):
            if sensor.is_pressed:
                time.sleep(0.2)
                return i
        time.sleep(0.01)

def detect_p4():
    while True:
        for i, sensor in enumerate(P4, start=1):
            if sensor.is_pressed:
                time.sleep(0.2)
                return i
        time.sleep(0.01)

def main():
    print("Puissance Dobble Pong — prototype")
    while True:
        zone = detect_ping()
        action = random.choice(ACTIONS)
        print(f"[PING] zone {zone}")
        print(f"[ACTION] {action}")

        colonne = detect_p4()
        symbole = random.choice(SYMBOLS)
        print(f"[P4] colonne {colonne}")
        print(f"[DOBBLE] symbole : {symbole}")
        print("---")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nArrêt.")
