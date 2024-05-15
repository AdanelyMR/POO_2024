#Convertir los tipos de datos

#Nota: Solo es posible en una concatenacion concatenaar entre tipos de datos iguales 

texto="Soy una cadena "
numero=23

print(texto)
print(numero)

print(texto+"y soy una cadena2")
print(numero+34)


#Convertir un tipo de datos int a str
numero_str=str(numero)
print(texto+" "+numero_str)

print(texto+" "+str(numero)) #ES LA MAS COMUN PARA MOSTRAR UNA CADENA CON UN NUMERO 

#Convertir un Str a Int 
n1=33

suma=int('23')+n1
print(suma)
print("suma: "+str(suma))


#Convertir un FLOAT a INT
n1=33
n2=int(33.10)
suma=n1+n2
print(suma)