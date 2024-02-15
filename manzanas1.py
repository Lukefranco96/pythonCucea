# api key 0531001f34a5b58b9c0cc8bc
import requests 
# clave de mi api key
API_KEY= '0531001f34a5b58b9c0cc8bc'

# api url base
BASE_URL = f'https://v6.exchangerate-api.com/v6/0531001f34a5b58b9c0cc8bc/latest/MXN'

# realiza solicitud a la api para obtener tasa de cambio
response = requests.get(BASE_URL)
data = response.json()

print(data)

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
    