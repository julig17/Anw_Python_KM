richtiges_passwort="ABC1234"
eingabe_passwort=input("Passwort eingeben:")

if (eingabe_passwort==richtiges_passwort):
	print("Herzlich Willkommen")
else:
	if (eingabe_passwort==""):
		print("Sie müssen tatsächlich ein Passwort eingeben!")
	else:
		print("Falsches Passwort.")