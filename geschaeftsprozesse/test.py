import kaufmaennisches_rechnen as kr
import kalkulation as ka


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


umsaetze = [2500, 575.45, 222.99, 40.50, 10.39]
gesamt_umsatz = ka.berechne_gesamtumsatz(umsaetze)
print(f"GesamtUmsatz: {gesamt_umsatz:.2f} €")
max_umsatz = ka.max_umsatz(umsaetze)
print(f"Max Umsatz: {max_umsatz:.2f} €")
rabattierte_umsaete = ka.rabatt_anwenden(umsaetze=umsaetze, rabatt=1)
print(f"Rabattierte Umätze: {', '.join(f'{umsatz:.2f} €' for umsatz in rabattierte_umsaete)}")