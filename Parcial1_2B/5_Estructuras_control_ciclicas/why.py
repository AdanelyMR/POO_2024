# El while es una estructura de control repetitiva o ciclica que funciona con iteraciones X veces siempre y cuando la condicion sea "True"

# Sintaxi: 

# while condicion:
#     bloque instrucciones

#Ejemplo 1 Crear un programa que imprima 5 veces el caracter @


contador=1

while contador <=5:
  print("@")
  contador+=1

#Ejemplo 2: Crear un programa que imprima los numeros del 1 al 5, los sume e imprima la suma al final 
contador=1
suma=0
while contador <=5:
  print(contador)
  suma+=contador
  contador+=1
  print(f"La suma es: {suma}")

#Ejemplo 3  Crear un programa que osloicite un numero y a partir de este numero genere e impprima 
#la tabla de multiplcar correspondiente 
multi=0
i=0
numero=int(input("ingrese un numero: "))
while i<=10:
    multi=numero*i
    print(f"{numero} X {i}={multi}")
    i+=1