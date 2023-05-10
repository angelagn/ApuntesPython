#Excepcion on file

try:
    archivo = open("/home/angela/ApuntesPython/s016_Poo/Prueba.txt", "r")
    print(archivo.readline())
except IOError:
    print("Error entrada y salida")

except:
    print("Procesando error")

finally:
    if not (archivo.close):
        archivo.close()
