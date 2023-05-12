'''2. Realizar un programa que tenga una clase Persona con las 
siguientes características. La clase tendrá como atributos el 
nombre y la edad de una persona. Implementar los métodos 
necesarios para inicializar los atributos, mostrar los datos e 
indicar si la persona es mayor de edad o no.'''

class Persona:
    nombre = "Angela"
    edad = 50

    #Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #Setter y el constructor es lo mismo, solo se ejecuta el constructor
    # cuando se crea el metodo u el setter cuando se necesita cambiar
    # el valor

    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #getter
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)

    
    def mayorDeEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")


persona1 = Persona("Angela", 40)
persona1.imprimir()
persona1.mayorDeEdad()