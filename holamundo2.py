# api key 1715c195a066cbdf034dbe96b257f611
import requests 
# clave de mi api key
API_KEY= '1715c195a066cbdf034dbe96b257f611'

# api url base
BASE_URL = f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}'

# realiza solicitud a la api para obtener tasa de cambio
response = requests.get(BASE_URL)
data = response.json()

print(data)