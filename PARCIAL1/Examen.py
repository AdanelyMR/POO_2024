#Realizar un programa en python que solicite
#nombre del tranajador
#Horas trabajadas
#Dias trabajados 
#Sueldo por hora


sueldo=300
trabajadores=0
while pregunta!="SI":
      nombre=input("ingrese el nombre del trabajador: ")
horas_trabajadas=int(input("ingrese las horas trabajadas: "))
dias_trabajados=int(input("ingrese los dias trabajados: "))
sueldo_hora=int(input("ingrese el sueldo por hora: "))

sueldo_hora=sueldo*horas_trabajadas
sueldo_semana=sueldo_hora*dias_trabajados
sueldo_mes=sueldo_semana*4

if sueldo_mes <=10000:
    print("Obrero tipo A")
elif sueldo_mes >10000 and sueldo_mes< 15000:
        print("Obrero tipo B")
else:
      print("sin categoria")

pregunta=(input("¿Deseas otra captura?"))
pregunta=input()
print(f" el sueldo de todos los trabajadores es:{trabajadores} ")
      
acumulador=+trabajadores

           
