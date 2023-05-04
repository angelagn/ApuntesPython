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
print("Multiplicación de complejos: ", a * b)

#División
print("División de complejos: ", a / b)

#Conjugado complejos 
a = 1 + 1j
print("Conjugado ", a.conjugate())




import cmath

print("Fase", cmath.phase(complex(5,0)))
print("Polar",cmath.polar(complex(5,5)))