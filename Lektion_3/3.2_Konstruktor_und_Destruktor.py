# Ein Konstruktor ist eine Methode, die immer dann initiiert wird, wenn ein Objekt erzeugt wird.
# Ein Destruktor wird dann aufgerufen, wenn ein Objekt zerstört (gelöscht) wird.


class beispiel(object):
    def __init__(self):  # Konstruktor
        print("Der Konstruktor wurde aufgerufen!")

    def __del__(self):  # Destruktor
        print("Der Destruktor wurde aufgerufen!")


a = beispiel()
b = beispiel()

del a
del b

a

