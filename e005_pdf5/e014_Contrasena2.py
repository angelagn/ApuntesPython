'''14. Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas. ( if )'''

contrasena = "palabra clave"


continuar = True
while continuar:
    teclado = input("Por favor escriba la contraseña: \n")
    if (contrasena == teclado):
        break
