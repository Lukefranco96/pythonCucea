from rembg import remove
from PIL import Image
import io


inputImage = "C:/Users/Dell/OneDrive/Documentos/GitHub/pythonCucea/borrarfondos.py/images.jpeg"
outputImage = "image_sin_fondo2.png"
with open(inputImage, "rb") as input_file:
    inputData = input_file.read()
    outputData = remove(inputData)

with open(outputImage, "wb") as output_file:
    output_file.write(outputData)















# import mysql.connector

# # Conectar a la base de datos
# conexion = mysql.connector.connect(
#     host="207.210.232.53",
#     port="3306",
#     user="ecadvice",
#     password="s1RE791!uq(TcP",
#     database="ecadvice_trento"
# )
# # Crear un cursor para ejecutar consultas SQL
# cursor = conexion.cursor()

# # Ejecutar una consulta para recuperar la URL de la base de datos
# cursor.execute("SELECT url FROM tabla WHERE condicion = valor")

# # Obtener el resultado de la consulta
# resultado = cursor.fetchone()

# # Cerrar el cursor y la conexión
# cursor.close()
# conexion.close()

# # Verificar si se encontró una URL en la base de datos
# if resultado:
#     # La URL está almacenada en la primera columna del resultado
#     url = resultado[0]

#     # Ahora puedes utilizar la URL como parámetro en la solicitud a la API de Google Custom Search
#     # Por ejemplo:
#     custom_search_url = f"https://www.googleapis.com/customsearch/v1?q=query&cx=your_cx&key=your_api_key&imgUrl={url}"
    
#     # Realizar la solicitud a la API de Google Custom Search utilizando la URL recuperada
#     # (Asegúrate de tener tu propia clave de API y el ID de búsqueda personalizado)
#     # ...

# else:
#     print("No se encontró ninguna URL en la base de datos.")











# import mysql.connector
# from rembg import remove
# import requests

# # Realizar solicitud HTTP para obtener los datos de la imagen
# inputUrl = "URL_DE_LA_IMAGEN_AQUÍ"
# response = requests.get(inputUrl)
# response.raise_for_status()

# # Procesar los datos de la imagen con rembg
# outputData = remove(response.content)

# # Conectar a la base de datos MySQL
# mydb = mysql.connector.connect(
#   host="TU_HOST",
#   user="TU_USUARIO",
#   password="TU_CONTRASEÑA",
#   database="NOMBRE_DE_LA_BASE_DE_DATOS"
# )

# # Insertar la imagen procesada en la base de datos
# mycursor = mydb.cursor()
# sql = "INSERT INTO images (name, data) VALUES (%s, %s)"
# val = ("image_sin_fondo.png", outputData)
# mycursor.execute(sql, val)

# # Confirmar la transacción y cerrar la conexión
# mydb.commit()
# mydb.close()




# JUNTE TODO A MI PERSPECTIVA, SI VES EL ERROR EN ALGUN MOMENTO ME DICES, TRATE DE METER LO DE GOOGLE
# import mysql.connector
# import requests
# from rembg import remove

# try:
#     # Realizar solicitud HTTP para obtener los datos de la imagen
#     inputUrl = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS-uY-9spMY5nXgDb0WCSSx3Sq9FF2cWFxtRJwLqsyg7wtzcBhmkqlCQ7fD"
#     response = requests.get(inputUrl)
#     response.raise_for_status()

#     # Procesar los datos de la imagen con rembg
#     outputData = remove(response.content)

#     # Conectar a la base de datos MySQL
#     mydb = mysql.connector.connect(
#         host="207.210.232.53",
#         port=3306,
#         user="ecadvice",
#         password="s1RE791!uq(TcP",
#         database="ecadvice_trento"
#     )

#     # Insertar la imagen procesada en la base de datos
#     mycursor = mydb.cursor()
#     directorio = "/borrarfondos.py"
#     val = ("image_sin_fondo.png", outputData)
#     mycursor.execute(directorio, val)

#     # Confirmar la transacción y cerrar la conexión
#     mydb.commit()
#     mydb.close()

#     print("La imagen se procesó y se insertó en la base de datos correctamente.")
# except Exception as e:
#     print("Error al procesar y almacenar la imagen:", e)