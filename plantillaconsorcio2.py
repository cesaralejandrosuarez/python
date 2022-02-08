from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD
from io import open
"""
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

"""
#inicializando
NombreUsuario1_Info=""
Rut1_Info=""
Anexo1_Info=""   
Correo1_Info="" 
Ubicacion1_Info=""
ProcesoRealizado1_Info=""
PruebasRealizadas1_Info=""

#Funcion para crear archivo de texto donde se pega la plantilla.
def guardar():
    
  #Aqui estoy inicializando las variables  
  
  NombreUsuario1_Info=NombreUsuario1.get()
  
  Rut1_Info=Rut1.get()
  Anexo1_Info=Anexo1.get()   
  Correo1_Info=Correo1.get() 
  Ubicacion1_Info=Ubicacion1.get()
  ProcesoRealizado1_Info=ProcesoRealizado1.get() 
  PruebasRealizadas1_Info=ProcesoRealizado1.get()  
    
  #aca escribe en el archivo de texto  la plantilla  
  abrirdocumento = open("documentoword.txt", "w")
  abrirdocumento.write("Nombre del afectado: "+NombreUsuario1_Info+"\n")
  abrirdocumento.write("Rut: "+Rut1_Info+"\n")
  abrirdocumento.write("Anexo/telefono: "+Anexo1_Info+"\n")
  abrirdocumento.write("Correo: "+Correo1_Info+"\n")
  abrirdocumento.write("Ubicacion: "+Ubicacion1_Info+"\n")
  abrirdocumento.write("Descripcion del caso: "+str(combo.get())+"\n")
  abrirdocumento.write("*******************************************\n")
  abrirdocumento.write("Proceso realizado: "+ProcesoRealizado1_Info+"\n")
  abrirdocumento.write("Pruebas realizadas: "+PruebasRealizadas1_Info+"\n")
  abrirdocumento.write("Usuario confirma solucion: "+str(UsuarioConfirmaSolucion.current(1))+"\n")
  #combobox
    
  
  
 #'cursos': ['Python','Django','JavaScript']  
DiccionarioCasos=[  
                  
{
  "Descripcion del caso":"Desbloqueo usuario AD","Proceso realizado":"Se desbloquea  usuario de red, ya puede ingresar al equipo ","Pruebas realizadas":"se verifica que pueda ingresar correctamente/solucionado"},
{
  "Descripcion del caso":"Desbloqueo Usuario  Salesforce","Proceso realizado":"Se comunica desbloque usuario de red, ya puede ingresar a salesforce  ","Pruebas realizadas":"se verifica que pueda ingresar correctamente a salesforce/solucionado"},                
{
  "Descripcion del caso":"Desbloqueo Usuario  PIN","Proceso realizado":"Se desbloqueo usuario en PIN, Ya puede ingresar a la PIN ","Pruebas realizadas":"se verifica que pueda ingresar correctamente a la PIN/solucionado"},                   
{
  "Descripcion del caso":"Desbloqueo Usuario  PINCO","Proceso realizado":"Se desbloqueo usuario en PINCO, Ya puede ingresar a la PINCO ","Pruebas realizadas":"se verifica que pueda ingresar correctamente a la PINCO/solucionado"},    
{
  "Descripcion del caso":"Desbloqueo Usuario  Portal Aplicaciones","Proceso realizado":"Se desbloqueo usuario en Portal Aplicaciones, Ya puede ingresar al Portal Aplicaciones  ","Pruebas realizadas":"se verifica que pueda ingresar correctamente al Portal Aplicaciones /solucionado"},                   
{
  "Descripcion del caso":"licenciamiento Office","Proceso realizado":"se instala actualizacion de Office ","Pruebas realizadas":"se verifica que se haya instalado la actualizacion correctamente/solucionado"},                   
{
  "Descripcion del caso":"Configuracion Wifi","Proceso realizado":"Se configura red corportariva en equipo ","Pruebas realizadas":"se verifica el acceso a la red consorcio/solucionado"},                   
{
  "Descripcion del caso":"Consulta Ticket","Proceso realizado":"Se realiza insistencia al caso, para una pronta gestión del grupo resolutor asignado.","Pruebas realizadas":"SE brinda informacion sobre el estado y el proceso que lleva el ticket que consulta"},                   
{
  "Descripcion del caso":"Configuración impresora","Proceso realizado":"Se realiza configuracion de imprera en equipo.","Pruebas realizadas":"se verifica que pueda imprimir correctamente/solucionado"},                   
{
  "Descripcion del caso":"Acceso VPN","Proceso realizado":"Se realiza la respectiva configuración según se indica en el manual 'Manual SSL VPN Foticlient v1.0' y se logra conectar correctamente.","Pruebas realizadas":"se verifica que pueda imprimir correctamente/solucionado"},                   
{
  "Descripcion del caso":"Se corta llamada","Proceso realizado":"Se corta llamada","Pruebas realizadas":"ninguna"},                   

   ]


