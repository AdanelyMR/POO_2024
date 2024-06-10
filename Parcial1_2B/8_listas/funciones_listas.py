"""
list (Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los
 valores se hace con un indice numerico

 Nota: sus valores si son modificables

 La lista es una coleccion ordenada y modificable 
 Permite miembros duplicados

 """
 #EJEMPLO 1
 #Crear una lista de numeros e imprimir el contenido

numeros=[23,34]
print(numeros)

#Recorrer la lista con un ciclo for
for i in numeros:
    print(i)

#Recorrer la lista con un ciclo while
i=0
while i<=len(numeros)-1:
    print(numeros[i])
    i+=1

#Ejemplo 2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra
# palabra = ["hola","utd", "como", "estas", "ok", "ok", "naranja"]
# palabra_buscar = input("inserta palabra a buscar: ")

# if palabra_buscar in palabra:
#     for i, p in enumerate(palabra):
#         if p == palabra_buscar:
#             print(f"Encontré la palabra en la posición {i}")
# else:
#     print("No encontré la palabra en la lista")

palabra = ["hola", "utd", "como", "estas", "ok", "naranja"]
palabra_buscar = input("Inserta una palabra a buscar: ")
i = 0
while i < len(palabra):
    if palabra[i] == palabra_buscar:
        print(f"Encontré la palabra en la posición {i}")
        break  
    i += 1
else:
    print("No encontré la palabra en la lista")


#Ejemplo 3 Agregar y eliminar elementos de una lista 
#Os system ("Clear")

numeros=[23,24,23]
print(numeros)

#Agregar un elemento 
numeros.append(100)
print(numeros)
numeros.insert(3,200)
print (numeros)

#Eliminar un elemnto 
numeros.remove(100)#indicar el elemnento a borrar 
print(numeros)
numeros.pop(2)#indicar la posicion del elememto a borrar 
print(numeros)
#Ejemplo 4 Crear una lista multilinea (matriz) para agregar los nombre y los numeros telefonocos 
agenda=(
("carlos", 6181234567),
("Leo", 6671234576),
("Sebastian", 6182341234),
("Pedro", 6171236789)
)
print(agenda)
for i in agenda: 
    print(f"{agenda.index(i)+1}.-{i}")

#Ejemplo 5 Crear un programa que permita gestionar (administrar) peliculas,
#colocar un menu de opciones para agregar, remover, consultar peliculas
#Notas 
#1.-Utilizar funciones y mandar llamar desde otro archivo 
#2.-Utilizar listas para almacenar los nombres de peliculas

# import peliculas_funciones

# def mostrar_menu():
#     print("1. Agregar película")
#     print("2. Remover película")
#     print("3. Consultar películas")
#     print("4. Salir")

import os
import peliculas_funciones


gestion=True
while gestion:
    os.system("cls")
    print("\t\n....::::GESTIÓN DE PELICULAS::::.....\n 1.- AGREGAR\n 2.- REMOVER\n 3.- CONSULTAR\n 4.- BUSCAR\n 5.- SALIR")
    opcion=input("\t Elige una opcion: ").upper()

    if opcion=="1":
        os.system("cls")
        peliculas_funciones.AgregarPeli()

    elif opcion=="2":
        os.system("cls")
        peliculas_funciones.RemovePeli()

    elif opcion=="3":
        os.system("cls")
        peliculas_funciones.ConsultarPeli()

    elif opcion=="4":
        os.system("cls")
        peliculas_funciones.BuscarPeli()

    elif opcion=="5":
        os.system("cls")
        gestion=False
        print("Terminaste la ejecucion del SW")
        peliculas=["El viaje de Chihiro", "El castillo bagabundo", "El secreto mundo de Arrieti"]

import msvcrt
def AgregarPeli():
    movie=input("\t¡AGREGA UNA PELICULA NUEVA! \nIngrese el nombre de la pelicula: ")
    peliculas.append(movie)
    print(f"¡Ha sido agregada {movie} con exito!")
    print("Presione una tecla para continuar......")
    msvcrt.getch()


def RemovePeli():
    print("\t¡ELIMINA UNA PELICULA!")
    print(peliculas)
    movie=input("Ingrese el nombre de la pelicula que desea remover: ")
    i=0
    encontro=False
    while i <= len(peliculas):
       
        if movie in peliculas:
             resp=input(f"Pelicula existente \n ¿Seguro de eliminar {movie}?").upper()
             if resp=="SI":
                 peliculas.remove(movie)
                 print(f"¡La pelicula {movie} ha sido removida con exito!")
                 encontro=True
        i+=1
                
    if not encontro:
         print(f"{movie} no fue encontrado en nuestra lista")

    print("Presione una tecla para continuar......")
    msvcrt.getch()

def ConsultarPeli():
    print("\t¡CONSULTA LA CARTELERA ACTUALIZADA!")
    print(peliculas)
    print("Presione una tecla para continuar......")
    msvcrt.getch()


def BuscarPeli():
    print("\t¡BUSCA UNA PELICULA!")
    movie=input("Ingresa la pelicula a buscar: ")
    
    if movie in peliculas:
        for i, p in enumerate(peliculas):
            if p==movie:
                print(f"La pelicula se encuentra en la posicion {i} de la lista")
        
    else:
        print("No se encontró la pelicula en la lista")

    print("Presione una tecla para continuar......")
    msvcrt.getch()