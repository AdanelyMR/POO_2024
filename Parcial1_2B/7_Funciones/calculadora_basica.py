#Crear una caluculadora que ayude a hacer la operacion que se solicite 
import os
os.system("clear")
opcion=True
while opcion:
 print ("\n\t..::: CALCULADORA BASICA:::.\n 1.-Suma \n 2.-Resta \n 3.-Multiplicacion \n 4.-División\n 5.-Salir")
 opcion=input("\t Elige una opcion: ").upper()

 if opcion=="1" or opcion=="+" or opcion=="Suma":
    n1=int(input(" Numero #1: "))
    n2=int(input(" Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
 elif opcion=="1" or opcion=="-" or opcion=="Resta":
    n1=int(input(" Numero #1: "))
    n2=int(input(" Numero #2: "))
    resta=n1-n2
    print(f"{n1}-{n2}={resta}")
 elif opcion=="1" or opcion=="-" or opcion=="Multiplicacion":
    n1=int(input(" Numero #1: "))
    n2=int(input(" Numero #2: "))
    multiplicacion=n1*n2
    print(f"{n1}*{n2}={multiplicacion}")
 elif opcion=="1" or opcion=="/" or opcion=="Division":
    n1=int(input(" Numero #1: "))
    n2=int(input(" Numero #2: "))
    division=n1/n2
    print(f"{n1}/{n2}={division}")
 else:
    print(" Terminaste la ejecucion del SW")
    opcion=False
def solicitarNumeros():
  global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))
  

def operacionAritmetica(num1,num2,opcion):  
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
     return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
     return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
     return f"{n1}/{n2}={n1/n2}"  

    
opcion=True    
while opcion:
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()
 if opcion!="5":
   solicitarNumeros()
   print(operacionAritmetica(n1,n2,opcion))
 else:  
     opcion=False    
     print("Terminaste la ejecucion del SW")

#Funcion dentro de una clase es un metodo

