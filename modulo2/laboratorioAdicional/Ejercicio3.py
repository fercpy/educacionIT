###
Comparar entrada de números
Pedir la edad por teclado y comparar si es mayor o menor de edad. No olvidar de que para
poder comparar el ingreso debe ser convertido a int, ya que el usuario ingresa un número entero.
###

edad = input("Que edad tenes? : ")
edad = int(edad)

if edad < 18:
  print("Sos menor de edad")
else:
  print("Sos mayor de edad")

