'''16. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es
par o impar'''

entero = int(input("Por favor ingrese un número: \n")) 

#funcion que define si es par  o impar
def ParImpar():
    num = entero%2
    if num == 0:
        print("El numero ", entero, "es par" )
    else:
        print("El numero ", entero, "es impar" )

#llamado a la función
ParImpar()