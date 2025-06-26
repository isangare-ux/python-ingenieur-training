#funktion aus Woche02_Kap4/funktionen_temperatur.py
#from datetime import datetime
# from sensormanager import Sensor, SensorManager

def temperaturwarnung(temp_c):
    """Gibt eine Warnung aus, wenn die Temperatur über 30 Grad Celsius liegt."""
    if temp_c < 0:
        return f"❄️ Temperatur ist zu niedrig: {temp_c} °C. Frostgefahr!"
    elif temp_c > 35:
        return "🔥 Hitzewarnung"
    else:
        return f"Temperatur ist im normalen Bereich: {temp_c} °C."