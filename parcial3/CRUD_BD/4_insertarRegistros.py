 #1er forma

# import conexionBD # (Se utiliza cuando se manda a llamar módulos o funciones)

# micursor=conexionBD.conexion.cursor() 

# sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. centro', '6181234567')"
# micursor.execute(sql)
# #Es necesario para que al final se complete el Execute(sql) y finalice la consulta SQL
# conexionBD.conexion.commit() 

# if micursor:
#     print(f"Registro Insertado con Exito")


#2da forma

from conexionBD import * #Incluir un paquete los archivos que quiero mostrar (Cuando se usan paquetes)

try:
    micursor=conexion.cursor()

    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. centro', '6181234567')"
    micursor.execute(sql)
    #Es necesario para que al final se complete el Execute(sql) y finalice la consulta SQL
    conexion.commit() 
except:
    print(f"Ocurrió un problema con el servidor... por favor intentalo más tarde...")
else:
    print(f"Registro Insertado Correctamente")
