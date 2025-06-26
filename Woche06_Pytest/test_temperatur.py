
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Woche02_Kap4.funktionen_temperatur import temperaturwarnung



def test_temperaturwarnung():
    assert temperaturwarnung(-5) == "❄️ Temperatur ist zu niedrig: -5 °C. Frostgefahr!"
    assert temperaturwarnung(20) == "Temperatur ist im normalen Bereich: 20 °C."
    assert temperaturwarnung(36) == "🔥 Hitzewarnung"
    assert temperaturwarnung(30) == "Temperatur ist im normalen Bereich: 30 °C."
    assert temperaturwarnung(35) == "Temperatur ist im normalen Bereich: 35 °C."

