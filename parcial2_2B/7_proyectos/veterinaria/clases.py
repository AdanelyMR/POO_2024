class Servicio:
    def __init__(self, nombre_servicio, descripcion, precio):
        self.nombre_servicio = nombre_servicio
        self.descripcion = descripcion
        self.precio = precio

    def get_precio(self):
        return self.precio

    def datos_servicio(self):
        return f"Servicio: {self.nombre_servicio}, Descripción: {self.descripcion}, Precio: {self.precio}"


class Empleado:
    def __init__(self, id_empleado, nombre_empleado, telefono, cargo):
        self.id_empleado = id_empleado
        self.nombre_empleado = nombre_empleado
        self.telefono = telefono
        self.cargo = cargo

    def atender_cita(self):
        pass  # Lógica para atender una cita

    def obtener_datos(self):
        return f"ID: {self.id_empleado}, Nombre: {self.nombre_empleado}, Teléfono: {self.telefono}, Cargo: {self.cargo}"


class Cliente:
    def __init__(self, id_cliente, correo, telefono, direccion):
        self.id_cliente = id_cliente
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def registrar_cliente(self):
        pass  # Lógica para registrar un cliente


class Animal:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad

    def datos_cliente(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Raza: {self.raza}, Edad: {self.edad}"


class Cita:
    def __init__(self, fecha, hora, num_cita):
        self.fecha = fecha
        self.hora = hora
        self.num_cita = num_cita

    def agregar_cita(self):
        pass 


class Veterinaria:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.clientes = []
        self.empleados = []
        self.citas = []
        self.servicios = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cita(self, cita):
        self.citas.append(cita)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def mostrar_informacion(self):
        return f"Veterinaria: {self.nombre}, Dirección: {self.direccion}, Clientes: {len(self.clientes)}, Empleados: {len(self.empleados)}, Citas: {len(self.citas)}, Servicios: {len(self.servicios)}"
