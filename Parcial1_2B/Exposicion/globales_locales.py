def suma(a, b):
    resultado = a + b
    print(f"Suma: {resultado}")
    return resultado

def resta(a, b):
    resultado = a - b
    print(f"Resta: {resultado}")
    return resultado

suma(5, 3)
resta(5, 3)
print(f"Intentando acceder a 'resultado' fuera de las funciones: {resultado}")
