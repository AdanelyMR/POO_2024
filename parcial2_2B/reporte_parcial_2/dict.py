class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._jornada = ''

    def establecer_jornada(self, jornada):
        self._jornada = jornada

    def getInfo(self):
        return f"Nombre: {self._nombre}\n Edad: {self._edad}\n Jornada: {self._jornada}"


class Jornada:
    def __init__(self, tipo, horas):
        self.tipo = tipo
        self.horas = horas

    def calcular_horas_extra(self, horas_extra):
        if horas_extra >= 10:
            resultado = horas_extra - 9
            resultado2 = horas_extra - resultado
            return (self.horas / 2) * resultado2 + (self.horas * 3 * resultado)
        else:
            return (self.horas / 2) * horas_extra

    def __str__(self):
        return f"\nTipo de jornada: {self.tipo}\n Horas extra laboradas: {self.horas}\n"


class Bonos:
    def __init__(self, monto):
        self.monto = monto

    def __str__(self):
        return f"Monto del bono: ${self.monto}\n"


class Empleado(Persona):
    def __init__(self, nombre, edad, jornada, bono):
        super().__init__(nombre, edad)
        self.jornada = jornada
        self.bono = bono
        self._dias_chambeados = 0
        self._horas_extra = 0
        self._sueldo_semanal = 0
        self._descanso_sem = 0
        self._pago_prima_dominical = 0
        self._horas_extra_pagar = 0

    def calcular_sueldo_semanal(self, sueldo_dia, prima_dominical):
        salario = sueldo_dia * self._dias_chambeados

        if self._horas_extra > 0:
            self._horas_extra_pagar = self.jornada.calcular_horas_extra(self._horas_extra)

        self._pago_prima_dominical = sueldo_dia * prima_dominical
        self._descanso_sem = sueldo_dia * 2
        self._sueldo_semanal = salario + self._descanso_sem + self._horas_extra_pagar + self._pago_prima_dominical + self.bono.monto

    def getInfo(self):
        return (f"Empleado: {self._nombre}\n Edad: {self._edad}\n {self.jornada}\n "
                f"Sueldo Semanal: ${self._sueldo_semanal}\n {self.bono}")


class CalculadoraSalario:
    def __init__(self, sueldo_dia, prima_dominical):
        self._sueldo_dia = sueldo_dia
        self._prima_dominical = prima_dominical
        self._empleados = []

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def mostrar_informacion(self):
        for empleado in self._empleados:
            empleado.calcular_sueldo_semanal(self._sueldo_dia, self._prima_dominical)
            print(empleado.getInfo())





