import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Woche05_OOP.sensormanager import Sensor, Messung, SensorManager

# === Unit-Tests für einzelne Klassenkomponenten ===

def test_sensor_erstellen():
    sensor = Sensor(sensor_id=1, name="Temperatur", einheit="°C")
    assert sensor.sensor_id == 1
    assert sensor.name == "Temperatur"
    assert sensor.einheit == "°C"
    assert sensor.messungen == []

def test_messung_hinzufuegen():
    sensor = Sensor(1, "Temperatur", "°C")
    messung = Messung(wert=25.5, zeitpunkt="2024-06-26")
    sensor.neue_messung(messung.wert, messung.zeitpunkt)
    assert len(sensor.messungen) == 1
    assert sensor.messungen[0].wert == 25.5

def test_sensor_durchschnitt():
    sensor = Sensor(1, name="Temperatur", einheit="°C")
    sensor.neue_messung(20, "2024-06-26")
    sensor.neue_messung(30, "2024-06-27")
    assert sensor.durchschnittswert() == 25

# === Integrationstest für SensorManager ===

def test_manager_sensorverwaltung():
    manager = SensorManager()
    sensor = Sensor(1, name="Temperatur", einheit="°C")
    manager.sensor_hinzufuegen(sensor)
    assert len(manager.sensoren) == 1
    assert manager.finde_sensor(1) == sensor

def test_manager_statistik():
    manager = SensorManager()
    sensor = Sensor(1,name="Temperatur", einheit="°C")
    sensor.neue_messung(10, "2024-06-26")
    sensor.neue_messung(20, "2024-06-27")
    manager.sensor_hinzufuegen(sensor)

    statistik = manager.auswertung()
    assert "Temperatur" in statistik
    assert statistik["Temperatur"] == 15  # Durchschnitt
