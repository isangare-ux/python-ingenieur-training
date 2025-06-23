import random

def sensorwerte_generieren(anzahl):
    """
    Generiert eine Liste von zufälligen Temperaturwerten.
    
    :param anzahl: Anzahl der zu generierenden Temperaturwerte
    :return: Liste mit Temperaturwerten
    """
    werte = [round(random.uniform(-10, 45), 1) for _ in range(anzahl)]
    print(f"simuliere Sensorwerte :{werte}")
    return werte

def werte_auswerten(werte):
    """
    Auswertung der Temperaturwerte.
    
    :param werte: Liste von Temperaturwerten
    :return: Durchschnitt, Minimum, Maximum
    """
    if not werte:
        return None, None, None
    
    durchschnitt = sum(werte) / len(werte)
    minimum = min(werte)
    maximum = max(werte)
    
    print(f"Durchschnitt: {durchschnitt:.1f} °C, Minimum: {minimum:.1f} °C, Maximum: {maximum:.1f} °C")
    
    return durchschnitt, minimum, maximum

def alarm_pruefen(werte):
    for wert in werte:
        if wert < 18.0:
            print(f"Alarm: Temperatur zu niedrig! ({wert:.1f} °C)")
        elif wert > 30.0:
            print(f"Alarm: Temperatur zu hoch! ({wert:.1f} °C)")    
    else:
        print("Keine Alarme ausgelöst.")    
        
       
if __name__ == "__main__":
    messwerte = sensorwerte_generieren(10)
    werte_auswerten(messwerte)
    alarm_pruefen(messwerte)
    
   
   