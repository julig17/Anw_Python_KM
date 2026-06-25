from rechteck import Rechteck
# Beispiel für die Verwendung der Rechteck-Klasse

print(help(Rechteck))

r1 = Rechteck(5, 3)

print("Länge:", r1.laenge)
print("Breite:", r1.breite)
print("Fläche:", r1.flaeche())
print("Umfang:", r1.umfang())

r2 = Rechteck(7, 5)

print("Länge:", r2.laenge)
print("Breite:", r2.breite)
print("Fläche:", r2.flaeche())
print("Umfang:", r2.umfang())