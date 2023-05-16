# CONTROLA EL TIEMPO DE EJECUCION DE FUNCIONES

'''Ejecuta una función cada cierto tiempo'''
# import time

# def funcionAejecutar():
#     print("hola")

# estado = True
# while True:
#     funcionAejecutar()
#     time.sleep(1) #espera 1 segundo
#     print("Se ejecuta todo...")




'''Sistema multihilo, son soldaditos para ponerlos  a hacer cosas distintas'''
import threading

def f():
    print("Hola mundo")

def f2():
    print("Adios mundo cruel")



t = threading.Timer(3, f) # 3 segundos a esperar y la f es la funcion
y = threading.Timer(5, f2) # 5 segundos a esperar y la f2 es otra funcion
t.start() # para iniciar 
y.start()
print("Esto se ejecuta antes que la funcion")





'''Llamar funcion con parametros
'''

# import threading

# def worker(number):
#     print("hilo: " + str(number)+ '\n')

# for i in range(4):
#     thread = threading.Thread(target=worker, args=(i, ))
#     thread.start()



