import random
# piensas un numero y le vas dando instruciones al computador hasta que se acerque al numero y lo adivine :
def ComputadoraAdivina (x):
    NumeroMasBajo=1
    NumeroMasAlto=x
    InstruccionDelUsuario=""
    NumeroPensadoPorUsuario=int(input(f"Escribe un numero de 1 al {NumeroMasAlto}: "))
    NumeroAleatorio=0
    # mientras la instruccion del usuario sea distinta a lo correcto se ejecuta el bucle
    
    while NumeroPensadoPorUsuario != NumeroAleatorio:
         
         NumeroAleatorio=random.randint(NumeroMasBajo,NumeroMasAlto)
         # usuario tiene tres opciones para eligir    
         InstruccionDelUsuario=input(f"¿¿¿ si El numero {NumeroAleatorio}  es masAlto escriba(a) o si es mas Bajo escriba(b)???").lower()
         if  InstruccionDelUsuario == "a":
            NumeroMasAlto=NumeroAleatorio-1
         elif InstruccionDelUsuario== "b":
           NumeroMasBajo= NumeroAleatorio+1
        
    print(f"el compuatador adivino su numero {NumeroAleatorio} correctamente" )

