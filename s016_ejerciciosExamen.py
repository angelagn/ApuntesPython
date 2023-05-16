
from typing import Self


diasSemana = ['lunes', 'miercoles', 'viernes']
mensaje = 'Me gusta ir a la piscina ...'

salida = mensaje + ' ' + ' y '.join(diasSemana) + ' !!'

#print(salida)


'''18. Crearemos la siguiente aplicación informática en python
- Nos mostrará un menú principal de bienvenida
- Nos solicitará un importe de compra ( ejemplo: pantalones 100e )
- Una función, Nos calculará un descuento de un 2% por ser festivo
- Una función, Nos calculará el IVA del 21%
- Luego nos mostrará el total a pagar por consola
'''

# importe = int(input("Ingrese el importe del producto: \n"))

# def descuentoFestivo():
#     descuento = importe * 2 / 100
#     return descuento

# def iva():
#     iva = importe * 21 / 100
#     return iva

# def totalPagar():
#     total = importe + iva() - descuentoFestivo()
#     return total

# total = totalPagar()
# print("Total a pagar:", total)


'''19. Corrige el siguiente código para poder controlar una respuesta booleana por parte del usuario
ListadoMascota = ___________
TipoMascota = input("¿Dispone de alguna mascota (si o no): \n")
print(TipoMascota)
print(type(TipoMascota)) # str
if TipoMascota == ____________:
ListadoMascota = ___________
else:
ListadoMascota = ___________
if ListadoMascota:
________________ = input("Introduzca nombre mascota: \n")
else:
________________ = "El alumno no dispone de ningún carnet"
print(tipoListadoMascota)
'''
# listadoMascota = False
# tipoMascota = input("Dispone de mascota (si/no): \n")
# #print(tipoMascota)

# #print(type(tipoMascota))

# if(tipoMascota == "si"):
#     listadoMascota = True
# else:
#     listadoMascota = False

# if(listadoMascota == True):
#     nombre = input("Introduzca nombre de la mascota:")
#     print("El nombre de la mascota es: " + nombre)
# else:
#     print("No dispone de mascota")


'''22. Crearemos 3 clases para poner un ejemplo de herencia multiple
- ClaseA + metodo1 print …
- ClaseB + metodo2 print …
- ClaseC + metodo3 print …
- Crear un objeto de la ClaseC que hereda de ClaseA y ClaseB
- Usar el método2 heredado de la ClaseC
'''

       

# class A:
#     def __init__(self):
#        print("clase A")
       
# class B:
#     def __init__(self):
#        print("clase B")

# class C(A, B):
#     def __init__(self):
#         B.__init__(self)
#         A.__init__(self)
     

# obj1 = C()


'''
23. Crea una aplicación llamada Login
- Solicitaremos el nombre de Usuario por teclado
- Solicitaremos el apellido de Usuario por teclado
- Almacenaremos dichos datos dentro de un archivo UTF-8
- Luego imprimiremos el contenido del archivo creado
'''


# archivo1 = open("/home/angela/ApuntesPython/archivo.txt", encoding="UTF-8") # la r es de lectura

# print(archivo1.read())

#Escribir, siempre se va a sobreescribir el contenido


# nombre = input("por favor ingrese el nombre")
# apellido = input("por favor ingrese el apellido")

# with open("/home/angela/ApuntesPython/archivo.txt", "w") as fichero1:

#     fichero1.write(nombre)
#     fichero1.write(apellido)

# archivo = open("/home/angela/ApuntesPython/archivo.txt", "r")
# print(archivo.read())
   

'''24. Mejora el ejemplo anterior usando try … except … finally
'''

nombre = input("Por favor, ingrese el nombre: ")
apellido = input("Por favor, ingrese el apellido: ")

try:
    with open("/home/angela/ApuntesPython/archivo.txt", "w") as fichero1:
        fichero1.write(nombre)
        fichero1.write(apellido)
except IOError:
    print("Error al escribir en el archivo")
finally:
    archivo = open("/home/angela/ApuntesPython/archivo.txt", "r")
    try:
        print(archivo.read())
    except IOError:
        print("Error al leer el archivo")
    finally:
        archivo.close()