ListaDescripcionCasos=[]
for  x in DiccionarioCasos:
       DescripcionCasos=x["Descripcion del caso"]
       ListaDescripcionCasos=DescripcionCasos
print(ListaDescripcionCasos)

#aqui se  abre el archivo y se lee
generarplantilla = open("documentoword.txt", "r")
print(generarplantilla.read())
  

   
  
    
  

#parte grafica como label entry botones etc...
root= Tk()
root.title("Plantilla Consorcio")
root.geometry("500x700")
root.configure(bg="black")

NombreUsuario=Label(root,text="Nombre del Usuario: \n",font=(BOLD),)
NombreUsuario.grid(row=0,column=0)
NombreUsuario1=Entry(root,width=40)
NombreUsuario1.grid(row=0,column=1)

Rut=Label(root,text="RUT: ",font=(BOTH))
Rut.grid(row=1,column=0)
Rut1=Entry(root,width=20)
Rut1.grid(row=1,column=1)

Anexo=Label(root,text="Anexo/Telefono: \n",font=(BOTH),anchor=W)
Anexo.grid(row=2,column=0)
Anexo1=Entry(root,width=20)
Anexo1.grid(row=2,column=1)

Correo=Label(root,text="Correo: \n",font=(BOTH),anchor=W)
Correo.grid(row=3,column=0)
Correo1=Entry(root,width=20)
Correo1.grid(row=3,column=1)

Ubicacion=Label(root,text="Ubicacion: \n",font=(BOTH),anchor=W)
Ubicacion.grid(row=4,column=0)
Ubicacion1=Entry(root,width=20)
Ubicacion1.grid(row=4,column=1)

DescripcionCaso=Label(root,text="Descripcion Caso: \n",font=(BOTH),anchor=W)
DescripcionCaso.grid(row=5,column=0)

#el primer combobox 
#lista descripcion de casos
casos=[" ",
"Desbloqueo Usuario AD",
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

for  x in DiccionarioCasos:
       DescripcionCasos=x["Descripcion del caso"]
   
  
   
  

#estas 4 lineas de codigo junto con  from tkinter import ttk  
#pueden  hacer un combo box
combo=ttk.Combobox(root,width=50)




combo["values"]=DescripcionCasos
#valor que por defecto aparece
combo.current(1)
combo.grid(row=5,column=1 ,) 

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
Proceso realizado:  
Pruebas Realizadas:  
Usuario confirma solución: Si/NO"""

NotasParaCierre=Label(root,text="Notas Para el Cierre: \n",font=(BOTH),anchor=W)

ProcesoRealizado=Label(root,text="ProcesoRealizado: ",font=(BOTH))
ProcesoRealizado.grid(row=6,column=0)
ProcesoRealizado1=Entry(root,width=20)
ProcesoRealizado1.grid(row=6,column=1)

PruebasRealizadas=Label(root,text="ProcesoRealizado: ",font=(BOTH))
PruebasRealizadas.grid(row=7,column=0)
PruebasRealizadas1=Entry(root,width=20)
PruebasRealizadas1.grid(row=7,column=1)

#segundo Combobox
UsuarioConfirmaSolucionLista=["si","no"]
UsuarioConfirmaSolucion=ttk.Combobox(root,width=5)
UsuarioConfirmaSolucion["values"]=UsuarioConfirmaSolucionLista
UsuarioConfirmaSolucion.current(1)
UsuarioConfirmaSolucion.grid(row=8,column=1) 








#boton que llama funcion de escribir un  documento 
generarplantilla=Button(root,text="Start",font=(BOTH),command=guardar)
generarplantilla.grid(row=9,column=0)

root.mainloop()





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


print(NombreUsuario1)





f = open("documentoword.txt", "w")
f.write("esto tiene que abrir!")
f.close()

#open and read the file after the appending:
f = open("documentoword.txt", "r")
print(f.read())"""