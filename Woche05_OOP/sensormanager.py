# Definition der Sensor-Klasse
class Sensor:
    def __init__(self, name, wert):
        # Initialisiert einen Sensor mit Name und Wert
        self.name = name
        self.wert = wert
        
    def messen(self):
        """Simuliert das Messen eines Wertes."""
        import random
        # Setzt den Wert auf einen zufälligen Wert zwischen 20.0 und 30.0
        self.wert = random.uniform(20.0, 30.0)
        print(f"Sensor {self.name} misst: {self.wert:.2f} °C")
        
# Definition der SensorManager-Klasse
class SensorManager:
    def __init__(self):
        # Initialisiert eine leere Liste für Sensoren
        self.sensoren = []

    def sensor_hinzufuegen(self, sensor):
        """Fügt einen Sensor zur Liste hinzu."""
        self.sensoren.append(sensor)
        print(f"Sensor {sensor.name} hinzugefügt.")

    def alle_messen(self):
        """Lässt alle Sensoren messen."""
        for sensor in self.sensoren:
            sensor.messen()
            
    def sensor_ausgeben(self):
        """Gibt die Namen und Werte aller Sensoren aus."""
        for sensor in self.sensoren:
            print(f"Sensor: {sensor.name}, Wert: {sensor.wert:.2f} °C")
            
    def sensor_entfernen(self, sensor_name):
        """Entfernt einen Sensor aus der Liste anhand des Namens."""
        for sensor in self.sensoren:
            if sensor.name == sensor_name:
                self.sensoren.remove(sensor)
                print(f"Sensor {sensor.name} entfernt.")
                return
        print(f"Sensor {sensor_name} nicht gefunden.")
        
    def sensor_aktualisieren(self, sensor_name, neuer_wert):
        """Aktualisiert den Wert eines Sensors anhand des Namens."""
        for sensor in self.sensoren:
            if sensor.name == sensor_name:
                sensor.wert = neuer_wert
                print(f"Sensor {sensor.name} aktualisiert auf {neuer_wert:.2f} °C.")
                return
        print(f"Sensor {sensor_name} nicht gefunden.")
        
        
# Beispiel zur Verwendung des SensorManagers
if __name__ == "__main__":
    manager = SensorManager()
    
    # Zwei Sensoren erzeugen
    sensor1 = Sensor("Temperatursensor 1", 0)
    sensor2 = Sensor("Temperatursensor 2", 0)
    
    # Sensoren zum Manager hinzufügen
    manager.sensor_hinzufuegen(sensor1)
    manager.sensor_hinzufuegen(sensor2)
    
    # Alle Sensoren messen lassen
    manager.alle_messen()
    
    # Sensoren und ihre Werte ausgeben
    manager.sensor_ausgeben()
    
    # Wert eines Sensors aktualisieren
    manager.sensor_aktualisieren("Temperatursensor 1", 25.5)
    
    # Einen Sensor entfernen
    manager.sensor_entfernen("Temperatursensor 2")
    
    # Alle verbleibenden Sensoren erneut ausgeben
    manager.sensor_ausgeben()   
# End of file
