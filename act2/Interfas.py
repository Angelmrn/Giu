from tkinter import *
from tkinter import ttk

raiz=Tk()

Nombre = StringVar()
AParerno = StringVar()
AMaterno = StringVar()
Correo = StringVar()
Movil = StringVar()
estado = StringVar()
raiz.title("Muestra Widgets")


comboEstados = ttk.Combobox(raiz, textvariable=estado)
comboEstados.grid(column=1, row= 10)
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

#FRAME CHECk
emple = ttk.Frame(raiz, padding="10 10 10 10")
emple.grid(column= 1, row= 2)

Estudiante = ttk.Radiobutton(emple, text="Estudiante")
Estudiante.grid(column=5,row=1, sticky=(W))
Empleado = ttk.Radiobutton(emple, text="Empleado")
Empleado.grid(column=5,row=2,pady=5, sticky=(W))
Desempleado = ttk.Radiobutton(emple, text="Desempleado")
Desempleado.grid(column=5,row=3,pady=5, sticky=(W))

#FRAME BOTONES
botones = ttk.Frame(raiz, padding="10 10 10 10")
botones.grid(column=0, row=20)

btnGuardar = ttk.Button(botones, text="Guardar", compound="bottom")
btnGuardar.grid(column=0,row=1)
btnCancelar = ttk.Button(botones, text="Cancelar", compound="bottom")
btnCancelar.grid(column=1,row=1)

#FRAME AFICIONES
Aficiones = ttk.Frame(raiz, padding="10 10 30 30",relief="raised")
Aficiones.grid(column=0, row=9, rowspan=5)

Leer = ttk.Checkbutton(Aficiones, text="Leer")
Leer.grid(column=0,row=0)
Musica = ttk.Checkbutton(Aficiones, text="Musica")
Musica.grid(column=1,row=0)
VideoJuegos = ttk.Checkbutton(Aficiones, text="VideoJuegos")
VideoJuegos.grid(column=2,row=0)

#FRAME USUARIO
Usuario = ttk.Frame(raiz, padding="10 10 10 10", relief="raised")
Usuario.grid(column=0, row=1,rowspan=5)

Nombre = ttk.Entry(Usuario, width=30, textvariable=Nombre)
Nombre.grid(column=1, row=0)
AParerno = ttk.Entry(Usuario, width=30, textvariable=AParerno)
AParerno.grid(column=1, row=1)
AMaterno = ttk.Entry(Usuario, width=30, textvariable=AMaterno)
AMaterno.grid(column=1, row=2)
Correo = ttk.Entry(Usuario, width=30, textvariable=Correo)
Correo.grid(column=1, row=3)
Movil = ttk.Entry(Usuario, width=30, textvariable=Movil)
Movil.grid(column=1, row=4)

ttk.Label(Usuario, text="Nombre").grid(column=0, row=0, pady=20)
ttk.Label(Usuario, text="A.Paterno").grid(column=0, row=1, pady=20)
ttk.Label(Usuario, text="A.Materno").grid(column=0, row=2,pady=20)
ttk.Label(Usuario, text="Correo").grid(column=0, row=3,pady=20)
ttk.Label(Usuario, text="Movil").grid(column=0, row=4,pady=20)

raiz.mainloop()