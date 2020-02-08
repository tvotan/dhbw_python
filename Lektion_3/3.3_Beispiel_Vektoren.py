from math import * # S. 148 ff.


class vektor(object):
    x = None  # Klassenattribute
    y = None  # Klassenattribute

    def vorgabe(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def rueckgabe(self):
        return self.x, self.y

    def eingabe(self):
        self.x = float(input("Bitte die x-Komponente eingeben: "))
        self.y = float(input("Bitte die y-Komponente eingeben: "))

    def ausgabe(self):
        if self.x == None or self.y == None:
            print("Es wurde noch kein Vektor definiert!")
        else:
            betrag = sqrt(self.x**2+self.y**2)
            print("X-Komponente: ", self.x)
            print("Y-Komponente: ", self.y)
            print("Der Betrag ist: ", betrag)


v = vektor()
v.ausgabe()

v.eingabe()

v.rueckgabe()

v.ausgabe()

u = vektor()
u.vorgabe(2, 3)
u.ausgabe()