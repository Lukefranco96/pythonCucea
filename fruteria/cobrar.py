 
import funcionesFruta





# # Solicitar al usuario ingresar el num de manzanas y precio
# numManzanas = int(input("ingresa el numero de manzanaz: "))
# precioManzana = float(input("ingresa el precio de la manzanaz: "))

# # precio en dollars
# precioManzanaUSD = precioManzana * tasaCambio

# # calcula el resultado de total de venta en dls
# resultadoUSD= numManzanas * precioManzanaUSD

# # calcular resultado en pesos mexicanos
# resultado = numManzanas*precioManzana

# # cambiamos los resultados a string para poder insertarlo en el .write
# resultadoMX= str(resultado)
# resultUSD = str(resultadoUSD)

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
        
         
