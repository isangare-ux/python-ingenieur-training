import random
import string

def zufallspasswort_generieren(laenge):
    """
    Generiert ein zufälliges Passwort mit der angegebenen Länge.
    
    :param laenge: Länge des zu generierenden Passworts (Standard: 12)
    :return: Zufallspasswort als String
    """
    zeichen = string.ascii_letters + string.digits + string.punctuation
    passwort = ''.join(random.choice(zeichen) for _ in range(laenge))
    return passwort

if __name__ == "__main__":
    input("Drücke Enter, um ein zufälliges Passwort zu generieren...")  # Warten auf Benutzereingabe    
    passwort_laenge = input("Bitte gib die gewünschte Passwortlänge ein (Standard: 12): ")
    passwort_laenge = int(passwort_laenge) if passwort_laenge.isdigit() else 12  # Standardlänge 12, falls keine Eingabe
    passwort = zufallspasswort_generieren(passwort_laenge)
    print(f"Generiertes Passwort: {passwort}")
