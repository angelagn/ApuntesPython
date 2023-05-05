'''9. Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''


contrasena = "palabra clave"


continuar = True
while continuar:
    teclado = input("Por favor escriba la contraseña: \n")
    if (contrasena == teclado):
        print("Contraseña correcta, bienvenido")
        break

