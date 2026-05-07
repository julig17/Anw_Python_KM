name = input("Gib einen Namen ein: ")
geschlecht = input("Gib ein Gechlecht ein m/w/ : ")
uhrzeit = int(input("Gib eine Uhrzeit ein 0-24: "))

uhrzeit_begruessung = "Guten Morgen"
geschlecht_text = " "
if(uhrzeit >= 10 and uhrzeit <= 17):
    uhrzeit_begruessung = "Guten Tag"
elif(uhrzeit >= 18 and uhrzeit <= 24):
    uhrzeit_begruessung = "Guten Abend"


if(geschlecht == "m" or geschlecht_text == "M"):
    geschlecht_text = "Herr"
elif(geschlecht == "w" or geschlecht_text == "W"):
    geschlecht_text = "Frau"
else:
    geschlecht_text = "Divers"

print(f"{uhrzeit_begruessung} {geschlecht_text} {name}")


#Die Anrede soll je nach Tageszeit mit „Guten Morgen“ (0–9 Uhr), „Guten Tag“
#(10–17), „Guten Abend (18–0 Uhr) 

match uhrzeit:
    case uhrzeit if uhrzeit > 9 and uhrzeit < 18:
        text = "Mittag"
    case uhrzeit if uhrzeit > 17 and uhrzeit < 25:
        text = "Abend"
    # Fall 3: Alles andere
    case _:
        text = "Morgen"
print(text)
