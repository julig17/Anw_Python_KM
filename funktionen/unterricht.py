def cpu_last_berechnen1(last1, last2):
    print("Mit zwei Parametern")
    return (last1 + last2) / 2

def cpu_last_berechnen2(liste):
    print("Mit einem Parameter")
    assert len(liste) == 2
    return (liste[0] + liste[1]) / 2

def schreibe_ausgabe():
    print(1)

ergebnis_zahlen = cpu_last_berechnen1(40, 60)
print(ergebnis_zahlen)

ergebnis_liste = cpu_last_berechnen2([20,50])
print(ergebnis_liste)

schreibe_ausgabe()


def subtrahiere_zahlen(minuend, subtrahend):
    return minuend - subtrahend

zahl1 = 50
zahl2 = 20
ergebnis = subtrahiere_zahlen(zahl1, zahl2)
ergebnis_falsch = subtrahiere_zahlen(zahl2, zahl1)  
print(ergebnis)
print(ergebnis_falsch)


def subtrahiere_zahlen2(minuend, subtrahend):
    minuend = 70
    return minuend - subtrahend

zahl1 = 50
zahl2 = 20
ergebnis = subtrahiere_zahlen2(zahl1, zahl2)
print(ergebnis)
print(zahl1)