'''16. Intentaremos sumar los valores de una lista'''

numeros = [1,3,5,4]
def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print("La suma de numeros en la lista es: ",suma(numeros))