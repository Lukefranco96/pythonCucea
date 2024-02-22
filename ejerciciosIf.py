#  problema 1
# Solicitar al usuario que ingrese dos numeros y mostrar cual de los numero es menor, considerar el caso en que ambos sean iguales 
print("ingresa 2 nunmeros y te dire cual es el menor")
numero1 = int(input("Ingresa tu primer numero: "))
numero2 = int(input("Ingresa tu segundo numero: "))


if(numero1>numero2):
    print(f"El numero {numero2} es menor que el {numero1}")
elif(numero2>numero1):
    print(f"El numero {numero1} es menor que el {numero2}")
else:
    print("Me diste numeros iguales papu")


# ejercicio 2 
# solicita al usuario que ungrese un numero de cliente, si es el numero 1000 dile que no un premio
print ("Ingresa tu numero de cliente a continuacion")
numCliente= int(input("Cual es su ID de cliente: "))

if numCliente == 1000:
    print("Ganaste premio maquinola")
else:
    print("Sigue intentando que estas mas alado que el mar")
    
#ejercicio 3
print("Ingresa 2 números y te diré cuál es el menor (sin considerar números iguales).")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 != num2:
    menor = min(num1, num2)
    print(f"El número {menor} es el menor.")
else:
    print("Los números son iguales.")


#ejercicio 4 
# Hacer porograma que permita saber si un a~no es bisiesto, para que sea un a~no bisisesto debe ser divisible entre 4 y no dene ser divisible por 100 eepto que tambien sea divisible por 400 

def esBisisesto(anio):
    if(anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False
    
anio = int(input("Ingresa el año: ")) 

if esBisisesto(anio):
    print("Es bisiesto el año")
else:
    print("No es bisiesto el año")    
    
# Escribe un programa que pida tres numeros y que escruiba si son los tres iguales si hay dos igualess o si los tres son distintos
print("ingresa 3 numeros a continuacion, te dire si los tres son iguales en valor o si son diferentes")
number1 = int(input("ingresa tu primer numero: "))
number2 = int(input("ingresa tu segundo numero: "))
number3 = int(input("ingresa tu tercer numero: "))

if number1 == number2 == number3:
    print ("Todos son iguales padrino")
elif (number1 == number2 or number3 == number1 or number2==number3):
    print("tienes dos numeros iguales")
else:
    print("todos son diferentes")