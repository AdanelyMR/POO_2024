#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

num_1=float(input("Ingrese un primer numero : "))
num_2=float(input("Ingrese un segundo numero : "))

suma=num_1 + num_2
resta=num_1 - num_2
multiplicacion=num_1 * num_2


if num_2 != 0:
    division = num_1 / num_2
else:
    division = "No se puede dividir entre cero"
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")