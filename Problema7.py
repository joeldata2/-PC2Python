"""--------------------------------------------------Problema 7:
Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no."""

def es_primo(numero):
    # 0 y 1 no son primos
    if numero < 2:
        return False
    
    # Verificamos si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    # Si no ha sido divisible por ningún número, es primo
    return True

# Solicitamos al usuario ingresar un número para verificar si es primo
numero = int(input("Ingrese un número para verificar si es primo: "))

# Llamamos a la función e imprimimos el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")