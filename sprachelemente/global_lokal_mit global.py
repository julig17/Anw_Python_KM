#schreibender ZUgriff auf globale Variable durch Schlüsselwort global
def funktion_ausgabe():
    global globale_variable
    print("In Funktion  global: ",globale_variable)      
    globale_variable = "Ich bin lokal Variable"
    print("In Funktion : ",globale_variable)

#Definition einer globalen Variable
globale_variable = "Ich bin eine globale Variable"
#Aufruf der Funktion, die auf die globale Variable zugreift
funktion_ausgabe()
print("Außerhalb Funktion: ",globale_variable)