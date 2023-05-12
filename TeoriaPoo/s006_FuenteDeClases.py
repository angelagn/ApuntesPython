
'''Creamos tres clases'''
#clase persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#clase cuadrado
class Square:
    def __init__(self, val):
        self.val = val
    
    def getVal(self):
        return self.val * self.val
    
#clase sumaresta, que tiene dos métodos 
class SumaResta:
    def suma(sefl, a, b):
        return a + b
    
    def resta(sefl, a, b):
        return a - b


                