# def saludo(empresa):
#     print(f"Hola somos {empresa} \n")
    
# saludo("Bimbo")
# saludo("Gamesa")

# def suma(a,b):
#     resultado = a+b
#     return resultado
    
# def multiplicacion(num1, num2, num3):
#     resMult= num1*num2*num3
#     print(f"La suma es de: {resMult}")
#     return resMult
    

# newResult = suma(5,4)

# resultTotal= multiplicacion(5,5,newResult)

# ejercicio 1
# def saludar(nombre):
#     print (f"Hola{nombre} Bienvenido a funciones en python")
    
# saludar("Pedro")
# saludar("Carlos")
# saludar("Omar")

# Ejercicio 2
# def saludar(nombre):
#     print(f"Hola {nombre}")
    
# saludar("Pedro")

# ejercico 3
# def parONo(numero):
#     if numero %2 == 0:
#       print ("es par")
    
#     else:
        
#       print("impar") 

# parONo(5)    

# ejercicio 4

def calcularFactura():
    cantidadSinIVA = float(input("ingresa el total de tu compra para calcular tu factura: "))
    impuesto= float(input("ingresa lo que vas a apagar de impuesto de la factura: "))
    impuestoPErsonalizado= cantidadSinIVA * impuesto
    cantidadPersonalizada= cantidadSinIVA*impuestoPErsonalizado
    iva= cantidadSinIVA*.21
    factura= cantidadSinIVA+iva
   
    if impuesto == 0:
            factura= cantidadSinIVA+iva
    else:
        factura = cantidadPersonalizada
    return factura

totalFactura= calcularFactura()
print(f" ESte es el total de tu factura= {totalFactura}")