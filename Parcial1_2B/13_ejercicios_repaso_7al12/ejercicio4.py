#Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

frutas=["Uvas", "Fresas", "Guayabas"]
frase="Sentado debajo de un arbol, sentado en un arbol de Uvas "
num=100
comer=True

def mensaje(variable):
    if isinstance(variable, list):  #isinstance determina el valor de la variable 
        print(f"{variable} Esta es una lista.")
    elif isinstance(variable, str):
        print(f"{variable} Esta es una cadena.")
    elif isinstance(variable, int):
        print(f"{variable} Este es un entero.")
    elif isinstance(variable, bool):
        print(f"{variable} Este es un valor lógico.")
    else:
        print("Tipo de dato desconocido.")


mensaje(frutas)
mensaje(frase)
mensaje(num)
mensaje(comer)