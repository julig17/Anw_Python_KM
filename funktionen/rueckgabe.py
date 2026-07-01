# Funktion die eine integer Zahl erhöht
#Parameter int-Zahl
#rückgabe erhöhte Zahl


#vor dem Aufruf print und nach dem Aufruf print




liste = ["Das", "ist", "jetzt", "spannend"]

def erweitere_liste(liste):
   """
    Die Funktion erweitere Liste erweitert Liste
    """
   liste.append("!")
   return liste


print(help(erweitere_liste))

print("Vor dem Funktionsaufruf:", liste)   
neue_liste = erweitere_liste(liste[:])
print("Nach dem Funktionsaufruf:", neue_liste)
print("Originalwert wird jetzt nicht verändert:", liste) 

zahle_liste = [15,30,45,2]
print(min(zahle_liste))

def gebe_tupel_zurück(liste):
   return liste[0], liste[-1]

tupel1, tupel2 = gebe_tupel_zurück(liste)
print(tupel1, tupel2)



