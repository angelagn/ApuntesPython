'''6. Crea una función que reciba 2 parametros ( mayor, menor ) y realice la división. Llamaremos a la
función pasandole los valores'''

def division(numMayor, numMenor):
    if numMayor< numMenor:
        return(numMenor / numMayor)
    else:
        return (numMayor /numMenor)


print("EL resultado de la división es: \n", division(6, 3))