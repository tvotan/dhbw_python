class Automobil(object):
    antrieb = "Ottomotor"
    leistung_in_kw = 120.0

    def ausgabe(self):
        print("Antrieb: ", self.antrieb)
        print("Leistung: ", self.leistung_in_kw)


class PKW(Automobil):
    pass


a = Automobil()
a.ausgabe()

b = PKW()
b.ausgabe()

# b verhält sich so wie a
# die Klasse PKW erbt/übernimt die Attribute und Objekte von Automobil
# Automobil ist die Oberklasse/Superklasse
# PKW ist die Unterklasse/Subklasse
# Auf diese Weise lassen sich Klassenhierarchie abbilden
# Klassen_4

