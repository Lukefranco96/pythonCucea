import mysql.connector


def dbConnection():
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="",
        database="mercado"
    )
        return conexion
def dbClose(cursor,conexion):
    cursor.close()
    conexion.close()
    
