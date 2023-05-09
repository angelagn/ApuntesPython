class Heroes:
    def __init__(self, nombre, edad, altura, poder, armas):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.poder = poder
        self.armas = armas

    def imprimirNombre(self):
        print("el nombre del heroe es", self.nombre)

    def imprimirEdad(self):
        print("la edad del heroe es", self.edad)

    def imprimirAltura(self):
        print("La altura del heroe es", self.altura)

    def imprimirPoder(self):
        print("El poder del heroe es", self.poder)

    def imprimirArmas(self):
        print("Las armas del heroe es", self.armas)

class Villanos:
    def __init__(self, nombre, poder, armas):
        self.nombre = nombre
        self.poder = poder
        self.armas = armas

    def imprimirNombre(self):
        print("el nombre del villano es", self.nombre)

    def imprimirPoder(self):
        print("el poder del villano es", self.poder)

    def imprimirArmas(self):
        print("armas del villano son", self.armas)

    #Método set
    def cambiarNombre(self, nombreTemp):
        self.nombre = nombreTemp