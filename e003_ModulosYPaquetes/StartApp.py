
# crear los namespace
import Paquete1.module1 
import Paquete2.module1
#import Paquete2.module2



#Hacer uso de lo que hay en el módulo 1
print(Paquete1.module1)
print(Paquete2.module1)
#print(Paquete2.module2)

#namespace con alias
#import Paquete2.module2 as p2m2
#print(p2m2)

#llamar variables de los módulos, en este caso del modulo 2

# print(p2m2.nombre)
# print(p2m2.altura)


#Importar una variable
from Paquete2.module2 import nombre
print(nombre)

#importar una función
Paquete2.module1.saludo()

#importar paq 3 mod 3
from Paquete3.module3 import * #Importa todo el contenido
print("\nimporta las funciones del modulo3 paq 3 \n")
fundoble(2)
fundiv1(4, 2)
funcuadrado(6)

