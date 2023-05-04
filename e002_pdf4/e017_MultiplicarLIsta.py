
'''17. Intenta adaptar el código anterior para hacer 
la multiplicación de valores de una lista'''

numeros = [1,3,5,4]

def multiplicacaion(numeros):
    total = 1 #para que la multiplicación no de cero
    for n in numeros:
        total *= n
    return total

print("La multiplicacion de numeros en la lista es: ", multiplicacaion(numeros))