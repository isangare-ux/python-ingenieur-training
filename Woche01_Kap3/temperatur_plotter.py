#temperaur_plotter.py
import random
import time
import matplotlib.pyplot as plt

temperatures = []
zeitstempel = []

print("Temperatur-Sensorsimulation wird in 20 s gestartet...  ")

for sekunde in range(20):
    temperatur = round(random.uniform(-10, 45), 1)
    temperatures.append(temperatur)
    zeitstempel.append(sekunde)
    print(f"🌡️ Zeit: {sekunde}s, Temperatur: {temperatur} °C")
    time.sleep(1)
    
#plotten der Temperaturdaten
plt.plot(zeitstempel, temperatures, marker='o', linestyle='-', color='b')
plt.title("Temperatur-Sensorsimulation")
plt.xlabel("Zeit (s)")
plt.ylabel("Temperatur (°C)")
plt.grid(True)
plt.xticks(range(0, 21, 2))  # X-Achse von 0 bis 20 in Schritten von 2  
plt.yticks(range(-10, 51, 5))  # Y-Achse von -10 bis 50 in Schritten von 5
plt.axhline(y=0, color='blue', linestyle='--', label='Frostgrenze (0 °C)')  
plt.axhline(y=20, color='orange', linestyle='--', label='Kühlgrenze (20 °C)')
plt.axhline(y=35, color='red', linestyle='--', label='Hitzewelle (35 °C)')
plt.legend()
plt.show()
# Hinweis: Stelle sicher, dass matplotlib installiert ist, um die Grafik anzuzeigen.
# Du kannst es mit `pip install matplotlib` installieren, falls es noch nicht installiert ist.
# Hinweis: Dieses Skript simuliert eine Temperaturmessung über 20 Sekunden und plottet die Ergebnisse.
# Es verwendet die Bibliothek matplotlib, um die Temperaturdaten zu visualisieren.
# Hinweis: Die Temperaturwerte werden zufällig generiert und können von -10 °C bis 45 °C reichen.
# Hinweis: Die X-Achse zeigt die Zeit in Sekunden an, während die Y-Achse die Temperatur in °C darstellt.
# Hinweis: Die horizontale Linien markieren die Frostgrenze (0 °C), die Kühlgrenze (20 °C) und die Hitzewelle (35 °C).
# Hinweis: Die Grafik wird automatisch angezeigt, wenn das Skript ausgeführt wird.
# Hinweis: Du kannst die Dauer der Simulation und die Temperaturbereiche anpassen, indem du die entsprechenden Werte im Code änderst.
