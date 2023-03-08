#Conversor de pies a metros 

from tkinter import *
# * significa con todos los elementos 
from tkinter import ttk
from tkinter import messagebox

class Conversor:
    def __init__(self,raiz):
        raiz.title("Pies a Metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz, padding="10 10 30 30")
        mainFrame.grid(column=0, row=0)

        piesEntry = ttk.Entry(mainFrame, width=10, textvariable=self.pies)
        piesEntry.grid(column=1, row=0, sticky=(W, E))

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="Son equivalentes a:").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)

        piesEntry.focus()
        #Hacer la operacion al precionar <Enter>
        raiz.bind("<Return>", self.calcular)
    
    def calcular(self, *args):
        print("Boton Precionado")
        try:
            piesUsuario = float(self.pies.get()) #Siempre devuelve una cadena String/Por lo que es mejor convertirlo desde antes.
            print("Pies ingresados:", piesUsuario)
            piesFlotante = float(piesUsuario)
            metros = piesFlotante * 0.3048
            print("Metros: ", metros)
            self.metros.set(metros)
        except ValueError:
            messagebox.showinfo("Error de Sintaxis", "Dato no valido")
            print("No es un dato valido")
            self.pies.set("")

if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara esto si es el prinipal.")
