woerterbuch = {"name": "Greif", "vorname" : "Julia"}
menge = {1,2,3}
print(type(menge))



zahlen_set = {1,2,3,5,3,4,5}
print(zahlen_set)
print(len(zahlen_set))
print(7 not in zahlen_set)


for element in zahlen_set:
    print(element)

"""
try:
    gemischte_set = { 1, "Hallo", 3.14, [1,4]}
except TypeError:
    print("TypeError wegen falscher Datentypen")
except Exception as fehler:
    print("Fehler", fehler)
"""

string_set = set("Hallo Welt")
print("Set aus String:", string_set)
print(set(woerterbuch))



"""
zahlen_set = {1,2,3,4,5}
zahlen_set.add(7)
print(zahlen_set)

zahlen_frozen = frozenset([1,2,3,4,5])
#zahlen_frozen.add(8)


#print(dict["one"])
#print(zahlen_set[0])



print(5 in zahlen_set)
print(20 in zahlen_set)
print(20 not in zahlen_set)
print(5 not in zahlen_set)
print(len(zahlen_set))

auto_set ={"BMW", "Opel"}
"""