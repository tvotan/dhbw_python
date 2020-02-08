# ungeordnete Zusammenfassung von Schlüssel-Wert-Paaren bzw. assoziative Arrays
# ähnlich wie eine Tabelle
# jedem Datenwert (data value) wird ein Schlüsselwert (key value) zugeordnet
# die Datenwerte dürfen aus Listen bestehen, die Schlüsselwerte jedoch nicht

woerterbuch = {"rot":"red","gelb":"yellow","gruen":"green"}
kfz = {"DO":"Dortmund","E":"Essen","W":"Wuppertal"}
print(kfz["DO"])

print(woerterbuch["gelb"])
#print(woerterbuch["yellow"])  # Fehlermeldung

type(kfz)

kfz["B"]="Berlin"
print(kfz)

neu = {}

type(neu)

print(neu)