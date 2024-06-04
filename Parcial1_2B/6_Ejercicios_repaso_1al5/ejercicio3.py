# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

multi=0
numero=int(input("ingrese un numero: "))
for numero in range(1,60):
    multi=numero*numero
    print(multi)

while numero<=60:
    multi=numero*numero
    print("El cuadrado del numero es: ",multi)
