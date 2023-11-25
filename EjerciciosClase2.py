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

""" --------------------------------------------Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
……
“Desea ingresar un número?”: NO
Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
Cantidad de números pares: 5
Cantidad de números impares: 4
Nota:
- Quizás a manera de ayuda el uso de una lista le sea de utilidad.
- El empleo de break sobre condiciones while también le serán de utilidad."""

# Lista para almacenar los números ingresados
numeros = []

# Inicializamos contadores para números pares e impares
pares = 0
impares = 0

# Bucle para ingresar números
while True:
    ingresar = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if ingresar == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)

        # Verificamos si el número es par o impar y actualizamos los contadores
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif ingresar == "NO":
        # Imprimimos la lista de números ingresados
        print("Números ingresados:")
        print(numeros)
        # Mostramos la cantidad de números pares e impares
        print("Cantidad de números pares:")
        print(pares)
        print("Cantidad de números impares:")
        print(impares)
        break
    else:
        print("Respuesta no válida. Por favor, ingrese SI o NO.")



"""-----------------------------------------------Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
Nota:
El uso de listas con diccionarios le será de utilidad."""

#Este codigo lo corrí en spyder y si me pregunta el valor n de los alumnos. Pero aca en github no. Pero no se por que. Lo incluyo para su retro.

# Lista para almacenar los datos de los alumnos
lista_alumnos = []

# Solicitamos el número de alumnos
num_alumnos = int(input("Ingrese el número de alumnos: "))

# Bucle para ingresar los datos de cada alumno
for numero_alumno in range(1, num_alumnos + 1):
    # Solicitamos el nombre del alumno
    nombre = input(f"Ingrese el nombre del alumno {numero_alumno}: ")

    # Inicializamos una lista para guardar las notas del alumno
    notas = []

    # Bucle para ingresar las 3 calificaciones del alumno
    for i in range(3):
        nota = float(input(f"Ingrese la calificación {i + 1} del alumno {nombre}: "))
        notas.append(nota)

    # Creamos un diccionario con el nombre del alumno y sus calificaciones
    alumno = {"Alumno": nombre, "Notas": notas}

    # Agregamos el diccionario a la lista de alumnos
    lista_alumnos.append(alumno)

    # Imprimimos el listado completo de alumnos
    print("\nListado completo de alumnos:")
    for alumno in lista_alumnos:
        print(alumno)


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


