import os
import requests






# clave de mi api key
API_KEY= '0531001f34a5b58b9c0cc8bc'

# api url base
BASE_URL = f'https://v6.exchangerate-api.com/v6/0531001f34a5b58b9c0cc8bc/latest/MXN'

# realiza solicitud a la api para obtener tasa de cambio
response = requests.get(BASE_URL)
data = response.json()


# obtiene la tasa de cambio de pesos eur a mxn
tasaCambio = data['conversion_rates']['USD']

PRECIOS_FRUTAS={
        1 : 10, #"manzanas"    
        2 : 15, #"peras"
        3 : 89, #"uva"
        4 : 35 #melon
}

def menu():
    frutas = int(input("""Que fruta vas a querer?
                       Manzana=1
                       Peras=2 
                       Uvas=3
                       Melon=4
                       Numero de fruta: """))
    if frutas in PRECIOS_FRUTAS:
        return frutas
    else:
        print ("valor invalido")
        return 0
        

def limpiar_pantalla():
            os.system('cls')

def descuento(frutas, cantFruta):
    precioFruta = PRECIOS_FRUTAS[frutas]
    resultado= cantFruta*precioFruta
    resultadoDollar = round(resultado * tasaCambio, 2)
    resultadoMX= str(resultado)
    resultadoUSD = str(resultadoDollar)
    
    
    
    with open('historial.txt', 'a') as historial:
        if cantFruta == 17:
            totalDeVentaEspecial = resultado * 0.80
            porcentajeEspecial= resultado*0.2
            totalDeVentaEspecialUSD = round(totalDeVentaEspecial * tasaCambio, 2) 
            porcentajeEspecialUSD = round(porcentajeEspecial * tasaCambio, 2)
            resultadoEspecialMX = str(totalDeVentaEspecial)
            resultadoEspecialUSD = str(totalDeVentaEspecialUSD)
            print(f"Por ser cliente especial tu descuento es del 20% y tu total a pagar es: ${totalDeVentaEspecial} con un descuento de ${porcentajeEspecial} o en dollares es de: ${totalDeVentaEspecialUSD} con descuento de ${porcentajeEspecialUSD}")
            historial.write(f'Vendiste ${resultadoEspecialMX} pesos mexicanos y tu venta en dollares fue de ${resultadoEspecialUSD}\n haciendo un decsuento del 20% en la compra\n')
            
        elif cantFruta >=10   :
            totalDeVenta =  resultado * 0.9
            porcentajeDescontado = resultado * 0.10
            totalDeVentaUSD = round(totalDeVenta * tasaCambio, 2)
            porcentajeDescontadoUSD = round(porcentajeDescontado * tasaCambio, 2)
            resultadoDescMX = str(totalDeVenta)
            resultadoDescUSD = str(totalDeVentaUSD)
            print (f"tu descuento fue del ${porcentajeDescontado} y el total va a ser ${ totalDeVenta} o en dollares es de: ${totalDeVentaUSD} con descuento de ${porcentajeDescontadoUSD}") 
            historial.write(f'Vendiste {resultadoDescMX} pesos mexicanos y tu venta en dollares fue de {resultadoDescUSD}\n haciendo un decsuento del 10% en la compra\n')
        else :
            print(f"Tu cantidad a pagar es de ${resultadoMX} pesos  o ${resultadoUSD}  dollares$ya que no fueron mas de 10 pz. y el descuento solo aplica arriba de 10pz")  
        # escribe el resultado en el historial.tx

        historial.write(f'Vendiste ${resultadoMX} pesos mexicanos y tu venta en dollares fue de ${resultadoUSD}\n')

    print(f'Vendiste ${resultadoMX} pesos mexicanos y tu venta en dollares fue de ${resultadoUSD}\n')





