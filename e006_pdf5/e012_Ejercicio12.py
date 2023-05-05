'''12. Escribir un programa en el que se pregunte al usuario por
 una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase'''

frase = input("Por favor escriba una frase: \n")
letra = input("Por favor escriba una letra: \n")
veces = 0
for i in range(0, len(frase)):
    if frase[i] == letra:
        veces += 1
print("La letra ha aparecido",veces, "veces.")

