class Messung:
    def __init__(self, wert, zeitpunkt):
        self.wert = wert
        self.zeitpunkt = zeitpunkt

class Sensor:
    def __init__(self, sensor_id, name, einheit):
        self.sensor_id = sensor_id
        self.name = name
        self.einheit = einheit
        self.messungen = []

    def neue_messung(self, wert, zeitpunkt):
        self.messungen.append(Messung(wert, zeitpunkt))
    
    def durchschnittswert(self):
        if not self.messungen:
            return None
        gesamt = sum(m.wert for m in self.messungen)
        return gesamt / len(self.messungen)

class SensorManager:
    def __init__(self):
        self.sensoren = []

    def sensor_hinzufuegen(self, sensor):
        self.sensoren.append(sensor)

    def finde_sensor(self, sensor_id):
        for s in self.sensoren:
            if s.sensor_id == sensor_id:
                return s
        return None
    def auswertung(self):
        """
        Gibt ein Dictionary mit dem Namen jedes Sensors und dessen Durchschnittswert zurück.
        """
        statistik = {}
        for sensor in self.sensoren:
            durchschnitt = sensor.durchschnittswert()
            statistik[sensor.name] = durchschnitt
        return statistik