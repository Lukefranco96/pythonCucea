numero1=  int(input("ingresa el numero 1: "))
numero2= int(input ("ingresa el numero 2: "))
rango= range(numero1,numero2)
for numero in rango:
    if numero%2==0:
        print (f"numero par {numero}")
    else :
        print(f"numero imprar{numero}")