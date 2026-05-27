test_wort = "Hallo"
print(len(test_wort))
print(test_wort + "Welt")
print(test_wort * 4)
print("H" in test_wort)
print(test_wort.endswith("la"))


test_str = "DAS WETTER IST TOLL!"
test_str1 = "ja/NEIN"
print(test_str.lower())
print(test_str1.upper())

test_str = "Hallo Welt!"
print(test_str.replace(" ", "#"))

separator = "#"
test_str4 = "Testwort#Hallo#Welt#!"
liste = ["HAllo", "Welt", "Du"]
print(" ".join(liste))
liste = test_str4.split(separator)
print(liste[0])