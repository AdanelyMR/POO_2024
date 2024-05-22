#Mostrar todas las tablas del 1 al 10. 
#Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10


multi=0
numero=int(input("ingrese un numero: "))
for i in range(1,11):
    multi=numero*i
    print(f"{numero} X {i}={multi}")