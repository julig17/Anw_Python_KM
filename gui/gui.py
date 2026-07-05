import tkinter as tk

def klick(event):
    print(event.x, event.y)

fenster = tk.Tk()

button = tk.Button(fenster, text="Klick")
button.pack()

button.bind("<Button-1>", klick)

fenster.mainloop()