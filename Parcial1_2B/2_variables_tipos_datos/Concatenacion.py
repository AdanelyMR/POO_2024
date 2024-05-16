#Formas de concatenar en python 

nombre="Adanely Martinez Ramos"
especialidad="Area de software multiplataforma"
carrera="Ingenieria en Gestion y Desarrollo de Software"

#Primer forma 
print("Mi nombre es "+nombre+"estoy en la especialidad de "+especialidad+"y estudio la carrera de "+carrera)

print("\n")

#segunda forma
print("Mi nombre es ",nombre,"estoy en la especialidad de ",especialidad,"y estudio la carrera de ",carrera)

print("\n")

#Tercera forma MAS COMUN EN PYTHON 
print(f"Mi nombre es,{nombre},estoy en la especialidad de ,{especialidad},y estudio la carrera de,{carrera}")

print("\n")

#Cuarta forma 
print("Mi nombre es,{},estoy en la especialidad de,{},y estudio la carrera de ,{}".format(nombre,especialidad, carrera))

print("\n")

#Quinta forma 
print('Mi nombre es'+nombre+'estoy en la especialidad de'+especialidad+'y estudio la carrera de '+carrera)

