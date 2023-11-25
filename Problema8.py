"""Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento."""



def factorial(numero):
    # El factorial de 0 es 1
    if numero == 0:
        return 1

    # Inicializamos el resultado con 1
    resultado = 1

    # Multiplicamos todos los números desde 1 hasta el número ingresado
    for i in range(1, numero + 1):
        resultado *= i

    return resultado

# Ingresar un número para calcular su factorial
numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

# Llamamos a la función e imprimimos el resultado
resultado_factorial = factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es {resultado_factorial}")