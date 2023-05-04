import cmath
#Función Suma de complejos
a = 1 + 3j
b = 4 + 1j 

def SumaComplejos():
    a = 1 + 3j
    b = 4 + 1j 
    print("Suma de complejos: ", a + b)

#Función Resta de complejos
def RestaComplejos():
    print("Resta de complejos: ", a - b)

#Función Multiplicación
def MultComplejos():
    print("Multiplicación de complejos: ", a * b)

#Función División
def DivComplejos():
    print("División de complejos: ", a / b)

#Función Conjugado complejos 

a = 1 + 1j
def ConjugadoComplejos():
    print("Conjugado ", a.conjugate())



def FaseYPolar():
    print("Fase", cmath.phase(complex(5,0)))
    print("Polar",cmath.polar(complex(5,5)))