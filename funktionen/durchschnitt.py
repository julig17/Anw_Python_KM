"""
Dieses Modul bietet eine Reihe von Funktionen an für kaufmännische Zwecke
"""

def berechne_durchschnitt(werte):
    """ Methode um den Durchschnitt mehrer Zahlen zu berechen 
    
    args:
        werte (list): Liste mit numerischen Zahlen
    returns: 
        float: Durchschnitt aller Zahlen
    
    """
    summe = 0
    if(len(werte) == 0):
        return -1
    for wert in werte:
        summe +=wert
    return summe / len(werte)

print(berechne_durchschnitt([3,4,5,7]))

print(berechne_durchschnitt.__doc__)

    