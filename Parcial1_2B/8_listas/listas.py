#Funciones Listas(mequivoque de carpeta)

paises=["Mexico","Brasil","USA","Japón"]
numeros=[23,100,3.1416,0.100]
varios=["Hola",True,100,10.22]

#Ordenar Paises 
print(paises)
paises.sort()
print(paises)
#Numeros
# print(numeros)
# numeros.sort()
# print(numeros)
#Agregar elementos
print(numeros)
numeros.insert(len(numeros),100)
print(numeros)
numeros.append(100)

#Eliminar elemntos 
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#Buscar dentro de una lista un dato o un valor 
encontrar="Brasil"in paises
print(encontrar) 

#Dar la vuelta a una lista
print(varios)
varios.reverse()
print(varios)

#Unir listas 
print(paises)
paises.extend(numeros)
print(paises)

#Vaciar una lista
print(varios)
varios.clear()
print(varios)
