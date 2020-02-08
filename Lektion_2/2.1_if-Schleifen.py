# Anweisungen, die nur nach jeder Bedingung ausgeführt werden sollen werden eingerückt.
# Diese bilden einen Einrückungsblock; Python erkennt an der Einrückung die Zugehörigkeit zur vorangehenden Bedingung.
# Anweisungen müssen um die gleiche Anzahl von Zeichen eingerückt werden

# Wiederholung der letzten Woche:
# für if-Schleifen ist es wichtig, dass nach dem if-Statement eine Bedingung folgt, die zu prüfen ist.
# Gibt die Bedingung am Ende ein True aus, werden alle Anweisungen im Einrückungsblock zur vorangehenden Bedingung ausgeführt, daher müssen diese dieselbe Einrückung haben

# Ein Beispiel bildeten die Vergleichsoperatoren mit der if-Schleife

# for-Schleife

# Wiederholung/Übung zu logische Operatoren
# Schleifen (oder Loops) werden genutzt, um Teile des Programms wiederholt durchlaufen zu lassen.

age = int(input("Alter der Person angeben: "))

if age >= 30:
    if age <= 39:
        print("2 - Diese Person ist in ihren 30ern.")
    else:
        print("2 - Diese Person ist nicht in ihren 30ern.")
else:
    print("2 - Diese Person ist nicht in ihren 30ern.")

# Lösung mit and
if age >= 30 and age <= 39:
    print("3 - Diese Person ist in ihren 30ern.")
else:
    print("3 - Diese Person ist nicht in ihren 30ern.")

# Lösung mit or
if age < 30 or age >= 40:
    print("4 - Diese Person ist nicht in ihren 30ern.")
else:
    print("4 - Diese Person ist in ihren 30ern.")

# Direkter Abfragenaufruf:

if True:
    print("if-Abfrage wurde ausgeführt")



