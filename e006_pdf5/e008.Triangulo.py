'''8. Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.'''

num = int(input("Por favor escriba un numero: \n"))

for i in range(1,num + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print(" ")

