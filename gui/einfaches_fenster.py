import tkinter as tk

fenster = tk.Tk()
fenster.title("Erstes Fenster")
fenster.geometry("500x500")

text_label = tk.Label(fenster, text="Hallo Fenster!")
text_label.pack()

zahl = 1

def aktualisieren():
    global zahl
    print("Aktualisiert")
    zahl += 1
    label_text = "Hallo" + str(zahl)
    text_label.config(text=label_text)
    fenster.after(1000,aktualisieren)
    
fenster.after(1000,aktualisieren)

fenster.mainloop()

