import random

# esta funcion hace que  adivines un numero de 1 a x como parametro y te va diciendo si el numero a adivinar es mayor o menor al que tu pones hasta encontrarlo 
def AdivinaUnNumero (x):

  numerosecreto=random.randint(1,x)
  numerousuario=0

  #mientras el numero a advinar y el numero del usuario no sean iguales ejecuta incansablemente
  while(numerosecreto != numerousuario): 

    
    numerousuario=int(input(f"escriba un numero entre 1 y {x}:  ")) 
    # si el numero que  dijita el usuario no esta entre el rango establecido se  rompe el while y te muestra un mensaje de numero incorrecto
    if(numerousuario<1 or numerousuario>x):
        print("el numero es incorrecto") 
        break 
    if(numerosecreto<numerousuario):
         print("lo siento el numero es menor") 
    elif (numerosecreto>numerousuario):
         print("lo siento el numero es mayor")      
    else:
         print("felicitaciones adivinaste el numero")     

AdivinaUnNumero(30)


