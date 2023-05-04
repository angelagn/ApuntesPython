'''9. Realiza los siguientes cálculos con las funciones que correspondan:
máximo de 3 valores
máximo de 2 valores
máximo en una lista de numeros ( 8 elementos elegidos por tí )
máximo de una lista de nombres ( 5 elementos elegidos por tí )
mínimo de 3 valores
mínimo de 2 valores
mínimo en una lista de numeros ( 8 elementos elegidos por tí )
mínimo de una lista de nombres ( 5 elementos elegidos por tí )
'''

#máximo de 3 valores
val1 = 3
val2 = 5
val3 = 7

print("1. El valor maximo es: ", max(val1, val2, val3))

#máximo de 2 valores
def Maximo():
    if val1 > val2:
        print("2. el valor máximo (Función)", val1)
    else:
         print("2. el valor máximo (Función) es", val2)

Maximo()



#máximo en una lista de numeros ( 8 elementos elegidos por tí )
listaNum = [2,3,4,5,76,8,9,6]
print("3. El valor maximo de la lista es: ",max(listaNum)) #Saca el valor maximo de la lista


#máximo de una lista de nombres ( 5 elementos elegidos por tí )
listaNombres = ["consuelo", "salvador", "dolores", "Angela", "concepcion"]
print("4. Maximo valor en lista de nombres: ",max(listaNombres))

#mínimo de 3 valores
print("5. valor mínimo de 3 valores: ", min(val1, val2, val3))

#mínimo de 2 valores
print("6. valor mínimo de 2 valores: ", min(val2, val3))

#mínimo en una lista de numeros ( 8 elementos elegidos por tí )
print("7. El valor minimo de la lista es: ",min(listaNum))

#mínimo de una lista de nombres ( 5 elementos elegidos por tí )
print("8. El valor minimo de la lista es: ",min(listaNombres))