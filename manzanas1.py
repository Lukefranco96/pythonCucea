# api key 1715c195a066cbdf034dbe96b257f611
import requests 
# clave de mi api key
API_KEY= '1715c195a066cbdf034dbe96b257f611'

# api url base
BASE_URL = f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}'

response = requests.get(BASE_URL)
data = response.json()

with open('historial.txt', 'a') as historial:
    numManzanas = int(input("ingresa el numero de manzanaz: "))
    precioManzana = int(input("ingresa el precio de la manzanaz: "))
    resultado = numManzanas*precioManzana
    resultadoStr= str(resultado)
    historial.write(f'Vendiste {resultadoStr} pesos\n')
    