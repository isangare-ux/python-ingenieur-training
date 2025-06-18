while True:
    try:
        temperatur = float(input("Gib die aktuelle Temperatur in °C ein: "))
    except ValueError:
        print("❌ Ungültige Eingabe! Bitte eine Zahl eingeben.")
        continue    
    
    if temperatur < 0:
        print("⚠️ Achtung: Frostgefahr!")
    elif temperatur < 20:
        print("🧥 Hinweis: Es ist kühl, Jacke empfohlen.")
    elif temperatur <= 35:
        print("✅ Temperatur ist angenehm.")
    else:
        print("🔥 Warnung: Hitzewelle! ")   
    
    choice = input("Weitere Temperatur prüfen? (j/n): ")
    if choice.lower() != "j":
        print("Programm beendet.")
        break

