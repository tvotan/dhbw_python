# Fortführung mit 'continue'

zaehler = 0

# Von 1 bis 10 zählen
while zaehler <= 10:
    zaehler += 1

    # Ungerade Zahlen ignorieren
    if zaehler % 2:
        continue  # Alles ab hier wird übersprungen

    print("Zähler: ", zaehler)


# Aufgabe auch ohne 'continue' lösbar

zaehler = 0

while zaehler <= 10:
    zaehler += 1

    if zaehler % 2 == 0:
        print("Zähler: ", zaehler)

