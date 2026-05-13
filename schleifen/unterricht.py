for zaehler in range(1, 11, 3):
    print(zaehler)
print("Fertig")


zaehler = 0
summe = 0
while zaehler <= 20:
    summe += zaehler
    zaehler += 1

print(summe)


countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1

print("Start!")



while True:
    eingabe = input("Gib etwas ein (oder 'exit' zum Beenden): ")
    if eingabe == "exit":
        print("Programm beendet.")
        break
    print("Du hast eingegeben:", eingabe)
print("Hier wird nach break weitergemacht")


for i in range(1, 21):
    if i % 7 == 0:   # Zahl durch 7 teilbar
        print("Erste Zahl durch 7 gefunden:", i)
        break
