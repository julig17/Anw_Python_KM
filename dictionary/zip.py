ports = [22, 80, 443]
dienste = ["SSH", "HTTP", "HTTPS"]

port_dienst = tuple(zip(ports, dienste))
#print(port_dienst)


kunden_nr = [123, 456, 789, 582]
kunden_name = ["JUlia1", "JUlia2", "JUlia3", "JUlia4"]

kunden_verkn = dict(zip(kunden_nr, kunden_name))

for schluessel in kunden_verkn:
    #print(schluessel, ":", kunden_verkn[schluessel])
    pass
"""
print(kunden_verkn.get(456, "Nicht vorhanden"))
try:
 print(kunden_verkn[457])
except KeyError:
   print("None")


print(kunden_verkn)
print(kunden_verkn.pop(456))
print(kunden_verkn)
del kunden_verkn[456]
"""

zweites_dict = {456:"Max"}
print(kunden_verkn)
print(kunden_verkn.update(zweites_dict))
print(kunden_verkn)

kunden_verkn[456] = "Max"

print(kunden_verkn.items())

values = kunden_verkn.values()

for v_items in values:
    print(v_items)


for item in kunden_verkn.items():
    print(item, item[0], item[1])