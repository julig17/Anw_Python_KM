# Funktion die eine integer Zahl erhöht
#Parameter int-Zahl
#rückgabe erhöhte Zahl


#vor dem Aufruf print und nach dem Aufruf print




liste = ["Das", "ist", "jetzt", "spannend"]


def erweitere_liste(liste):
   liste.append("!")
   return liste


print("Vor dem Funktionsaufruf:", liste)   
neue_liste = erweitere_liste(liste[:])
print("Nach dem Funktionsaufruf:", neue_liste)
print("Originalwert wird jetzt nicht verändert:", liste)  

