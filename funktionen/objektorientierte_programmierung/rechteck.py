"""
Diese Klasse ist eine Abstraktion eines Rechtecks,
welche über die Attribute Länge und Breite beschrieben wird.
Das Rechteck bietet die Methode flaeche und zmfang an, mit denen man 
den Flächenumfang und den Umfang des Rechtecks bestimmen kann.

"""

#das ist ein normaler KOmmentar
class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def flaeche(self):
        """Die Methode flaeche berechnet den Flächeninhalt eines Rechtecks 
        und liefert den Flächeninhalt zurück

        Returns:
            float: Flächeninhalt
        """
        return self.laenge * self.breite

    def umfang(self):
        """Die Methode umfang berechnet den Umfang eines Rechtecks 
        und liefert den Umfang zurück

        Returns:
            float: Umfang
        """
        return 2 * (self.laenge + self.breite)



