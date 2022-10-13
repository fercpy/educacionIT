###
Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares
###


salario_total_enero_a_junio = 300 * 6
salario_total_julio_a_octubre = 500 * 4
salario_total_noviembre_a_diciembre = 700 * 2

salario_anual = salario_total_enero_a_junio + salario_total_julio_a_octubre + salario_total_noviembre_a_diciembre

print("El salario anual es de $",salario_anual)

salario_promedio = round(salario_anual / 12)
print("Su salario promedio es de $", salario_promedio)

if salario_promedio < 300:
    print("Sueldo Bajo")
elif salario_promedio < 900:
    print("Sueldo Normal")
else:
    print("Sueldo mejor de lo Normal")
