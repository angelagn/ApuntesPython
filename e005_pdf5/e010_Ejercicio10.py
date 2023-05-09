'''10. Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es un número primo o no'''

num = int(input("Por favor escriba un numero: \n"))

def esPrimo(numero):
    # Los números menores a 2 no son primos
    if numero < 2:
        print(num, "no es primo")
        return False
    
    # Comprobar si el número es divisible por algún otro número distinto de 1 y de sí mismo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(num, "no es primo")
            return False
    # Si no es divisible por ningún otro número, es primo
    print(num, "es primo")
    return True

esPrimo(num)