'''1. Realizar un programa que conste de una clase llamada 
Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos 
y mostrar un mensaje con el resultado de la nota y si ha aprobado 
o no.'''


class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    #Métodos get

    def imprimirNombre(self):
        print("El nombre es", self.nombre)

    def imprimirNota(self):
        print("La nota es", self.nota)

    #Método set
    
    def cambiarNombre(self, nombreTemp):
        self.nombre = nombreTemp
        
    def cambiarNota(self, notaTemp):
        self.nombre = notaTemp
    
    def aprobado(self, nota):
        if nota < 5:
            print("no aprobado")
        else:
            print("Aprobado")


alumno1 = Alumno("Pepito", 10)
alumno1.imprimirNombre()
alumno1.imprimirNota()
alumno1.aprobado(5)

