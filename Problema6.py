"""-----------------------------------------------Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores."""

# Función para generar la serie de Fibonacci hasta 50
def fibonacci(n):
    # Primeros dos números de la serie
    a, b = 0, 1
    # Lista para almacenar los valores de la serie
    serie_fibonacci = []

    while a <= n:
        serie_fibonacci.append(a)
        a, b = b, a + b

    return serie_fibonacci

# Llamamos a la función y mostramos la serie de Fibonacci hasta el número 50
n = 50
serie = fibonacci(n)

print(f"Serie de Fibonacci hasta {n}:")
print(serie)