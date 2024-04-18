import mysql.connector
import usuarioModel 
import connector


def extraerUsuarios():
# conexion a la base de datos
    conn = connector.dbConnection()
    cursor= conn.cursor()
    # Crear un cursor para ejecutar consultas
    
    # Consulta para obtener el resultado como un array
    query = """
    SELECT *
    FROM usuario
    WHERE id_usuario

    """
    
    # Ejecutar consulta
    cursor.execute(query)
    usuarios=[]
    # Obtener el resultado de la consulta como un array
    resultados = cursor.fetchall()

    for fila in resultados:
        usuario = usuarioModel.asignarDatos(fila)
        usuarios.append(usuario)
    
    cursor.close()
    conn.close()
    return usuarios

# Imprimir el resultado como un array
def extraeUsuario(codigo):
    # Establecer la conexión
    # Realizar operaciones en la base de datos
    conn = connector.dbConnection()
    cursor= conn.cursor()
    # Ejemplo de consulta
    cursor.execute(f"SELECT * FROM usuario WHERE id_usuario = {codigo}")
    usuarios = []
    # Obtener los resultados
    resultados = cursor.fetchall()
    # Imprimir los resultados
    for fila in resultados:
        usuario1 = usuarioModel.usuario
        usuario1['id_usuario']=fila[0]
        usuario1['usuario']=fila[1]
        usuario1['correo']=fila[3]
        usuario1['nombre']=fila[4]
        usuario1['apellidoPaterno']=fila[5]
        usuario1['apellidoMaterno']=fila[6]
        usuario1['puesto']=fila[7]
        usuario1['telefono']=fila[8]
        usuarios.append(usuario1)
        del usuario1
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    
    
    return usuarios

datosUsuarios = extraerUsuarios()
print(datosUsuarios)
datosUsuario = extraeUsuario(2)
print(datosUsuario)

