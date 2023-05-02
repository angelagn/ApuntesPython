'''pide numerosy crea una lista, cuando el usuario ingrese 
cero dejamos de insertar, imprime la lista, y orgamizala de
diferentes maneras'''


lista = []
num = ""
while num != 0:
    num = int(input("ingrese un numero"))
    lista.append(num)

print(lista)
#ordenar la lista
lista.sort()
#reverso de la lista
lista.reverse()
#remover el cero
lista.remove(0)
print(lista)