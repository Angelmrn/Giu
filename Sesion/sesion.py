from tkinter import *
from tkinter import ttk

class sesion:
    def __init__(self,raiz):
        raiz.title("Inicio de Sesion")

        self.usuario = StringVar()
        self.contraseña = StringVar()

        mainFrame = ttk.Frame(raiz, padding="10 10 30 30")
        mainFrame.grid(column=0, row=0)

        self.usuario = StringVar()
        self.contraseña = StringVar()

        mainFrame = ttk.Frame(raiz, padding="10 10 30 30")
        mainFrame.grid(column=0, row=0)

        usuarioEntry = ttk.Entry(mainFrame, width=30, textvariable=self.usuario)
        usuarioEntry.grid(column=1, row=0, sticky=(W, E))

        contrasenaEntry = ttk.Entry(mainFrame, width=30, textvariable=self.usuario)
        contrasenaEntry.grid(column=1, row=2, sticky=(W, E))

        ttk.Label(mainFrame, text="Usuario").grid(column=0, row=0)
        ttk.Label(mainFrame, text="").grid(column=0, row=1)
        ttk.Label(mainFrame, text="Contraseña").grid(column=0, row=2)
        ttk.Label(mainFrame, text="").grid(column=3, row=3)
        
        ttk.Button(mainFrame, text="Ingresar").grid(column=1, row=4, sticky=(E))
    