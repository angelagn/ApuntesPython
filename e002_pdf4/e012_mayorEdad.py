'''12. Crear una aplicación, que solicite por teclado el nombre y 
la edad y muestre el siguiente mensaje
Miguel es mayor de 18 años o es menor de 18 años ( usa el if: else: )
'''

nombre = input("Ingrese nombre de alumno\n")
edad = int(input("Ingrese edad del alumno\n"))

if edad >= 18:
    print(nombre, "es mayor de edad.")
else:
    print(nombre, "es menor de edad.")