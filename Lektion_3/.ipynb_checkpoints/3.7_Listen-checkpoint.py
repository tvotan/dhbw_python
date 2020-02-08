a = [1, 3, 5, 7, 9]  # eine Liste ist eine geordnete Zusammenfassung von Elementen
b = [2, "Hallo!", 12.5]  # eine Liste kann unterschiedliche Datentypen speichern bzw. beliebige Objekte
c = [[2, 4], ['a', 'b']]  # auch eine Liste ist ein Objekt und kann daher gespeichert werden
d = [[a, b, c]]  # definierte Variablen können ebenfalls gespeichert werden

print(a)
print(a[0], a[3])  # Zugreif auf ein bestimmtes Element in einer Liste über den Index; der Index fängt in Python bei 0 an
print(b[1])
print(c[1], c[1][1])
print(d)


