###
###Insertar entre Alejandro y Roberto a Paula. 
##Y luego agregar al final a Silvina.
###Para finalizar, hay que recorrer la lista y mostrar a
###todos los nombres por pantalla.
###

### append método, puedes agregar un elemento al final de la lista.
## my_list.append(object)

### El método insert() es utilizado para insertar un elemento en un índice (una posición) particular de la lista.
## Syntax: list_name.insert(index, element)

nombres = ["Susana","Alejandro","Roberto"]

nombres.insert(2, "Paula")
nombres.append("Silvina")
print(nombres)

