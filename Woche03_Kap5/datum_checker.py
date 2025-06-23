from datetime import datetime

def ist_wochenende(datum_str):
    datum = datetime.strptime(datum_str, "%d.%m.%Y")
    return datum.weekday() >= 5

def tage_bis_ziel(datum_str, ziel_str):
    heute = datetime.strptime(datum_str, "%d.%m.%Y")
    
    ziel = datetime.strptime(ziel_str, "%d.%m.%Y")
    return (ziel - heute).days

if __name__ == "__main__":
    heute = "28.06.2025"
    ziel = "01.07.2025"

    print(f"📆 {heute} ist Wochenende? {ist_wochenende(heute)}")
    print(f"⏳ Tage bis {ziel}: {tage_bis_ziel(heute, ziel)}")
