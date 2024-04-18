# curp
import datetime

def curpGenerada(info):
    fechaDeNacimiento = info['fechaDeNacimiento'].strftime("%y%m%d")
    
    primerApellido = info['pApellido']
    primeraLetraApellido = primerApellido[0]
    apellidoSinPrimeraLetra = primerApellido[1:]
    
    segundaVocalApellido = ''
    for letra in apellidoSinPrimeraLetra:
        if letra in 'AEIOUaeiou':
            segundaVocalApellido = letra
            break
    print(segundaVocalApellido)
    valorPrimerVocal = segundaVocalApellido
            
    segundoApellido = info.get('sApellido', '')
    primeraLetraSegundoApellido = segundoApellido[0] if segundoApellido else 'X'
    
    nombreCompleto = info['nombre']
    primeraLetraNombre = nombreCompleto[0]
    
    letraSexo = 'H' if info['sexo'] == 'Hombre' else 'M'
        
    curp = (primeraLetraApellido + valorPrimerVocal + primeraLetraSegundoApellido +
            primeraLetraNombre + fechaDeNacimiento + letraSexo)
    curp = curp.upper()
    return curp
    
# Ejemplo de uso
OMAR = {
    "nombre" : "Jorge Omar",
    "pApellido" : "Aguilar",
    "sApellido" : "Franco",
    "fechaDeNacimiento" : datetime.datetime(1996, 10, 1),
    "sexo" : 'Hombre'
}

DIEGO={
    "nombre": "Diego Giovanni",
    "pApellido": "Arroyo",
    "sApellido": "Pesqueda",
    "fechaDeNacimiento": datetime.datetime(2002, 9, 19),
    "sexo": "Hombre"
}

print(curpGenerada(OMAR))
print(curpGenerada(DIEGO))




# pedir 10 calificaciones de alumnos y mostrar el promedio de los 10


# palindromas

# revisar cuantas veces se repite una palabra  diccionarios con listas hashmaps
# def identificador (oracion):
#     for 'cion' in oracion:
#         if 
        
        
        
# revisar si es pangrams
def detectorPalindromos(cadena):
    #quitamos espacios
    cadena= cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

cadena1 = "Anita lava la tina"
cadena2 = "Coca Cola"
print (detectorPalindromos(cadena1))
print(detectorPalindromos(cadena2))
# oracle

# ver si las siguientes palabras se tienen en comun ya sea de derecha a izq o de izq a derecha


# hulk
# monthulk

# rapid
# forgett

# coder
# redocalib
palabra1 = "monthulk"
palabra2= "forgett"
palabra3= "redocalib"


if "hulk" in palabra1:
    print ("si anda aqui ")
else:
    print("no anda aca ")
    
if "rapid" in palabra2:
    print ("si aparece aqui")
else: 
    print("no anda aca la repelotuda")

if "coder" in palabra3:
    print("si anda aqui")
elif "coder"in palabra3[::-1]:
    print ("eres crack papirrin")
else: 
    print("no esta aqui")
    
