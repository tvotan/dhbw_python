"""
Kombinatorik

Das Python-Programm 'Stochastik.py' verfügt über nützliche Tools und Funktionen der Kombinatorik
---
1. Aufgabe:
Realisiere das Lottospiel für den Fall 'zahlenlotto_mit_wiederholung' um.

    Tipp:
    Die mathematische Grundlage bietet die Kombinatorik. Schaue dazu im Ordner nach der PDF-Datei 'kombinatorik.pdf' und versuche die Realisierung des Falls
    'zahlenlotto_ohne_wiederholung' nachzuvollziehen.

2. Aufgabe:
Es besteht eine Gefahr, nämlich dass mehr Ziehungen möglich sind, als Auswahlmoeglichkeit vorhanden sind.

"""


# Trennstriche
strich = 8 * "-"

# Titel
print("+++ Lottospiel mit variabler Anzahl an Auswahlmoeglichkeiten und Ziehungen +++")


# Berechnung der Fakultaet
def fakultaet(x):
    p = 1

    for i in range(x):
        p = p * (i + 1)

    return p


def zahlenlotto_ohne_wiederholung(p, n):
    h = fakultaet(p)
    j = fakultaet(p-n)*fakultaet(n)
    y = h / j
    print("Es existieren {0} verschiedene Kombinationsmoeglichkeiten für das Lottospiel, wenn man aus insgesamt {1} Zahlen davon {2} Zahlen aussuchen darf.".format(y, p, n))


# Lösung von Aufgabe 1
def zahlenlotto_mit_wiederholung(p, n):
    m = (p + n - 1)
    h = fakultaet(m)
    j = fakultaet(m - n) * fakultaet(n)
    y = h / j
    print("Es existieren {0} verschiedene Kombinationsmoeglichkeiten für das Lottospiel, wenn man aus insgesamt {1} Zahlen davon {2} Zahlen aussuchen darf.".format(y, p, n))


def menue():
    print("---------------------")
    print("Menü:")
    print("(1) Neue Auswahl")
    print("(2) Beenden")
    print("---------------------")

    # Gewünschten Menüpunkt abfragen
    auswahl = int(input("Deine Wahl: "))

    return auswahl


# Menue abfragen
def main():

    #auswahl = None

    #while auswahl != "B" or "b":
    while True:

        auswahl = menue()

        if auswahl == 1:
            p = int(input("Bitte gib die Menge der Auswahlmoeglichkeiten an: "))
            n = int(input("Bitte gib die Menge der Ziehungen an: "))

            # Lösung von Aufgabe 2

            if p >= n:
                print(strich)
                zahlenlotto_ohne_wiederholung(p, n)

                print(strich)
                zahlenlotto_mit_wiederholung(p, n)
            else:
                print("FEHLER: Ziehung darf nicht groesser sein als Auswahl.")

        # Spiel beenden
        elif auswahl == 2:
            print("Lottospiel wird beendet")
            break

        else:
            print("Falsche Eingabe")


main()


