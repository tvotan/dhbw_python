# auch Mengen
# ungeordnete Zusammenfassung von Objekten, wobei jedes Element nur einmal darin vorkommen kann
# Listen können keine Elemente von Sets sein

Menge1 = set([12, 34, 60, 12, 72, 34, 90])
print(Menge1)

Menge2 = set([17, 90, 34, 34, 112, 9, 12])
print(Menge2)

# Sets_1
# Durchschnitt buw. Schnittmenge
Menge1 & Menge2

# Differenz
Menge1 - Menge2
Menge2 - Menge1

# Vereinigung
Menge1|Menge2

for i in Menge1:
    print(i)