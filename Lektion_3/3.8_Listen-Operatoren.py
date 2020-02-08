# Listen sind iterierbare Objekte, daher können Funktionen und Operatoren eingesetzt werden

# in-Funktion
moegliche_farben = ["rot", "gruen", "blau"]
farbe = input("Bitte Farbe eingeben: ")

if farbe not in moegliche_farben:
    print("Diese Farbe ist nicht enthalten!")
else:
    print("Diese Farbe ist enthalten!")

# len-Funktion
anzahl = len(moegliche_farben)

for i in range(0, anzahl, 1):
    print(i, moegliche_farben[i])


# äquivalent zu:

for i in moegliche_farben:
    print(i)


# äquivalent zu:

for i in moegliche_farben:
    j = moegliche_farben.index(i)
    print(j, i)


inhalt = [5, 23, 45, 15, 22, 54]

print(inhalt)

# sortieren
inhalt.sort()
print(inhalt)

# drehen
inhalt.reverse()
print(inhalt)


inhalt = [23.5, 12, [19, "Hallo"], 12, 45]
print(inhalt)

# anhängen
inhalt.append(100)
print(inhalt)

inhalt[2].append(200)
print(inhalt)

# zählen
anzahl = inhalt.count(12)
print(anzahl)

# löschen
inhalt.remove(23.5)
print(inhalt)

# Index abfragen
ind = inhalt.index(45)
print(ind)

# einfügen
inhalt.insert(3, 77)
print(inhalt)


# Operatoren

## Addieren  und Multiplizieren
Liste1 = [1, 2, 3]
Liste2 = [3, 4, 5]
Ergebnis = Liste1 + Liste2
print(Ergebnis)

E = 4*Liste2
print(E)

## Überschreiben von Listenelementen - Zugriff auf letztes Element
Liste1 = [10, 20, 40, 70]

Liste1[2] = -45
Liste1[-1] = 90
print(Liste1)

## Maximum und Minimum ermitteln
max(Liste1)
min(Liste1)

Orte = ["Xanten", "Essen", "Aachen", "Wuppertal"]
min(Orte)
max(Orte)