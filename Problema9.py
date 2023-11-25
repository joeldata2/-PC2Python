"""Métodos de Cadenas:
Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
-
Input: Twitter
Output: Twttr
-
Input: What's your name? Output: Wht's yr nm? """


def omitir_vocales(palabra):
    # Creamos una cadena nueva sin vocales
    palabra_sin_vocales = ''.join(letra for letra in palabra if letra.lower() not in 'aeiou')

    return palabra_sin_vocales

# Solicitamos al usuario ingresar una cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Llamamos a la función e imprimimos el resultado
resultado = omitir_vocales(texto)
print(f"Texto sin vocales: {resultado}")