import tkinter as tk


def speichern():
    """
    Liest die Eingaben aus den Textfeldern und gibt sie auf der Konsole aus.
    """
    isbn = entry_isbn.get()
    autor = entry_autor.get()
    titel = entry_titel.get()
    erscheinungsjahr = entry_erscheinungsjahr.get()

    print("Buchdaten")
    print(f"ISBN : {isbn}")
    print(f"Autor: {autor}")
    print(f"Titel: {titel}")
    print(f"Erscheinungsjahr: {erscheinungsjahr}")
    print("-" * 30)


# Fenster erstellen
fenster = tk.Tk()
fenster.title("Buchverwaltung")

# Beschriftungen
tk.Label(fenster, text="ISBN:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(fenster, text="Autor:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(fenster, text="Titel:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(fenster, text="Erscheinungsjahr:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

# Eingabefelder
entry_isbn = tk.Entry(fenster, width=40)
entry_autor = tk.Entry(fenster, width=40)
entry_titel = tk.Entry(fenster, width=40)
entry_erscheinungsjahr = tk.Entry(fenster, width=40)

entry_isbn.grid(row=0, column=1, padx=10, pady=5)
entry_autor.grid(row=1, column=1, padx=10, pady=5)
entry_titel.grid(row=2, column=1, padx=10, pady=5)
entry_erscheinungsjahr.grid(row=3, column=1, padx=10, pady=5)

# Button
button_speichern = tk.Button(
    fenster,
    text="Speichern",
    command=speichern
)
button_speichern.grid(row=4, column=0, columnspan=2, pady=15)

# Ereignisschleife starten
fenster.mainloop()