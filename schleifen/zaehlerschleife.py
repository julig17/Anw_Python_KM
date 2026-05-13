# einfache Zählerschleife

for zaehler in range(1, 9):
    print(zaehler)

#Programmiere mit der zählergesteuerten Schleife die Ausgabe von geraden Zahlen von 0 bis inkl. 20 
for zaehler in range(0,21,2):
    print(zaehler)


import time
countdown = 10

while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1

print("Start!")


zeichenkette = "Hasso"
for buchstabe in zeichenkette:
    if buchstabe.lower() == "l":
        print("l gefunden")
        break
    print(buchstabe)
else:
    print("Kein l gefunden")
print("Fertig")


