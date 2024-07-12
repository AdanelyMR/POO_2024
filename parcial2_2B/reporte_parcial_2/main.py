from dict import *
print(".::::::::::Salario semanal de los empleados YAZAKI::::::::::.")
print(" ")

jornada_diurna = Jornada('Diurna', 8)
jornada_mixta = Jornada('Mixta', 5)
jornada_nocturna = Jornada('Nocturna', 7)


bono_empleado1 = Bonos(200)
bono_empleado2 = Bonos(150)

empleado1 = Empleado("Pedro Chacón", 30, jornada_diurna, bono_empleado1)
empleado1.establecer_jornada('a')
empleado1._dias_chambeados = 5
empleado1._horas_extra = 12

empleado2 = Empleado("Arturo Salas", 25, jornada_mixta, bono_empleado2)
empleado2.establecer_jornada('b')
empleado2._dias_chambeados = 6
empleado2._horas_extra = 8


calculadora = CalculadoraSalario(sueldo_dia=248.93, prima_dominical=0.25)

calculadora.agregar_empleado(empleado1)
calculadora.agregar_empleado(empleado2)

calculadora.mostrar_informacion()


