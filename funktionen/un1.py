def beispiel_fkt(zahl1):
    pass
    #print("Ausgabe")
    
ergebnis = beispiel_fkt(5)
#print(ergebnis)


#Funktion die Differnz berechnet (Minusrechnen)
#Fkt  bekommt 2 Parameter
#berechent Minus und gibt das Ergebnis zurück

#2 Zahlen, mit denen die Fkt aufgerufen wird und das Ergebnis ausgegeben

def gruss(name="Julia",  *, anrede="Hallo"):
    print(f"{anrede}, {name}")

gruss()
gruss(name="Julia", anrede="Guten Morgen")
gruss(anrede="Guten Morgen", name="Julia")

import durchschnitt
print(help(durchschnitt))