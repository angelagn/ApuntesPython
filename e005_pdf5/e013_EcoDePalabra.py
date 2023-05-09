'''13. Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que
el usuario escriba “salir” que terminará'''


salir = "salir"

continuar = True
while continuar:
    palabra = input("Por favor grese una palabra por teclado: \n")
    print(palabra)
    if (salir == palabra):
        break

