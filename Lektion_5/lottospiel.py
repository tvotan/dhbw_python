"""
Kombinatorik

Das Python-Programm 'lottospiel.py' verfuegt ueber nuetzliche Tools und Funktionen der Kombinatorik.
---
1. Aufgabe:
Realisiere das Lottospiel für den Fall 'zahlenlotto_mit_wiederholung' um.

    Tipp:
    Die mathematische Grundlage bietet die Kombinatorik. Schaue dazu im Ordner nach der PDF-Datei 'kombinatorik.pdf' und versuche die Realisierung des Falls 'zahlenlotto_ohne_wiederholung' nachzuvollziehen.

2. Aufgabe:
Es besteht eine Gefahr, naemlich dass mehr Ziehungen moeglich sind, als Auswahlmoeglichkeit vorhanden sind. Schreibe einen passenden Python-Code, der dies unterbindet.

"""


# Trennstriche
strich = 30 * "-"

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
    print("Es existieren {0} verschiedene Kombinationsmoeglichkeiten für das Lottospiel ohne Wiederholung der Zahlen, wenn man aus insgesamt {1} Zahlen davon {2} Zahlen aussuchen darf.".format(y, p, n))


# Aufgabe 1
def zahlenlotto_mit_wiederholung(p, n):
    # Hier kommt euer Python-Code
    # Bei zahlenlotto_mit_wiederholung handelt es sich mathematisch um eine Kombination mit Wiederholung / Zuruecklegen


# Menue abfragen
def menue():
    print(strich)
    print("Menue:")
    print("(1) Neue Auswahl")
    print("(2) Beenden")
    print(strich)

    # Gewuenschten Menuepunkt abfragen
    auswahl = int(input("Deine Wahl: "))

    return auswahl


# Hauptprogramm
def main():
    while True:

        auswahl = menue()

        if auswahl == 1:
            p = int(input("Bitte gib die Menge der Auswahlmoeglichkeiten an: "))
            n = int(input("Bitte gib die Menge der Ziehungen an: "))

            # Aufgabe 2
            # Hier kommt euer Python-Code
            # Geht sicher, dass die eingegebene Anzahl an Ziehungen nicht hoeher ist als die Anzahl an Moeglichkeiten

        # Spiel beenden
        elif auswahl == 2:
            print("Lottospiel wird beendet")
            break

        else:
            print("Falsche Eingabe")


main()
