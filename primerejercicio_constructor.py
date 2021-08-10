# siempre se crea primero la clase  
class Fraccion: 
 num=2  
 den=3 
#el metodo constructor  Su función es inicializar el objeto 
 def __init__(self): 
     
     print("hola nuevamente soy el constructor") 
     print(self.num) 
 #un metodo que solo impreme dentro  del constructor       
 def imprime(self): 
    print("hola yo soy la impresora")  
#la clase main 
def main( ):  
     #aca se esta llamado lo que hace en el constructor  
     #este primero se llama en automatico 
     a=Fraccion() 
     #este si tocoo construirlo 
     a.imprime() 
        
if __name__== "__main__": 
       main()