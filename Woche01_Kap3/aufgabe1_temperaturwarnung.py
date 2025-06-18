# aufgabe1_temperaturwarnung.py
import random
import time

def temperaturwarnung(temp):
    if temp < 0:
        return "⚠️ Achtung: Frostgefahr!"
    elif temp < 20:
        return "🧥 Hinweis: Es ist kühl, Jacke empfohlen."
    elif temp <= 35:
        return "✅ Temperatur ist angenehm."
    else:
        return "🔥 Warnung: Hitzewelle!"

while True:
    modus = input("Wähle Modus – (m)anuelle Eingabe oder (s)ensor-Simulation: ").lower()

    if modus == "m":
        try:
            temperatur = float(input("Gib die aktuelle Temperatur in °C ein: "))
        except ValueError:
            print("❌ Ungültige Eingabe! Bitte eine Zahl eingeben.")
            continue
    elif modus == "s":
        temperatur = round(random.uniform(-10, 45), 1)
        print(f"🌡️ Sensorsimulation: {temperatur} °C")
        time.sleep(1)
    else:
        print("Ungültige Auswahl.")
        continue

    status = temperaturwarnung(temperatur)
    print(status)

    choice = input("Weitere Temperatur prüfen? (j/n): ")
    if choice.lower() != "j":
        print("Programm beendet.")
        break