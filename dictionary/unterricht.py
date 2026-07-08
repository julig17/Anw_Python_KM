#anlegen eines leeren Dictionaries
leeres_dict = {}
#print(type(leeres_dict))

#anlegen eines Dictionaries mit Werten
noten_dict = {"Mathematik": [1,2], "Deutsch": 2, "Englisch": 3}
#print(noten_dict)




valides_dict = {42 : "Antwort", (1,2) : {"zweites Dict" : "Inneres Dict"}, 3.14 : "Pi"}
#print(valides_dict)


#Dict mit unterschiedlichen Datentypen
personen_dict = {"Name": "Max Mustermann",
                   1: 21,
                   "Student": True,
                   "Noten": [1, 2, 3]}

#print(personen_dict["Noten"])

for schluessel in personen_dict:
    print(schluessel, ":", personen_dict[schluessel])

#print(personen_dict)
#print(personen_dict["Student"])
#for key in personen_dict:
    #print(key,":", personen_dict[key])


#person = {"vornamen" : "Julia", "nachnamen" : "Greif", "alter" : 40, "hobbys" :["Lesen", "Schwimmen"]}



"""
liste = [2,5,5,15]
print(liste[0])
liste[0] = 7
print(liste[0])
print(len(liste))
wort = "Hallo"
print(wort[0])

print("*"*20)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4, "b":3}
kombiniertes_dict = dict1 | dict2
print(kombiniertes_dict)
"""