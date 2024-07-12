class Lectores:

    def __init__(nombre, direccion,tel,reservar,entregar):
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel
        self.reservar=reservar
        self.entregar=entregar

    def getNombre(self):
      return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getDireccion(self):
      return self.direccion

    def setDireccion(self, direccion):
        self.direccion=direccion

    def getTel(self):
      return self.tel

    def setTel(self,tel):
        self.tel=tel

    def getReservar(self):
      return self.reservar

    def setReservar(self,reservar):
        self.reservar=reservar

    def getEntregar(self):
      return self.entregar

    def setEntregar(self, entregar):
        self.entregar=entregar
    
    def getInfo(self):
       print(f"Nombre: {self.getNombre()},\n Direccion: {self.getDireccion()} \n Telefono: {self.getTelefono()} Reserva {self.getReservar()} y entrega {self.getEntregar()} ")


class Estudiantes(Lectores):
   def __init__(nombre, direccion,tel,reservar,entregar,carrera,matricula):
      super().__init__(nombre, direccion,tel,reservar,entregar)
      self._carrera=carrera
      self._matricula=matricula
    
   def getCarrera(self):
      return self._carrera
   
   def setCarrera(self,carrera):
      self._carrera=carrera

   def getMatricula(self):
      return self._matricula

   def setMatricula(self, matricula):
        self._Matricula=matricula
    
   def getInfo(self):
       print(f"Nombre: {self.getNombre()},\n Direccion: {self.getDireccion()} \n Telefono: {self.getTelefono()}\n Reserva {self.getReservar()} y entrega {self.getEntregar()}\nLa carrera del alumno es:{self.getCarrera()}\n La matricula del alumno es:{self.getMatricula()}  ")
    
class Docentes(Lectores):
   def __init__(nombre, direccion,tel,reservar,entregar,modalidad,num_empleado):
      super().__init__(nombre, direccion,tel,reservar,entregar)
      self.__modalidad=num_empleado
      self.__Num_empleado=num_empleado
    
   def getModalidad(self):
      return self.__modalidad
   
   def setModalidad(self,modalidad):
      self.__modalidad=modalidad

   def getNum_empleado(self):
      return self.__num_empleado

   def setNum_empleado(self, num_empleado):
        self.__num_empleado=num_empleado
    
   def getInfo(self):
       print(f"Nombre: {self.getNombre()},\n Direccion: {self.getDireccion()} \n Telefono: {self.getTelefono()}\n Reserva {self.getReservar()} y entrega {self.getEntregar()}\nLa modalidad del maestro es:{self.getModalidad()}\n El numero de empleado es:{self.getNum_empleado()}  ")
    
    
    