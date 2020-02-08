# geordnete Zusammenfassung beliebiger Objekte
# Unterschied zu Listen: Tuples sind unveränderlich

werte = (10, 20, 30)
type(werte)

zahlen = 10, 20, 30
type(zahlen)

print(werte == zahlen)

print(werte + zahlen)

print(3*werte)

print(30 in werte)

print(60 in zahlen)

for i in werte:
    print(i)