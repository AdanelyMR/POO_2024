from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"

    micursor.execute(sql)
    conexion.commit() #commit solo se utiliza con el insert, delete y update)

except:
    print(f"Ocurrió un problema con el servidor... por favor intentalo más tarde...")
else:
    print("Registro Eliminado Correctamente")