'''7. Crear un función con 3 parámetros python, 2 de ellos 
tendrán un valor por defecto “lo puedes elegir” y
devolverá la suma de los 3 parametros'''

def tresParametros(val1 , val2 = 5, val3 = 5):
    return(val1 + val2 + val3)


'''- Llama a la función pasándole 3 valores nuevos
- Llama a la función pasándole 1 valor y que coja 
solo los 2 valores por defecto'''
print("La suma  con tres parametros es:", tresParametros(4, 3, 2))
print("La suma es con un parámetro es:", tresParametros(4))