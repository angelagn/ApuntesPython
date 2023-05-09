'''6. Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido.'''

num = int(input("Por favor escriba un numero: \n"))

for i in range(num):
    print("*" *(i+1))