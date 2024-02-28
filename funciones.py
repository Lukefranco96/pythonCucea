def saludo(empresa):
    print(f"Hola somos {empresa} \n")
    
saludo("Bimbo")
saludo("Gamesa")

def suma(a,b):
    resultado = a+b
    return resultado
    
def multiplicacion(num1, num2, num3):
    resMult= num1*num2*num3
    print(f"La suma es de: {resMult}")
    return resMult
    

newResult = suma(5,4)

resultTotal= multiplicacion(5,5,newResult)