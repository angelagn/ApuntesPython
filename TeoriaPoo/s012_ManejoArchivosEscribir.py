#Escribir, siempre se va a sobreescribir el contenido
with open("/home/angela/ApuntesPython/s016_Poo/PruebaEScribir.txt", "w") as fichero1:
    fichero1.write("Linea1\n")
    fichero1.write("Linea2\n")
    fichero1.write("Linea3\n")

#Agregar más contenido
#add

with open("/home/angela/ApuntesPython/s016_Poo/PruebaEScribir.txt", "a") as fichero1:
    fichero1.write("Linea4\n")
    fichero1.write("Linea5\n")
    fichero1.write("Linea6\n")

#Preguntar cuantas lineas tiene el archivo
with open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r") as fp:
    x = len(fp.readlines())
    print('total lineas: ', x)