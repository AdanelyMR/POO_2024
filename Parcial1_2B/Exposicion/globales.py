resultado_global = 0

def suma(a, b):
    global resultado_global
    resultado_global = a + b
    print(f"Suma: {resultado_global}")

def resta(a, b):
    global resultado_global
    resultado_global = a - b
    print(f"Resta: {resultado_global}")

suma(5, 3)
resta(5, 3)

print(f"Resultado global fuera de las funciones: {resultado_global}")
