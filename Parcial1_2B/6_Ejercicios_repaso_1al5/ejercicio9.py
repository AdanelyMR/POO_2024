#Hacer un programa que solicite numeros indefinidamente 
#hasta que se introduzca el 111 y salir del programa

def main():
    numero = 0
    while numero != 111:
        numero = int(input("Ingresa un número: "))
        if numero==111:
            print("Se ha ingresado 111.")

if __name__ == "__main__":
    main()
