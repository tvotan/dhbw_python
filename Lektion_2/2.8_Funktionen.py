# Funktionen sind nützlich, um wiederkehrenden Code, der mehrfach verwendet werden soll, einmal zu definieren
# für ihre Bezeichnung gelten dieselben Regeln, wie für Variablen
# PEP8: 2 Zeilen vor und nach einer Funktion freilassen


def wochentage():
    print("Montag")
    print("Dienstag")
    print("Mittwoch")
    print("Donnerstag")
    print("Freitag")
    print("Samstag")
    print("Sonntag")


wochentage()
wochentage()

# globale und lokale Variablen
# eine Funktion ist ein in sich geschlossenes Stück Quelltext mit einer speziellen Aufgabe und soll nach außen keine Auswirkungen haben.
# Eine globale Variable kann also nicht so einfach innerhalb von Funktionen verändert werden.


# Überschreiben der Variable Zahl
def zahl_ersetzen():
    zahl = 20
    print("Funktion: Neuer Wert:", zahl)
    testvariable = 408
    print("Testvariable:", testvariable)


# Hauptprogramm
zahl = 17

zahl_ersetzen()
print("Hauptprogramm: Neuer Wert:", zahl)

# Das wäre ein Fehler!
#print("Testvariable:", testvariable)


