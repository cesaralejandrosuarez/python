import tkinter as tk


def menu_pantalla():
    global pantalla
    pantalla =tk.Tk()
    pantalla.geometry("350x450")
    pantalla.title("login_propio") 

    #montamos la imagen
    imagen=tk.PhotoImage(file="logo1.gif")
    imagen=imagen.subsample(4,6)
    etiquetaimagen=tk.Label(image=imagen)
    etiquetaimagen.pack()

    etiqueta1=tk.Label(text="Access to the system",bg="#F7E3F9",fg="#67106E",height=2,width=30,pady=0)
    etiqueta1.pack()

    Iniciar_Seccion=tk.Button(text="Iniciar Seccion",height=3,width=30,pady=0,command=inicio_seccion)
    Iniciar_Seccion.pack()

    registrar=tk.Button(text="Registrar",height=3,width=30,pady=0,command=funcion_registrar)
    registrar.pack()



    pantalla.mainloop()
    
def inicio_seccion():
 
  # creacion de  la nueva ventana
  global pantatalla1
  pantalla1=tk.Toplevel(pantalla)
  pantalla1.geometry("400x250")
  pantalla1.title=("inicio de seccion")
   
  # mensaje  con un espacio
  tk.Label(pantalla1,text="por favor ingrese usuario y contraseña\n si ya esta registrado: ").pack()
  tk.Label(pantalla1,text="").pack()


  #se crean las variables para que guarden los datos que inserto el usuario 
  global nombreusuario_verify
  global contraseñausuario_verify
  

  nombreusuario_verify=tk.StringVar()   
  contraseñausuario_verify=tk.StringVar() 

  global nombre_usuario_entry
  global contraseña_usuario_entry


  #se crean las etiquetas y el entry las cuales se alamacenan en la variable de arriba 
  tk.Label(pantalla1,text="usuario").pack()
  nombre_usuario_entry=tk.Entry(pantalla1,textvariable=nombreusuario_verify)
  nombre_usuario_entry.pack()

  tk.Label(pantalla1,text="contraseña").pack()
  contraseña_usuario_entry=tk.Entry(pantalla1,textvariable=contraseñausuario_verify) 
  contraseña_usuario_entry.pack()

  tk.Label(pantalla1,text="").pack() 
  tk.Button(pantalla1,text="iniciar seccion").pack() 


def funcion_registrar():
  # creacion de  la nueva ventana
  global pantatalla2
  pantalla2=tk.Toplevel(pantalla)
  pantalla2.geometry("400x250")
  pantalla2.title=("inicio de seccion")

  # mensaje  con un espacio
  tk.Label(pantalla2,text="por favor ingrese usuario y contraseña \n para registrar usuario: ").pack()
  tk.Label(pantalla2,text="").pack()


 #se crean las variables para que guarden los datos que inserto el usuario 
  global nombreusuario_verify
  global contraseñausuario_verify
  
  nombreusuario_verify=tk.StringVar()   
  contraseñausuario_verify=tk.StringVar()


  tk.Label(pantalla2,text="usuario").pack()
  nombreusuario_verify=tk.Entry(pantalla2)
  nombreusuario_verify.pack()

  tk.Label(pantalla2,text="contraseña").pack()
  contraseñausuario_verify=tk.Entry(pantalla2) 
  contraseñausuario_verify.pack()

  tk.Label(pantalla2,text="").pack() 
  tk.Button(pantalla2,text="Registrar").pack() 




menu_pantalla()  
