#Schreibe eine Funktion, die eine Liste von Zahlen als 
#Parameter erhält und die größte und kleinste Zahl
#als Tupel(größte, kleinste) zurückgibt.  

def groesste_kleinste_zahl(zahlen_liste):
    #groesste = max(zahlen_liste)
    #kleinste = min(zahlen_liste)
    groesste = meine_max_fkt(zahlen_liste)
    kleinste = meine_min_fkt(zahlen_liste)
    return (groesste, kleinste) 

def meine_max_fkt(zahlen_liste):
    if len(zahlen_liste) == 0:
        return -1
    if len(zahlen_liste) == 1:
        return zahlen_liste[0]
    max = zahlen_liste[0]
    for zahl in zahlen_liste:
        if zahl > max:
            max = zahl
    return max


def meine_min_fkt(zahlen_liste):
    if len(zahlen_liste) == 0:
        return -1
    if len(zahlen_liste) == 1:
        return zahlen_liste[0]
    min = zahlen_liste[0]
    for zahl in zahlen_liste:
        if zahl < min:
            min = zahl
    return min

#Beispielaufruf
zahlen = [34, 12, 5, 67, 23, 89, 1]
ergebnis = groesste_kleinste_zahl(zahlen)   
print("Größte Zahl:", ergebnis[0])
print("Kleinste Zahl:", ergebnis[1])

#Alternativ mit Entpacken des Tupels
groesste, kleinste = groesste_kleinste_zahl(zahlen) 
print("Größte Zahl:", groesste)
print("Kleinste Zahl:", kleinste)


