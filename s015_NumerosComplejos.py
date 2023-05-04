a = 5 +5j
b = 1.3 -7j

#Numero complejo con parte real iguala cero
c = 10.3j


c= 3 + 5j
print(c.real)
print(c.imag)

#Crear numeros complejos
c = complex(3,5)
print(c)

#Suma de complejos
a = 1 + 3j
b = 4 + 1j
print("Suma de complejos: ", a + b)

#Resta de complejos

print("Resta de complejos: ", a - b)

#Multiplicación
'''La multiplicación es algo más compleja. Si multiplicamos 
a+bj por c+dj, se puede demostrar
fácilmente que el resultado es (ac-bd) para la parte real 
y (ad+bc) para la imaginaria. '''

print("Multiplicación de complejos: ", a * b)

#División
print("División de complejos: ", a / b)

#Conjugado complejos 
''' Calcular el conjugado consiste en negar la parte imaginaria,
 es decir, cambiar si signo de + a - y
viceversa.'''
a = 1 + 1j
print("Conjugado ", a.conjugate())


'''Algunas de las cosas que puedes hacer son las siguientes:
•Calcular la fase, que es el ángulo que forma el vector con el 
eje x, en radianes.
•Calcular la forma polar, es decir módulo y ángulo.'''
import cmath

print("Fase", cmath.phase(complex(5,0)))
print("Polar",cmath.polar(complex(5,5)))