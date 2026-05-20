
wort = "Banane%"
#print(wort[1], wort[6])

#print(wort[0:])


#wort[6] = "!"

wort = "Banane!"
#print(wort[6])



#slicing
wort = "Wir testen slicing"
teilstring = wort[::-1]
print(teilstring)

for element in wort:
    if element == "t":
        print("e gefunden")
        break
    print(element)
else:
    print("Element nicht gefunden")




"""str = "Hallo"
zahl = 1
print(str(zahl))"""


