'''LIstas son estructuras que nos permiten 
almacenar cualquier tipo de datos'''

#Lista de enteros
calificaciones = [10, 9, 8, 7, 5]
print(calificaciones)

#Lista de string
nombres = ["ana", "Juan", "Sofia", "Pepe", "Pablo"]
print(nombres)

#Lista de diferentes tipos de datos
mezclaValue = [True, 10.5, "abc, [1,2,3]"]
print(mezclaValue)

#Indice de listas, imprime elementos de la lista
print("Nombre: ", nombres[2]) #Sofia
print("Nombre: ", nombres[-1]) #el último de la lista
print("Values: ", mezclaValue[2]) #"abc"

#Añade elementos a la lista
nombres.append("Maria")
nombres.append("Laura")
print(nombres)
#Elimninar elementos de la lista 
nombres.remove("Juan")
print(nombres)

#De lista a tupla
print(tuple(nombres))

#Imprimir elementos de la lista
print(nombres[2])

#Imprime toda la lista
print(nombres[:])
 
squares = [1,4,9,16,25]
squares + [37, 70]
print(squares)
print(max(squares)) #Saca el valor maximo de la lista


