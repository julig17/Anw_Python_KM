personen = {
    "Max Mustermann": {"Geburtjahr": 1990, "Geschlecht": "männlich"},
    "Anna Müller": {"Geburtjahr": 1985, "Geschlecht": "weiblich"},
    "Peter Schmidt": {"Geburtjahr": 1978, "Geschlecht": "männlich"},
    "Laura Fischer": {"Geburtjahr": 1995, "Geschlecht": "weiblich"},
    "Tom Weber": {"Geburtjahr": 2000, "Geschlecht": "männlich"}
}
"""
print(personen.items())
# Alternative Ausgabe mit Formatierung
print("\nAlternative Ausgabe mit Formatierung:")    
for name, details in personen.items():
    geburtsjahr = details["Geburtsjahr"]
    geschlecht = details["Geschlecht"]
    print(f"{name}, {geburtsjahr}, {geschlecht}")



"""
for name in personen:
    ausgabe = ""
    for werte in personen[name].values():
        ausgabe += str(werte) +", "
    print(name,",",ausgabe)

