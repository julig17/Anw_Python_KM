import pandas as pd

def schreibe_in_excel(buch_dict):

    # DataFrame erstellen
    df = pd.DataFrame([buch_dict])

    # Als Excel-Datei speichern
    df.to_excel("buecher.xlsx", index=False)
    df.to_html("buecher.html")

    print("Excel-Datei wurde erfolgreich erstellt.")