from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()

img = PhotoImage(file="mike.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = img

etqCombinada = ttk.Label(raiz, text="EtqCombinada",font="italic",foreground="purple", background="blue", compound="center")
etqCombinada.grid()
etqCombinada['image'] = img

raiz.mainloop()