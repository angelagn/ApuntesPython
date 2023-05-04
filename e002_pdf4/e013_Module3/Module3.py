'''13. Crear una carpeta nueva Module3 y dentro de el un archivo module3.py, Crearemos 3 funciones:
doble de un numero
mitad de un numero
cuadrado de un numero
division de 2 numero mostrando la parte decimal
división de 2 numero sin mostrar la parte decimal
Crear un archivo StartApp2.py que importe dicho paquete y modulo y llamaremos a las funciones'''
import math

#funcion doble de un numero
num = 5
def Doblenum():
    print("1. El doble del numero es:", num*2 )

#funcion mitad de un numero

def MitadNum():
    print("2. El doble del numero es:", num/2 )

#Función cuadrado de un numero
def CuadradoNum():
    print("3. El cuadrado del numero es:", num**2 )

#Función division de 2 numero mostrando la parte decimal

n1 = 10
n2 = 3
def divDecimal():
    resultado = n1 / n2
    print("4. División con parete decimal",round(resultado, 2))

#Función division de 2 numero mostrando la parte entera
def divEntera():
    resultado = n1 // n2
    print("5. División con parete entera",round(resultado))