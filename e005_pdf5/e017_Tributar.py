'''17. Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al
usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que
tributar o no'''

edad = int(input("Por favor ingrese su edad: \n")) 
ingresos = int(input("Por favor escriba el ingreso: \n"))

def Tributar():
    if edad > 16 and ingresos > 1000:
        print("La persona debe tributar")
    else:
        print("La persona no debe tributar")


Tributar()