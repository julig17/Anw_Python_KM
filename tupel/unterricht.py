obst_liste = ["Apfel", "Banane", "Kirsche", "Dattel"]  
print(type(obst_liste))

obst_tupel = ("Apfel", "Banane", "Kirsche", "Dattel", "Apfel") 
print(type(obst_tupel))

gemischte_tupel = (2.5, 3, "Apfel" , False)
print(gemischte_tupel[1:3])
print(gemischte_tupel[::-1])
obst_liste[1] = "Kiwi"
print(obst_liste)
# Tupel ist immutable, deshalb keine Veränderung
#obst_tupel[1] = "Kiwi"
#obst_liste2 = ["Apfel", "Banane", "Kirsche", "Dattel", "Apfel"]
#obst_liste2 = list(obst_tupel)
#obst_liste2[1] = "Kiwi"
#obst_tupel = tuple(obst_liste2)


# Datentyp verändern
wort = 3
zahl = int(wort)

mehrdimension_tpel = (5, 2, 7,((1,2,"Hallo"), 5, "Wort"))
for element in mehrdimension_tpel:
    if type(element) == tuple:
        for unteres_element in element:
            print(unteres_element)



gemischte_tupel2 = (2.5, 3, "Apfel" , False)
#del gemischte_tupel2[0]
gemischte_tupel2 = gemischte_tupel *3
print(gemischte_tupel2)
tupel_neu = obst_tupel + gemischte_tupel2
print(tupel_neu)

liste = [3.19,4.20,6.99]
neue_preise = []
for element in liste:
    neue_preise.append(element * 2)

print(neue_preise)

#ZIP Funktion in python, funktioniert auch mit Tupel
namen = ["Julia" , "Marie", "Greif", "Müller"]
vorname1,  vorname2, nachname, zuname = namen
nachname = namen[2]
print(nachname)

koordinaten = (1,5)
x,y = koordinaten
