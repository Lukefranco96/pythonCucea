#  problema 1
# Solicitar al usuario que ingrese dos numeros y mostrar cual de los numero es menor, considerar el caso en que ambos sean iguales 
print("ingresa 2 nunmeros y te dire cual es el menor ")
numero1 = int(input("Ingresa tu primer numero: "))
numero2 = int(input("Ingresa tu segundo numero: "))

if(numero1>numero2):
    print(f"El numero {numero2} es menor que el {numero1}")
elif(numero2>numero1):
    print(f"El numero {numero1} es menor que el {numero2}")
else:
    print("Me diste numeros iguales papu")