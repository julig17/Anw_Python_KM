obst_liste = ["Apfel", "Banane", "Kirsche", "Dattel"]  
print(type(obst_liste))


obst_tupel = ("Apfel", "Banane", "Kirsche", "Dattel", "Apfel") 
print(type(obst_tupel))
print(obst_tupel[0])

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

#wird zu Tupel
kurz = 1,2,5
print(type(kurz))

kurz += koordinaten
print(kurz)


autoren =  ["Goethe", "Broente", "Hugo"]

buecher = ["Faust", "Violette", "Die Elenden", "Schülerlexikon"]
buecher1 = ["Faust", "Violette", "Die Elenden"]

buecher_autoren = list(zip(autoren, buecher))
print("+" *20)
print(buecher_autoren)

autoren_tupel = tuple(autoren)
buecher_tupel = tuple(buecher)

#ZUsicherung dass beide Tupel die gleiche Anzahl an Elementen hat
#assert len(autoren_tupel) == len(buecher_tupel)

wieder_liste = list(autoren_tupel)

print("*" *20)
print(len(autoren_tupel))
print(autoren_tupel[2])
print("*" *20)
for autor in autoren_tupel:
    print(autor)

#range(len(autoren_tupel liefer eine Sequenz 0,1,2
for index in (range(len(autoren_tupel))):
    try:
        print(f"Auf Position {index} schreibt der Autor {autoren_tupel[index]} das Buch {buecher_tupel[index]}")
    except IndexError as fehler :
        print(fehler)

try:
    print(autoren_tupel.index("Ross"))
except ValueError as fehler:
    print(f"Dieser Autor taucht nciht auf: {fehler}")


