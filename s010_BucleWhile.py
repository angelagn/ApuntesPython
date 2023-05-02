#Guardar valores del 1 al 100 en una lista

lista1 = []
i = 1
while i < 100:
    lista1.append(i)
    i = i + 1

print("numeros de 1 a 99",lista1)




#imprimir numeros pares
lista2 = []
i = 2
while i < 100:
    lista2.append(i)
    i = i + 2

print(lista2)

#Otra forma de imprimir lista de valores
lista3 = list(range(1,101))
print("rango de valores lista 3",lista3)