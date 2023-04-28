'''Secuencia de elementos, lista, no pueden ser modificadas 
directamente, no exixte append o insert'''

colores =("azul", "verde", "rojo") #La tupla es entre parentesis
print(colores[0])
print(colores[-1])

#Convertir a lista, la lista va entre corchetes[]
print(list(colores))

listaColores =list(colores)
print(listaColores)