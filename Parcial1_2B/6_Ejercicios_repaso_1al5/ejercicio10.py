#Crear un programa que solicite la calificacion de 15 alumnos 
#e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

reprobados=0
aprobados=0
for contador in range(1,16):

     calif=float(input(f"Ingrese la calificación del alumno {contador} (1 a 100): "))
     
     if calif<=79:
        reprobados+=1
     if calif>=80:
        aprobados+=1

print(f"{aprobados} alumnos aprobados en total")
print(f"{reprobados} alumnos reprobados en total")