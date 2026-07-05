import tkinter as tk

fenster = tk.Tk()

def aktualisieren():
    print("Aktualisiert")
    fenster.after(1000, aktualisieren)

fenster.after(1000, aktualisieren)

fenster.mainloop()