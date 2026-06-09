fruechte_liste = ["Apfel", "Kirsche", "Banane"]

print(fruechte_liste)

fruechte_liste.append("Erdbeere")
print(fruechte_liste)

print(fruechte_liste.count("Apfel"))

print(fruechte_liste.index("Kirsche"))

gemuese_liste = ["Paprika", "Kartoffeln"]
fruechte_liste.extend(gemuese_liste)
print(fruechte_liste)

fruechte_liste.insert(1, "Tomate")
print(fruechte_liste)

print(fruechte_liste.pop())
print(fruechte_liste)

zahlen = [3,2,5,8,2,9,7]
zahlen.remove(2)
print(zahlen)
zahlen.reverse()
print(zahlen)
print(zahlen[::-1])

zahlen.sort(reverse=True)
print(zahlen)

print("**********************************************")
zahlen_sort = [3,2,5,8,2,9,7]
zahlen_sorted = [3,2,5,8,2,9,7]
print(zahlen_sort.sort())
print(zahlen_sort)
#sorted verändert nicht die ursprüngliche Liste!
neue_liste = sorted(zahlen_sorted)
print("Sorttierte Liste: ", sorted(zahlen_sorted))
print("Aber Liste intern nicht verändert: ", zahlen_sorted)
print("Aber in neuer Liste kann man auch die sortierte Speichern: ", neue_liste)

fruechte_liste.clear()
print(fruechte_liste)