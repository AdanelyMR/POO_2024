#Registros o tupla
from conexionBD import *

try:
  micursor=conexion.cursor()

  sql="select nombre,direccion,tel from clientes"
  micursor.execute(sql)
  resultado=micursor.fetchall() #fetchall toma las tupla y las manda a resultado (Arreglo asosiativo = Lista)

  if len(resultado)>0:
      print(f"Registros de la tabla: {len(resultado)}")
      for x in resultado:
        print(x)
except:
    print(f"Ocurrió un problema con el servidor... por favor intentalo más tarde...")
else:
    print(f"Registro Insertado Correctamente")