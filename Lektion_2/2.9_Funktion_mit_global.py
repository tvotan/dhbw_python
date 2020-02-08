# Das Schlüsselwort "global"


# Überschreiben der Variable "zahl"
def zahl_ersetzen():
    global zahl
    zahl = 20
    print("Funktion: Neuer Wert:", zahl)


# Hauptprogramm
zahl = 17

zahl_ersetzen()
print("Hauptprogramm: Neuer Wert:", zahl)