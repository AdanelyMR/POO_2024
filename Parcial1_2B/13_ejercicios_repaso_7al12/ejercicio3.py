#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir  el contenido de la lista en mayusculas

import os

lista=[]

if not lista:
    print("La lista está Vacia")
    while True:
        lleno=input(" Agrege una palabra para llenarla: ")
        lista.append(lleno)
        resp=input("¿Quieres seguir agregando frases? (si/no): ").strip().lower() #Elimina espacios adicionales, convierte a minusculas
        os.system("cls")
        if  resp=="no":
            print("Ejecucion del SW terminado")
            print(f"\tCONTENIDO DE LA LISTA")
            for x in lista:
                print(x.upper())
            break

else:
     for x in lista:
                print(x.upper())