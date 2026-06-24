'''Übergeben von Parametern an Funktionen per Call by Value'''
def person_daten(alter, nachname):
    print("Wert in Funktion:", id(alter), alter)
    print("Wert in Funktion:", id(nachname), nachname)
    alter = 20
    nachname = "Müller"
    print("Wert in Funktion nach Änderung:", id(alter), alter)
    print("Wert in Funktion nach Änderung:", id(nachname), nachname)

#außerhalb der Funktion
alter = 30
nachname = "Schmidt"
print("Wert außerhalb Funktion vor Aufruf:", id(alter), alter)
print("Wert außerhalb Funktion vor Aufruf:", id(nachname), nachname)


person_daten(alter, nachname) 
print("Wert außerhalb Funktion nach Aufruf:", id(alter), alter)
print("Wert außerhalb Funktion nach Aufruf:", id(nachname), nachname)

       