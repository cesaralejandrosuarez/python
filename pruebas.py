#ejericio numero 1:
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")

#ejericio numero 2:
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
SaludoMundial=("¡Hola Mundo!")
print(SaludoMundial)

#ejericio numero 3:
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre= input("indica tu nombre: ")
print(f"hola, {nombre}")


#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
operacion_matematica= ((3+2)/(2*5))**2
print(operacion_matematica)


#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horalaborada=int(input("cuantas horas laboro: "))
valor= horalaborada*4000
print(f"cada hora laborada cuesta 4000, tu tienes: {horalaborada} horas laboradas, tu pago es de :{valor}")


#Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta  n . La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma:
n= int(input("escriba un numero:"))
suma= n*(n+1)/2
print(f"la suma de los numeros de 1 a {n} es: {suma}") 


#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.








def imprimeunnombre(name):
   print(name)

imprimeunnombre("HOLA MUNDO")

imprimeunnombre("hola soy cesar alejandro suarez")
