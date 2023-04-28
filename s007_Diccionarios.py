'''Clave : valor
nombre :  "Angela"'''
#Los diccionarios se definen con llaves
edades = {"JUan" : 22, "Juana" : 23, "Juanita": 42}
#Imprime todo el diccionario
print(edades)
#Imprima solo las llaves
print(edades.keys())
#Imprima solo valores, el resultado en consola sale como lista
print(edades.values())
#Añadir elementos
edades["Angela"] = 45
print(edades)
#Modificar elementos
edades["Angela"] = 50
print(edades)
#Borrar elementos
del edades["Angela"]
print(edades)
