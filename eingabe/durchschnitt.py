summe = 0
anzahl = 0  
durchschnitt = 0

while True:
    eingabe = input("Geben Sie eine Zahl ein (oder -1 zum Beenden): ")
    zahl = int(eingabe)
    
    if zahl == -1:
        break
    
    summe += zahl
    anzahl += 1

if anzahl > 0:
    durchschnitt = summe / anzahl
    print(f"Der Durchschnitt ist: {durchschnitt}")
else:
    print("Keine Zahlen eingegeben.")   