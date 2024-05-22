#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario


num_1=int(input("Ingrese el primer numero: "))
num_2=int(input("ingrese el segundo numero: "))


num_1+=1
for num in range(num_1,num_2):
    if num%2!=0:
        print("Los numeros impares son: ",num)