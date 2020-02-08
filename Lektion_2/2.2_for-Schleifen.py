# i definiert die Schleifenvariable

# for Aktuelles_Objekt in Allen_Objekten
# • Allen_Objekten = Datenmenge aus Objekten ; iterierbares Objekt, z.B. Listen
# • Aktuelles Objekt = Objekte aus der Datenmenge

# einfache Schleife mit dem Quadrat der Zahl
for i in 1,2,3,4:
    print(i, i*i)

# Zählen von 1 bis 9
for n in range(1, 10, 1):
    print(n)

# Variablen für den Zähler abfragen
start = int(input("Startwert des Zählers: "))
ende = int(input("Endwert des Zählers: "))
schrittweite = int(input("Schrittweite des Zählers: "))

# Zählschleife durchlaufen
for i in range(start, ende, schrittweite):
    print(i)

