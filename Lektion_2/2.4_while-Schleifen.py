# auch als Bedinungsschleife bekannt
# Bedingung nach while definiert
# solange diese Bedingung erfüllt ist, also True ist, wird der eingerückte Code ausgeführt
# folglich muss im Laufe der Abarbeitung irgendwann einmal eine Bedingung False werden, um es zu beenden
# es muss daher eine Abbruchbedingung definiert werden, ansonsten läuft sie in eine Endlosschleife
# und die while-Schleife muss initialisiert werden

# Menü ausgeben
print("Menü:")
print("1: Heizstab ein\n2: Heizstab aus")
# print("2: Heizstab aus")
print("3: Programm beenden")

aktion = 0

# Gewünschte Aktion abfragen
while aktion != 3:
    aktion = int(input("Aktion wählen: "))

    # Funktion ausführen
    if aktion == 1:
        print("Heizstab wird eingeschaltet")
    elif aktion == 2:
        print("Heizstab wird ausgeschaltet")
    elif aktion == 3:
        print("Programm wird beendet")
    else:
        print("Ungültige Eingabe")

# while-else-Schleifen
# Abfragen, wann Zähler beendet werden soll
abbruch = int(input("Abbruch des Zählers bei: "))

zaehler = 0

# Bis zehn oder Abbruch zählen
while zaehler <= 10:
    if zaehler == abbruch:
        print("Zähler abgebrochen")
        break

    zaehler += 1
    print(zaehler)
else:
    print("Zähler erfolgreich beendet!")