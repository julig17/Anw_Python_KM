import kaufmaennisches_rechnen as kr


print(kr.berechne_durchschnitt.__doc__)
print(kr.berechne_durchschnitt([3,4,5,7]))
print(kr.berechne_durchschnitt([2.5, 5, 2.7]))
print(kr.berechne_durchschnitt([]))
print(kr.berechne_durchschnitt([0]))

print(kr.berechne_prozentwert(grundwert=1000, prozentsatz=1))
print(kr.berechne_prozentwert(grundwert=200, prozentsatz=25))
print(kr.berechne_grundwert(prozentwert=1000, prozentsatz=1))
print(kr.berechne_grundwert(prozentwert=200, prozentsatz=25))
print(kr.berechne_prozentsatz(grundwert=200, prozentwert=20))