# ejercicio 1
# Leer numeros enteros del teclado hasta que el usuario ingrese el 0. finalmente mostar la sumatoria de todos los numeros
suma = 0

numero= int(input("ingresa un numero, este juego acaba cuando ingreses el numero 0: "))

while numero!=0:
    suma += numero
        
    numero= int(input("ingresa un numero, este juego acaba cuando ingreses el numero 0: "))  
    
print(f"Como no tienes memoria para recordar todos los numeros que me diste aqui esta tu suma total de todos los num que ingresaste= {suma}")

# ejercicio 2
# Escribir un algoritmo que lea del teclado un numero entero y que compruebe si el numero es menor que 10. si no lo esta debe volver a leer el numero repitiendo la oeracion hasta que el usuario escriba un valor correcto. finalmente debe escribir por pantalla el valor correcto ingresado

numeroNigma = int(input("ingresa un numero del 0 al 20: "))

while numeroNigma>=10:
    
        print(f"Ingresaste el numero {numeroNigma} y es incorrecto para descifrar el codigo ")
    
        numeroNigma = int(input("ingresa un numero del 0 al 20: "))
        
print(f"ingresaste el numero {numeroNigma} y este es menor que 10, venciste al gato con botas")

#ejercicio 3 Modifica el algoritmo del problema pasado para que en vez de comprobar que el numero sea menor que 10 comprube que esta en el rango del (0,20)

numeroNigma2 = int(input("ingresa un numero del 0 al 50: "))

while 0<numeroNigma2<20:
    
        print(f"Ingresaste el numero {numeroNigma2} y es incorrecto para descifrar el codigo ")
    
        numeroNigma2 = int(input("ingresa un numero del 0 al 50: "))
        
print(f"ingresaste el numero {numeroNigma2} y este esta en el rango de 0,20 venciste al gato con botas")


#ejercicio 4 
#modifica el  algoritmo 

numeroNigma3 = int(input("ingresa un numero del 0 al 50: "))
vidas = 0

while not (0<numeroNigma3<20):
    
        print(f"Ingresaste el numero {numeroNigma3} y es incorrecto para descifrar el codigo ")
        vidas +=1
    
        numeroNigma3 = int(input("ingresa un numero del 0 al 50: "))
        
print(f"ingresaste el numero {numeroNigma3} y este esta en el rango de 0,20 lo intentaste {vidas} veces, te falta ser mago para vencerme en menos vidas")