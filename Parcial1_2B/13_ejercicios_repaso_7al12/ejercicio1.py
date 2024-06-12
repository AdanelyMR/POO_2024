#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

#  a.- 
numeros = [2,1,3,5,6,8,4,7]

print("Elementos de la lista:")
for numero in numeros:
    print(numero)
    
#  b.-
def lista_a_string(lista):
    return " ".join(str(numero) for numero in lista)

numeros = [2,1,3,5,6,8,4,7]
resultado = lista_a_string(numeros)
print("Lista como string:", resultado)

#  c.-
numeros = [2,1,3,5,6,8,4,7]
numeros.sort()

print("Lista ordenada:")
for numero in numeros:
    print(numero)
    #  d.-
numeros = [2,1,3,5,6,8,4,7]
longitud = len(numeros)
print("Longitud de la lista:", longitud)

#  e.-
try:
    elemento_buscado = int(input("Ingresa un número para buscar en la lista: "))
    if elemento_buscado in numeros:
        print(f"{elemento_buscado} está en la lista.")
    else:
        print(f"{elemento_buscado} no está en la lista.")
except ValueError:
    print("Error: Ingresa un número válido.")
