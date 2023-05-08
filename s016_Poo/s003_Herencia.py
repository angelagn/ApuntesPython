#capacidad de  heredar caracteristicas de  ootra clase
#herencia

class Abuelo:
    def printAbuelo(self):
        print("Soy la funcion abuelo")

class Padre:
    def printPadre(self):
        print("soy la funcion padre")

'''Herencia'''
#se indican entre parentesisi las clases de las que se quiere heredar
#Python permite herencia múltiple
class Hijo(Abuelo, Padre):
    def printHijo(self):
        print("soy el hijo")

obj1 = Hijo()
obj1.printAbuelo()
obj1.printPadre()
