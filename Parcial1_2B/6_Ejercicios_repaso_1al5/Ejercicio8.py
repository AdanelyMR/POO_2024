#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?


x_porc=int(input("Ingrece el porcentaje: "))
num=int(input("Ingrese el numero: "))

print(f"¿Cuanto es el {x_porc} por ciento de {num}?")
porcen=x_porc/100
numf=num*porcen
print(numf)