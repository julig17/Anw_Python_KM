
zahl = 5
wort = "Hallo"

#Wenn ich auf diesen Fehler nicht reagiere, stürzt mein Skript ab
neue_art = zahl + wort


try:
    neue_art = zahl + wort
except TypeError:
    print("Datentypen passen nicht zueinander")

zahl2 = 3
print(zahl*zahl2)
print(zahl2**3)