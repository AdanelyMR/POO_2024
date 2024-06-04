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


#Ejemplo 2, Crear una lista de palabras y posterigormente buscar la coincidencia de una palabra

palabras=["hola","como","estas","ok"]
palabras_buscar=input("Ingrese las palabras a buscar: ")
for i==palabras_buscar:
    

print("Encontre la palabra en la posición", )