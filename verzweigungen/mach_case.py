#wir matchen Schulnoten
note = int(input("GEbe eine Zahl zw 1-6 ein:"))

#Funktionsweise:
#Die Variable note wird mit den Cases verglichen
#note = "a"
text = ""
match note:
    case 1:
        text = "Sehr gut"
    case 2 if note == 2 or note == 3:
        print("Gut")
    case 3:
        print("Befriedigend")
    case 4:
        print("Ausreichend")
    case 5:
        print("Mangelhaft")
    case 6:
        print("Ungenügend")
    case _:
        print("Ungültige Note")





def check_value(x):
    match x:
        # Fall 1: x ist ein Integer UND größer als 10
        case int(n) if n > 10:
            return f"{n} ist eine große Zahl"
        # Fall 2: x ist ein Integer, aber <= 10
        case int(n):
            return f"{n} ist eine kleine Zahl"
        # Fall 3: Alles andere
        case _:
            return "Kein Integer"

print(check_value(15))  # Ausgabe: 15 ist eine große Zahl
print(check_value(5)) 