"""---------------------------Problema 2:------------------------------------
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
"""


# Número de filas. No pide ser ingresadas por usuario
filas = 5

# Parte positiva de la piramide
for i in range(1, filas + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Parte negativa de la priamide
for i in range(filas - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()