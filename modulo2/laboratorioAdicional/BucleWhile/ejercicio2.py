###
Pedir por teclado el nombre de usuario, si está vacío, volver a pedirlo hasta que se ingrese
un nombre. Luego, saludar al usuario. 
###

nombre = input("Ingrese su nombre de usuario: ")


while nombre == "":
	print("Debe ingresar un nombre valido")
	nombre = input("Volve a ingrsar tu nombre de usuario: ")

print("Hola, tu nombre de usuario es "+ nombre)
