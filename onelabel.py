from tkinter import * 
from tkinter import  ttk
ventana= Tk()
ventana.title("bienvenido ")
ventana.geometry("500x300")
def click1():
  getit= caja1.get()
  etiqueta1.config(text=getit)
etiqueta1=Label(ventana,text="escribe el usuario")
etiqueta1.pack() 
valor=""
caja1= Entry(ventana,textvariable=valor)
caja1.pack() 
Button(ventana,text="click",command=click1).pack()
ventana.mainloop()