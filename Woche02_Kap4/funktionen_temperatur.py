#funktionen_temperatur.py
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_kelvin(c):
    """Convert Fahrenheit to Celsius."""
    return (c - 32) * 5/9
def temperatur_ausgeben(c):
    f = celsius_to_fahrenheit(c)
    k = fahrenheit_to_kelvin(c)
    print(f"{c}°C = {f:.2f} °F = {k:.2f} Kelvin")
    
temperatur_ausgeben(25)
temperatur_ausgeben(-10)    
    