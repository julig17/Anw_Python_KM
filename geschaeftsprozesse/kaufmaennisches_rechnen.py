"""
Dieses Modul bietet Hilfsfunktionen im BEreich kaufmännisches Rechnen an
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

def berechne_prozentwert(*, grundwert, prozentsatz):
    """
    Berechnet den Prozentwert.

    args:
        grundwert (float): Der Grundwert.
        prozentsatz (float): Der Prozentsatz.

    returns:
        float: Der Prozentwert.
    """
    return grundwert * prozentsatz / 100


def berechne_grundwert(*, prozentwert, prozentsatz):
    """
    Berechnet den Grundwert.

    Args:
        prozentwert (float): Der gegebene Prozentwert.
        prozentsatz (float): Der Prozentsatz.

    Returns:
        float: Der berechnete Grundwert.
    """
    return prozentwert * 100 / prozentsatz


def berechne_prozentsatz(*, prozentwert, grundwert):
    """
    Berechnet den Prozentsatz.

    Args:
        prozentwert (float): Der gegebene Prozentwert.
        grundwert (float): Der Grundwert.

    Returns:
        float: Der berechnete Prozentsatz.
    """
    return prozentwert * 100 / grundwert