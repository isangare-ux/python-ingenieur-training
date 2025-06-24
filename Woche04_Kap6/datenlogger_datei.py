import  random
import datetime
import os   
import matplotlib.pyplot as plt

def temperatur_werte_generieren():
    """Generiert eine Liste von Temperaturwerten."""
    temperatur_werte = []
    for _ in range(10):
        temperatur_werte.append(random.uniform(20.0, 30.0))
    return temperatur_werte
def zeit_werte_generieren():
    """Generiert eine Liste von Zeitwerten."""
    zeit_werte = []
    startzeit = datetime.datetime.now()
    for i in range(10):
        zeit_werte.append(startzeit + datetime.timedelta(minutes=i))
    return zeit_werte

def plot_temperatures(temperatur_werte, zeit_werte):
    """Plotet die Temperaturwerte gegen die Zeitwerte."""
    plt.plot(zeit_werte, temperatur_werte, marker='o')
    plt.xlabel('Zeit')
    plt.ylabel('Temperatur (°C)')
    plt.title('Temperaturverlauf')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Sicherstellen, dass der Ordner existiert
    os.makedirs('plots', exist_ok=True)
    
    # Speichern des Plots
    plt.savefig('plots/temperatur_plot.png')
    plt.show()  
if __name__ == "__main__":
    print("Starte Plot...")
    temperatur_werte = temperatur_werte_generieren()
    zeit_werte = zeit_werte_generieren()
    plot_temperatures(temperatur_werte, zeit_werte)
# End of file
# End of recent edits

