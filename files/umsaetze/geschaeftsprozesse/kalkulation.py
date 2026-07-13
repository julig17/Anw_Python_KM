"""
Dieses Modul bietet Hilfsfunktionen im Bereich Kalkulationen an
"""

def berechne_gesamtumsatz(umsaetze):
    """ Methode um den Gesamtumsatz  zu berechen 
    
    args:
        umsätze (list): Liste mit numerischen Zahlen
    returns: 
        float: Summe aller Zahlen
    
    """
    summe = 0
    if(len(umsaetze) == 0):
        return -1
    for umsatz in umsaetze:
        summe +=umsatz
    return summe

def max_umsatz(umsaetze):
    """ Methode um den Größten Umsatz zu bestimmen
    
    args:
        umsätze (list): Liste mit numerischen Zahlen
    returns: 
        float: Größter Umsatz
    
    """
    maximum = umsaetze[0]

    for umsatz in umsaetze:
        if umsatz > maximum:
            maximum = umsatz

    return maximum

def rabatt_anwenden(*, umsaetze, rabatt):
    """ Methode um auf alle Umsätze Rabatt anzuwenden
    
    args:
        umsätze (list): Liste mit numerischen Zahlen
    returns: 
        list: Rabattierte Umsätze
    
    """
    neue_preise = []

    for umsatz in umsaetze:
        neue_preise.append(umsatz * (1 - rabatt / 100))

    return neue_preise


def berechne_umsatz(umsaetze):
    """ Methode um den Gesamtumsatz  zu berechen 
    
    args:
        umsätze (list): Liste mit numerischen Zahlen
    returns: 
        float: Summe aller Zahlen

    """
    if not umsaetze:
        return 0
    return umsaetze[0] + berechne_umsatz(umsaetze[1:])

