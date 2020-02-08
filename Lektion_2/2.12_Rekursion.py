# Verwenden einer Funktion innerhalb derselben Funktion


# Rekursive Funktion für einen Countdown
def countdown(wert):
    print("Countdown:", wert)

    if wert > 0:
        countdown(wert-1)


# Hauptprogramm
countdown(10)