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

print(curpGenerada(OMAR))




# pedir 10 calificaciones de alumnos y mostrar el promedio de los 10


# palindromas

# revisar cuantas veces se repite una palabra  diccionarios con listas hashmaps

# revisar si es pangrams

# oracle

# ver si las siguientes palabras se tienen en comun ya sea de derecha a izq o de izq a derecha


# hulk
# monthulk

# rapid
# forgett

# coder
# redocalib
