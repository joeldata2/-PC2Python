"""Funciones:
Problema 5:
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4
Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
count."""

def cont_digitos(numero, digito):
    # Convertimos el número a cadena para facilitar la manipulación de dígitos
    numero_cadena = str(numero)

    # Contamos la cantidad de veces que aparece el dígito en el número
    cantidad = numero_cadena.count(str(digito))

    return cantidad

# Solicitamos al usuario ingresar un número y un dígito
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese un dígito: "))

# Llamamos a la función y mostramos el resultado
cantidad_digitos = cont_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero}: {cantidad_digitos}")
