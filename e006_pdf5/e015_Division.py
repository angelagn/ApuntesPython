'''15. Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error'''

val1 = int(input("Por favor ingrese un número: \n"))    
val2 = int(input("Por favor ingrese un número: \n"))   

if val2 == 0:
    print("error, el divisor no puede ser cero")
else:
    print(f"El resultado de la division es: {val1 / val2}")
