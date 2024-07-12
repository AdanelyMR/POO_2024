from datetime import date, time
from clases import Veterinaria, Servicio, Empleado, Cliente, Animal, Cita

# Crear una instancia de la veterinaria
clases = Veterinaria("Veterinaria Los Animales", "123 Calle villas")

# Crear y agregar un servicio
servicio = Servicio("Consulta", "Consulta general para mascotas", 50.0)
clases.agregar_servicio(servicio)

# Crear y agregar un empleado
empleado = Empleado(1, "Juan Pérez", "618-234-1234", "Veterinario")
clases.agregar_empleado(empleado)

# Crear y agregar un cliente
cliente = Cliente(1, "cliente@gmail.com", "618-555-5678", "123 Calle Matamoros")
clases.agregar_cliente(cliente)

# Crear y agregar una mascota para el cliente
mascota = Animal("Firulais", "Perro", "chihuahua", 5)
cliente.registrar_mascota(mascota)

# Crear y agregar una cita
cita = Cita(date.today(), time(10, 0), 1)
clases.agregar_cita(cita)

# Mostrar información de la veterinaria
print(clases.mostrar_informacion())
