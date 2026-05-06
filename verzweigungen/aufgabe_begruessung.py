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