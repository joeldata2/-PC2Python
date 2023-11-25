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