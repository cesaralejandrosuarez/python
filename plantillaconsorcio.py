
from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD
"""
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

"""


root= Tk()
root.title("Plantilla Consorcio")
root.geometry("500x700")









NombreUsuario=Label(root,text="Nombre del Usuario: \n",font=(BOLD))
NombreUsuario.grid(row=0,column=0)
NombreUsuario1=Entry(root,width=50)
NombreUsuario1.grid(row=0,column=1)

Rut=Label(root,text="RUT: ",font=(BOTH))
Rut.grid(row=1,column=0)
Rut1=Entry(root,width=20)
Rut1.grid(row=1,column=1)

Anexo=Label(root,text="Anexo/Telefono: \n",font=(BOTH))
Anexo.grid(row=2,column=0)
Anexo1=Entry(root,width=20)
Anexo1.grid(row=2,column=1)

Correo=Label(root,text="Correo: \n",font=(BOTH))
Correo.grid(row=3,column=0)
Correo1=Entry(root,width=20)
Correo1.grid(row=3,column=1)

Ubicacion=Label(root,text="Ubicacion: \n",font=(BOTH))
Ubicacion.grid(row=4,column=0)
Ubicacion1=Entry(root,width=20)
Ubicacion1.grid(row=4,column=1)

DescripcionCaso=Label(root,text="Descripcion Caso: \n",font=(BOTH))
DescripcionCaso.grid(row=5,column=0)



casos=["Desbloqueo Usuario AD",
"Desbloqueo Usuario Salesforce",
"Desbloqueo en la PIN",
"Desbloqueo PINCO",
"Desbloqueo Portal Aplicaciones",
"Office Sin Licencia",
"Consulta Ticket: " ,
"Configuración Wifi",
"Configuración Impresora",
"Acceso VPN",
"Se Corta llamada"]
#estas 4 lineas de codigo junto con  from tkinter import ttk  
#pueden  hacer un combo box
combo=ttk.Combobox(root)
combo["values"]=casos
#valor que por defecto aparece
combo.current(1)
combo.place(x=50, y=100)

ProcesoRealizado=Label(root,text="ProcesoRealizado: ",font=(BOTH))
ProcesoRealizado.grid(row=6,column=0)
#caja de texto
ProcesoRealizado1=Text(root,width=20,height=10)
ProcesoRealizado1.grid(row=6,column=1)

generarplantilla=Button(root,text="Start",font=(BOTH))
generarplantilla.grid(row=7,column=0)


"""
saludo=Entry(root,)
saludo.pack()
saludo.insert(0,"enter your  nombre: ")


def myclick():
  mylabel=Label(root,text=f"Hola {saludo.get()}")
  mylabel.pack()

# el boton tiene propiedades  como padx y pady tambien el estado desabilitado 
mybutton=Button(root,text="mi boton",padx=20,pady=5,command=myclick)
mybutton.pack()

"""
root.mainloop()
