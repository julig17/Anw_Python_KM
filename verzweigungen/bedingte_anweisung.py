

#Wenn die Zahl gerade ist, gebe „Gerade“ aus.
#Wenn die Zahl ungerade ist, gebe „Ungerade“ aus.
#Aber auf jedenfall gebe die Zahl aus
"""
zahl = 9
modulo = zahl % 2

if (modulo  == 0):
   print("Gerade")
   zahl += 2
else:
   print("Ungerade")
   zahl -= 1
print(zahl)


x = 8
if x > 5 and x < 10:
   print("A")
else:
   print("B")

x = 3
if x == 1 or x == 2 or x == 3:
   print("Treffer")

x = 3
if x == 1 or 2 or 3: 
   print("OK")

x = 5
if x > 10 and x < 20 or x == 5:
   print("Ja")
else:
   print("Nein")

  
x = 0
if not x:
   print("Leer")
else:
   print("Nicht leer")

   





benutzer = "admin"
passwort = "12345"
superuser = False

if benutzer == "admin" and (passwort == "1234" or superuser):
   print("Login erfolgreich")
else:
   print("Fehler")



"""
name = "f"
if not name:
	print("Name ist  nicht leer")
else:
   print("Name ist leer")






