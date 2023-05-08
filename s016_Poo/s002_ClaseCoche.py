'''1. clase'''
# para crear una clase las mismas palabras reservadas que en c#
class Coche: 
    #variable sestaticas
    ruedas = 4

    #métodos es como se llaman a las funciones o a los procedimientos en poo
    #metodo constructor siempre lleva la palabra init
    #COnstructor sirve para inicializar variables
    #lleva doble guion bajo en el init
    def __init__(self, color, aceleracion): #se crean las variavbñes
        #se inicializan las variables
        #en python, self es como el this de c#
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0 #variable que no viene por parámetro
    
    #poner self en todos los métodos
    def acelera(self): # el self es para que utilice las variables internas propias de la clase
        self.velocidad = self.velocidad + self.aceleracion
    
    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v
    '''las variables que se cran dentro de una funcion solo viven en la 
    funcion'''


'''2. instanciar o crear objetos de la clase'''
obj1 = Coche("rojo", 20)
#llamar a variables del objeto
print(obj1.color)
print(obj1.ruedas)

#creo otro objeto
obj2 = Coche("azul", 10)
obj2.ruedas = 8
print("el color del coche es" + obj2.color)
print("f{obj2.ruedas}")
