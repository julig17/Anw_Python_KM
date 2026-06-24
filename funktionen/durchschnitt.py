
def berechne_durchschnitt(werte):
    summe = 0
    if(len(werte) == 0):
        return -1
    for wert in werte:
        summe +=wert
    return summe / len(werte)

print(berechne_durchschnitt([3,4,5,7]))

    