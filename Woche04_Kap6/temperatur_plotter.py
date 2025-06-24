#temperatur_plotter.py
import matplotlib.pyplot as plt

def plot_temperatures(werte, zeiten = None):
    """
    Plots the temperature values against time.

    Parameters:
    werte (list): List of temperature values.
    zeiten (list, optional): List of time values. If None, uses indices as time.
    """
    if zeiten is None:
        zeiten = list(range(len(werte)))

    plt.plot(zeiten, werte, marker='o')
    plt.xlabel('Zeit')
    plt.ylabel('Temperatur (°C)')
    plt.title('Temperaturverlauf')
    plt.grid(True)
    plt.show()  
    
if __name__ == "__main__":
    # Example usage
    temperatur_werte = [20, 22, 21, 23, 24, 25, 26]
    zeit_werte = [0, 1, 2, 3, 4, 5, 6]  # Optional time values

    plot_temperatures(temperatur_werte, zeit_werte) 
    