## Crear un programa que solicite una fila y una
###columna e imprima en pantalla el número en 
### esa posición según la siguiente matriz:

## Fila: 1
## Columna: 2
## 6.4 
### matriz = [

### El programa debe chequear que la fila y la
### columna tengan valores válidos.
### En este caso, las únicas filas válidas son 0 y 1;
### las columnas, 0, 1 y 2. Si alguno de los dos
### valores es inválido, debe mostrar un mensaje
### de error.

matriz = [
         [3.3, 6.1, 4.0], 
         [4.9, 5.7, 6.4]
]

fila = int(input("Ingrese el numero de fila: "))
columna = int(input("Ingrese el numero de columna "))

if fila < len(matriz):
	if columna < len(matriz[fila]):
          print("El numero de la posicion buscada es" ,  matriz[fila][columna])
	else:
		print("El valor de columna es invalido")
else:
	print("El valor de las filas es invalido")

