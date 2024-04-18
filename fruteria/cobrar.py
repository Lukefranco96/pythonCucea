 
import funcionesFruta
import mysql.connector

# conexion a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="",
    database="mercado"
)


# #codigo Omar

#crear menu y ligar todos los precios hasta que funcione



while True:
    fruta = funcionesFruta.menu()
    cantFruta = int(input("ingresa el numero de piezas a comprar: "))
    
    if cantFruta == 0:
        print('fin del programa pusiste 0')
        break
    else:
        funcionesFruta.descuento(fruta, cantFruta)
        seguir = input("quieres seguir? (si/no) : ")
        
        if seguir.lower() == "si":
            funcionesFruta.limpiar_pantalla()
        else: 
            funcionesFruta.limpiar_pantalla()
        
         
