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