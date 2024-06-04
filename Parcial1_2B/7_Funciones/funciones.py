#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como 
#un programa mas pequeñp que cumple una funcion especifica. La funcion se puede reutilizar con 
#el simle hecho de imvocarla es decir mandarla a llamar

#sintaxix:

#def nombredeMifuncion(parametros):
#   bloque o conjunto de instrucciones 

#nombredeMifuncion(parametros):

#Las funciones pueden ser de 4 tipos 
#1.- Funcion que no recibe parametros y no regresa valor 
#2.- Funcion que no recibe parametros y regresa valor 
#3.- Funcion recibe parametros y no regresa valor 
#4.- Funcion recibe parametros y regresa valor 


#Crear una funcion para imprimir nombres de personas
#            1.- Funcion que no recibe parametros y no regresa valor 

def solicitarNombres():
    nombre=input("Ingresa el nombre completo de una persona: ")

solicitarNombres()

#Ejemplo 2 Crear una funcion que realice una sumatoria de dos numeros
#            1.- Funcion que no recibe parametros y no regresa valor 

def suma():
    n1=int(input("Numero 1: "))
    n2=int(input("Numero 2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()

#Ejemplo 3 Sumar dos numeros
#2.- Funcion que no recibe parametros y regresa valor

def suma():
    n1=int(input("Numero 1: "))
    n2=int(input("Numero 2: "))
    suma=n1+n2
    return suma

suma()

resultado_suma=suma()
print("La suma es: {resultado_suma}")


#Ejemplo 4 Sumar dos numeros
#2.- Funcion que no recibe parametros y no regresa valor

def suma(n1, n2):
    suma=n1+n2
    print("La suma es: {suma}")


n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
suma(n1,n2)

#Ejemplo 5 Sumar dos numeros
#2.- Funcion que recibe parametros y  regresa valor
def suma(n1, n2):
    suma=n1+n2
    return suma 

n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
resultado_suma=suma(n1,n2)
suma(n1,n2)
print(f"La suma es: {resultado_suma}")

print (f"{n1}+{n2}= {resultado_suma}")

#Crear un programa que solicite a traves de una funvion la siguienre infotmacion
#Nombre del pacuente
#Edad
#Estatura
#Tipo de sangra 
#Utilizar los cuatro tipo de funciones

def solicitarEdad():
    edad=input("Ingresa la edad: ")

solicitarEdad()
def solicitarEstatura():
    estatura=input("Ingresa la Estatura: ")

solicitarTipodeSangre2()
def solicitarEdad():
    tipo_sangre=input("Ingrese el tipo de sangre: ")

solicitarTipodeSangre2()


#Funcion tien parametros y no regresa valor 
def solicitarPaciente3(nom,ed,est,sangre):
    print (f,"Nombre del paciente {nombre} /n")