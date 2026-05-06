#Verschachtelte Verzweigung
zahl = 17

if(zahl %2 == 0):
    print("Gerade")
else:
    print("Ungerade")
    if(zahl % 3 == 0):
        print("und durch drei teilbar")
    else:
        print("und ?")

#oder mit elif
if(zahl %2 == 0):
    print("Gerade")
elif(zahl % 3 == 0):
    print("Ungerade")
    print("und durch drei teilbar")
else:
    print("Ungerade")
    print("und ?")


preis = 5500
if (preis <= 1000.00):
	preis = preis * (1 - 0.03)
elif (preis > 1000.00 and preis <= 5000 ):
	preis = preis * (1 - 0.05)
else:
	preis = preis * (1 - 0.08)
print("Berechneter Preis: ", preis)


preis = 5500

if (preis <= 1000.00):
	preis = preis * (1 - 0.03)
else:
	if (preis > 5000.00):
		preis = preis * (1 - 0.08)
	else:
		preis = preis * (1 - 0.05)
print("Berechneter Preis: ", preis)


match zahl:
    case 1|2|3|4|5:
        print("Wochentag")
    case 6|7:
        print("Wochenende!")
    case _:
        print("Kein Wochentag")

#alle Nullwerte oder leeren Objekte sind False
if(not(0 or 0.0 or "" or [] or False or None)):
    print("Alles False")

