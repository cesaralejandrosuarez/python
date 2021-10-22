#El projecto Hangman
import os
import random
#se importa el listado que tengo en otro archivo 
from ListaDePalabras import ListaDePalabras


def run():
   
     imagenes= ['''
      +---+
      |   |
          |
          |
          |
          |
     =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
     =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
     =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
     =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
     =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
     =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
     =========''']
     #declaramos la varibles siempre al principio como de costumbre 
     palabra=random.choice(ListaDePalabras)
     espacios=["_"]*len(palabra)
     intentos = 6
     print(espacios)

     
     #creamos un bucle que siempre se repita
     while True:
       
       # este comando sirve para  limpiar la  linea de comandos
       os.system("cls")
       
       for caracter in espacios:   
            print(caracter,end="")
           
       print(imagenes[intentos])    
       letra= input("elige una letra: ")   
       encontro=False
       
       for idx,caracter in enumerate(palabra):
            if caracter== letra:
                espacios[idx]= letra
                encontro=True
  
       if not encontro:
            intentos-=1

       if "_" not in espacios:
            
            print("¡¡¡you won!!!")    
            break
            input()
     
       if intentos == 0:
            
            print("¡¡¡ Sorry Hangman !!!")    
            print(f"la palabra era: {palabra}")
            break
            input()

      


if __name__=="__main__":
     run()    


