#Zugriff auf eine globale Variable innerhalb einer Funktion
#In diesem Beispiel wird eine globale Variable definiert und innerhalb einer Funktion auf sie zugegriffen.
#Definiert man innerhalb der Funktion eine Variable mit demselben Namen und anderem Wert, 
#wird die globale Variable innerhalb der Funktion überschattet und es entsteht eine lokale Variable.
#Wert der Globalen Variable bleibt unverändert
def funktion_ausgabe():
    print("In Funktion: ",globale_variable)

#Definition einer globalen Variable
globale_variable = "Ich bin eine globale Variable"
#Aufruf der Funktion, die auf die globale Variable zugreift
funktion_ausgabe()
print("Außerhalb Funktion: ",globale_variable)