def saludoPersonalizado():
    print("Hola mundo Python")

def despedida():
    print("adios")

#funcion con parametros
def saludoNombre(name):
    print("hello", name)
    
#Funcion que suma valores
def sumar(val1, val2):
    return(val1 + val2)


#Valores predeterminados
def sumar2(val3, val4 = 5):
    return(val3 + val4)

#Funcion duplica el valor
def duplica(val5):
    return(val5 + val5)


#

#llamado de funciones
saludoPersonalizado()
despedida()
saludoNombre("angela")
print(sumar(3, 5))

print("un solo parametro: ",sumar2(3))
print(sumar2(val4= 8, val3=4))
print(duplica(5))
