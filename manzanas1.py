# api key 0531001f34a5b58b9c0cc8bc
import requests 

# clave de mi api key
API_KEY= '0531001f34a5b58b9c0cc8bc'

# api url base
BASE_URL = f'https://v6.exchangerate-api.com/v6/0531001f34a5b58b9c0cc8bc/latest/MXN'

# realiza solicitud a la api para obtener tasa de cambio
response = requests.get(BASE_URL)
data = response.json()

# print(data)

# obtiene la tasa de cambio de pesos eur a mxn
tasaCambio = data['conversion_rates']['USD']
# obtiene la tasa de cambio de EUR a pesos

# Solicitar al usuario ingresar el num de manzanas y precio
numManzanas = int(input("ingresa el numero de manzanaz: "))
precioManzana = float(input("ingresa el precio de la manzanaz: "))

# precio en dollars
precioManzanaUSD = precioManzana * tasaCambio

# calcula el resultado de total de venta en dls
resultadoUSD= numManzanas * precioManzanaUSD

# calcular resultado en pesos mexicanos
resultado = numManzanas*precioManzana

# cambiamos los resultados a string para poder insertarlo en el .write
resultadoMX= str(resultado)
resultUSD = str(resultadoUSD)

# escribe el resultado en el historial.tx
with open('historial.txt', 'a') as historial:
    historial.write(f'Vendiste {resultadoMX} pesos mexicanos y tu venta en dollares fue de {resultadoUSD}\n')

print(f'Vendiste {resultadoMX} pesos mexicanos y tu venta en dollares fue de {resultadoUSD}\n')
#codigo Omar



while True:
    numManzanas = int(input("ingresa el numero de manzanaz: "))
    precioManzana = float(input("ingresa el precio de la manzanaz: "))
    if numManzanas == 0:
        print('fin del programa pusiste 0')
        break
    else:
        descuento()
        seguir = input("quieres seguir? : ")
        
        if seguir == "si":
            limpiar_pantalla()
        else: 
            limpiar_pantalla()
        
         

# Parte 1
# convertir el descuento en funcion




# parte 2 limpiar pantalla



# Llamar a la función para limpiar la pantalla





#codigo efrain

# if numManzanas==17:
#     porcentajeDescontado= resultado*.8
#     print(f"por ser cliente especial este es el total a pagar {porcentajeDescontado}")
# elif numManzanas>=10:
#     totalDeVenta = resultado *.9
#     porcentajeDescontado=resultado*.1
#     print(f"descuento fue de {porcentajeDescontado} total {totalDeVenta}")
# else:
#     print(f"no hay descuento")
 
 #crear un programa que m diga si un año es bisisesto, tiene que ser divisible entre 4 pero no entre 100 ssolo con la excepcion que sea 400
#  hacerlo con operadores ternarios



# while
# tabla=13
# multi=0

# while multi<=1000:
#     print (f'{tabla}*{multi}= {tabla*multi}')
#     multi += 1



# numero1=  int(input("ingresa el numero 1: "))
# numero2= int(input ("ingresa el numero 2: "))
# rango= range(numero1,numero2)
# for numero in rango:
#     if numero%2==0:
#         print (f"numero par {numero}")
#     else :
#         print(f"numero imprar{numero}")