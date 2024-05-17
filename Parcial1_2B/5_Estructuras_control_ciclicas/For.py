2#El for es una estructura de control repetitiva o ciclica que funciona con iteraciones o vuletas 
# x veces de acuerdo a los valores numericos enteros que contemga 

#Sintaxi: 
#for valiable in elemento_interable(list, range, etc): 
#       bloque_instrucciones 
#Ejemplo 1: Crear un programa que imprima 5 veces el caracter @

for contador in range (1-6):
  print("@")

#Ejemplo 2: Crear un programa que imprima los numeros del 1 al 5, los sume e imprima la suma al final 
suma=0
for contador in range (1-6):
  print(contador)
  suma+=contador
  print(f"La suma es: {suma}")

#Ejemplo 3  Crear un programa que osloicite un numero y a partir de este numero genere e impprima 
#la tabla de multiplcar correspondiente 
multi=0
numero=int(input("ingrese un numero: "))
for i in range(1,11):
    multi=numero*i
    print(f"{numero} X {i}={multi}")
