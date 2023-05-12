'''Siempre hay que cerrar los archivos
r => de lectura
w =>de escribir
a =>de aniadir
'''


# #Modo 1 de lectura

# #Creamos un archivo txt en la misma carpeta
# #el archivo txt se puede utilizar como base de datos, hay que que veridicar que esteb bien tabulados

# # archivo1 = open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", encoding="UTF-8") # la r es de lectura
# # print(archivo1.read())

# #Modo 2 de lectura
# #seabre modo lectura y recorre el archivo linea a linea 
# archivo2 = open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r")
# for line in archivo2:
#     print(line)

# archivo2.close()


# #Modo 3
# archivo3 = open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r")
# #Leer las primeras tres líneas
# # print(archivo3.readline()) # lee de línea en línea
# # print(archivo3.readline()) #lee otra linea
# # print(archivo3.readline()) # lee otra linea


# # print(archivo3.readlines()[2]) #imprime un alinea de codigo
# #imprime 3 lineas de código
# for i in range(3):
#     linea = archivo3.readline()
#     if (i == 2): "solo imprime la psicion 2"
#     print(linea)


# #la funcion rstrip('\n') borra el espacio entre las lineas
# archivo4 = open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r")

# for line in archivo4:
#     line = line.rstrip('\n')
#     print(line)

# archivo4.close()



# #4 caracteres de la primera linea
with open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r") as archivo:
    linea = archivo.readline(4) #4 caracteres
    
    print(linea)


#4 ultimos caracteres de una linea
# with open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r") as archivos:
#     for i in range(3):  
#         linea = archivos.readline().replace("\n", "=> (sevilla)")
#         print(linea)

#guardar palabras en lista.
#creo la lista
datos2 = []
#abro archivo con alias pra recorrerlo
with open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r") as fname:
    #recorro el archivo por lineas
    for lineas in fname:
        datos2.extend(lineas.split()) #el extend va añadiendo palabra a palabra a la lista
        print("i", datos2) # imprimo cada dato que se agrega
print(datos2)

