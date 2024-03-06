 
import funcionesFruta

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
        
         
