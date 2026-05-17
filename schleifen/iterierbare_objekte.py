zeichenkette = "Datenverarbeitung"

for buchstabe in zeichenkette:
    if buchstabe.lower() == "n":
        break
    print(buchstabe)
else:
    print("Ich habe diese Zeichenkette nicht gefunden")
print("Fertig")