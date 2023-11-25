"""----------------------------Problema 1:------------------------------------------------------------
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos)"""

numeros_div_mul = []

# rango de 1500 a 2700
for numero in range(1500, 2701):
    # comprobamos si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        # Si cumple la condición, se agrega a una lista
        numeros_div_mul.append(numero)

# Imprimimos los resultados
print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(numeros_div_mul)
