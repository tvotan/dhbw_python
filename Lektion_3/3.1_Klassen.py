# Objektorientiertes Programmieren; Programmiertechnik
# Lektion 1 und 2 war prozedurale Programmierung
# unterschiedliche Daten in Datenpakete gebündelt und in einem einheitlichen Begriff beschrieben
# Klasse_1
# in der Informatik bezeichnet man solche Datenpakete als Verbundstrukturen
# die Kombination aus Datenpaketen und Funktionen, welche zur Manipulation der Daten hinzugefügt werden, nennt man Objekte

# Objekt
# Ein Objekt besteht also aus Daten und Funktionen
# Die Daten werden als Attribute bezeichnet
# Tag, Monat und Jahr sind also Attribute des Objekts Datum

# Klasse
# Eine Klasse kann als Bauplan, Konstrukt ider Schablone zur Erzeugung von Objekten verstanden werden
# Klasse_2


# Definieren einer einfachen Klasse


# Klassendefinition
class Auto:
    def __init__(self, marke, farbe, leistung, anzahl_tueren): # Methoden
        self.kilometerstand = 0 # Attribut
        self.marke = marke
        self.farbe = farbe
        self.leistung = leistung
        self.anzahl_tueren = anzahl_tueren

        print("Hurra, ein Neuwagen!")

    def zeige_daten(self): # Methoden
        print("Marke:", self.marke)
        print("Kilometerstand:", self.kilometerstand)
        print("Farbe:", self.farbe)
        print("Leistung:", self.leistung, "kW")
        print("Anzahl der Türen:", self.anzahl_tueren)

    def strecke_fahren(self, kilometer): # Methoden
        print("Das Auto fährt {0} Kilometer".format(kilometer))
        self.kilometerstand += kilometer


def main():
    # Hauptprogramm
    auto_eins = Auto("Peugeot", "Silber", 100, 3)
    auto_zwei = Auto("Hyundai", "Weiß", 55, 3)

    print("\nDaten von Auto eins:")
    auto_eins.zeige_daten()

    print("\nDaten von Auto zwei:")
    auto_zwei.zeige_daten()

    print("\nDie Autos fahren ein wenig durch die Gegend...")

    auto_eins.strecke_fahren(340)
    auto_zwei.strecke_fahren(408)

    print("Kilometerstand des ersten Autos:", auto_eins.kilometerstand)
    print("Kilometerstand des zweiten Autos:", auto_zwei.kilometerstand)


main()