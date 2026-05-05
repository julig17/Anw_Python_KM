

#Wenn die Zahl gerade ist, gebe „Gerade“ aus.
#Wenn die Zahl ungerade ist, gebe „Ungerade“ aus.
#Aber auf jedenfall gebe die Zahl aus

zahl = 9
modulo = zahl % 2

if (modulo  == 0):
   print("Gerade")
   zahl += 2
else:
   print("Ungerade")
   zahl -= 1
print(zahl)

  

