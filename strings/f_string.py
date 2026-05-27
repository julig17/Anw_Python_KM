name = "Julia"
alter = 20
print("ICh heiße", name, "und bin ", alter, "Jahre alt")
print(f"Ich heiße {name} und bin {alter} Jahre alt.")



breite = 5
laenge = 7
print(F"Der Flächeninhalt des Rechteckes ist {breite * laenge} cm^2")

breite = 5
laenge = 5
print(f"Der Flächeninhalt des {'Rechteckes' 
                               if breite != laenge 
                               else 'Quadrates' } ist {breite * laenge} cm^2")



preis = 0.49
print(f"Preis: {preis:.2f}")
print(f"Preis: {preis:10.2f}")
print(f"Preis: {preis:010.2f}")

preis = 15559.49
print(f"Preis: {preis:3.2f}")

#Tabelle
text = "Text"
zahl = 225
f_zahl = 5.5
print(3*(f"|{text:^15s}||{zahl:>15d}||{f_zahl:>15.2f}|\n"))

text = "Alle lieben Python"
print(text[::-1])
