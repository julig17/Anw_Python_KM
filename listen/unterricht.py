# liste in python

"""

print(type(automarken))
autoreifen = [5,2]

zahlen = [1,5,2,8,7]
wort = "HAllo"
gemischte_datentypen = ["BMW", 5, 2.7, [5,2], zahlen, wort, autoreifen]


zahlen[2]
zahlen[2:-1:2]
print(gemischte_datentypen[::-1])

zahlen_2 = [1,5,2,8,7]
print(zahlen_2)
print(zahlen_2[1])
zahlen_2[1] = "HAllo"
print(zahlen_2)
"""


automarken = ["BMW", "Opel", "VW"]
zahlen = [1,5,2,8,7]
zahlen_2 = [1,5,2,8,7]
print(automarken)
print(zahlen)
neue_liste = automarken+zahlen
print(neue_liste)
print(automarken+zahlen)
print(automarken)
print(zahlen)

wort = "Hallo"
#Achtung hier FEhler
# print(zahlen * zahlen_2)

# in und not in Operator
print("a" in wort)
print("k" in wort)
print("k" not in wort)
print("*" *20)
print("BMW" in automarken)
print("bmw" in automarken)
print(5 in automarken)
print("k" not in automarken)
print("*" *20)
# Achtung damit verändert mn die Liste im Unterschied zum + Operator
del zahlen_2[0]
print(zahlen_2)


print("*" *20)
print(zahlen)
del zahlen[1:3]
print(zahlen)

zahl1 = 5
zahl2 = 8
#zahl2 += zahl1
zahl2 = zahl2 + zahl1
print(zahl2)

zahlen = [1,5,2,8,7]
zahlen_2 = [1,5,2,8,7]
zahlen_2 += zahlen
print(zahlen_2)

print(len(zahlen_2))

print("*" *20)
for zaehler in range(2,10,2):
    print(zaehler)

print

for buchstabe in "ZEichenkette":
    print(buchstabe)

#Zugriff auf alle elemente in der Liste
# python beliebt Variante
for element in automarken:
    print(element)

zahl = 0
automarken[zahl]

print("*" *20)
print(len(automarken))
for zaehler in range(len(automarken)):
    print("Bei Zähler:", zaehler, "ist in der Liste drin:", automarken[zaehler])

print("*" *20)
i = 0
while i < len(automarken):
	print(automarken[i])
	i = i + 1



liste = [15,5,2,8,1]