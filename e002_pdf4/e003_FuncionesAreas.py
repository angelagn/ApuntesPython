
import math
'''3. Crea un modulo con tres funciones, cada una de ellas será para calcular
- El area del cuadrado ( area = lado * lado )
- El area del Circulo ( A=PI*r^2 )
- El area del triangulo ( area=int (base) * int (altura) / 2.0 )
llamar a cada función para que imprima el resultado de dichos calculos, las variables deben crearse
dentro de la función'''

def areaCuadrado():
    lado = 2
    return(lado*lado)



def areaCirculo():
    radio = 5
    a = math.pi * radio ** 2
    return(a)


def areaTriangulo():
    base = 3
    altura = 4
    aT = base * altura / 2
    return (aT)


print("Area cuadrado: \n",areaCuadrado())

print("Area circulo: \n", areaCirculo())
#print(math.pi)

print("Area Triangulo : \n",areaTriangulo())