from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text="Boton solo texto")
boton.grid()

img = PhotoImage(file="mike.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] = img
btnCombinada = ttk.Button(raiz, text="Boton Combinado", compound="bottom")
btnCombinada.grid()
btnCombinada['image'] = img

chkBoton = ttk.Checkbutton(raiz, text="Opcion 1")
chkBoton.grid()

raiz.mainloop()