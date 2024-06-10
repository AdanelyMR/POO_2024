#Los errores de ejecucion en un lenguaje de programacion se presentan cuando existe una anomalia o error dentro de la ejcucion del codigo lo cual provoca que se detenga la ejecucion del mismo SW con el control y manejo de excepciones sera posible minimizar o editar la interrupcion del programa debido a una excepcion

#Ejemplo 1 cuando una variable no se genera 

# try:
#     nombre=input("Introduce el nombre completo de una persona: ")

#     if len(nombre)>0:

#      nombre_usuario="El nombre del usuario es: "+nombre

#      print(nombre_usuario)
# except:
#    print("Es necesario introducir un nombre de usuario... verifica por favor")

# x=3+4
# print("El valor de x es: "+str(x))

#Ejemplo 2 cuando se solicita un numero y se integra otra cosa
# try:
#  numero=int(input("Ingrese un  numero entero: "))
#  if numero>0:
#    print("Soy un numero entero positivo")
#  elif numero==0:
#    print("Soy un numero entero neutro")
#  else: 
#    print("Soy un numero entero negativo")
# except ValueError:
#  print("Introduce un valor de un numeor entero")

 #Ejemplo 3 Genera multiples excepciones 

try:
 numero=int(input("Introduzca un  numero: "))
 print("El cuadrado del numero es:"+str (numero*numero))
except ValueError:
 print("Introduce un valor numerico entero")
except TypeError:
 print("Se debe convertir el numero a entero")
else:
 print("No se presentaron errores de ejecucucion")
finally#Permigte que lo que se ingrese debajo de el se ejecute siempre no importa si tiene probleas o no
 print("Termine la ejecucion")

