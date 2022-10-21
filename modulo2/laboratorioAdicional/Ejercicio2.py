###
Pedir nombre
Crear un programa que solicite el nombre de un alumno a través de la consola, y luego chequee
que no esté vacío.
En caso de estarlo, tiene que imprimir un mensaje de error; caso contrario, deberá imprimir un mensaje indicando que se ingresó correctamente.
###

nombre_alumno = input("Ingresar el nombre de un alumno: ")
if nombre_alumno == "":
    print("Error: se ingreso un nombre invalido.")
else:
    print("Se ingreso el nombre del alumno correctamente.")
