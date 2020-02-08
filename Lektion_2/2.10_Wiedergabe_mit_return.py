# Parameterrückgabe und Rückgabewert bei Funktionen


def fakultaet(n):
    p = 1
    for i in range(n):
        p = p*(i+1)
    return p


print(fakultaet(10))
print(fakultaet(5))


# Vorzeichen einer Zahl wechseln
def vorzeichen_wechseln(zahl):
    zahl *= -1

    print("Funktion: Zahl:", zahl)


# Hauptprogramm
eine_zahl = 15

vorzeichen_wechseln(eine_zahl)
print("Hauptprogramm: eine_zahl:", eine_zahl)

vorzeichen_wechseln(21)


# Mehrere Parameter
def volumen_wuerfel(laenge, breite, hoehe): # Parameter
    volumen = laenge*breite*hoehe
    return volumen


volumen_wuerfel(8, 7, 6) # Argumente
