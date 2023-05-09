'''1. Crear la clase heroe1 con los atributos
	canFly = True
	canShoot = True

2. Crear la clase heroe2 con los atributos
	canEyesLaser = True
	name = "superman"

3. Crea una clase que herede de heroe1 y heroe2 y ademas tiene el metodo
	showinfo(self):
    	   print("Mi nombre nuevo es X")

4. Crear un objeto de la clase3.
	- Imprimir si puede volar
	- Imprimir si puede disparar
	- Imprimir el nombre
	- Imprimir la funcion showinfo()'''

class Heroe1:
    def __init__ (self, canFly, canShoot):
        self.canFly = True
        self.canShoot = True

    def puedeVolar(self):
        if self.canFly == True:
            print("el heroe puede volar")

    def puedeDisparar(self):
        if self.canShoot == True:
            print("el heroe puede disparar")



class Heroe2:
    def __init__(self, canEyesLaser, name):
        self.canEyesLaser = True
        self.name = "Superman"


class MostrarHeroe(Heroe1, Heroe2):
    def __init__(self, canFly, canShoot):
        super().__init__(self, canFly, canShoot)

    def ShowInfo(self, nuevoTemp):
        #nuevoTemp = Heroe
        print("mi nombre nuevo es", nuevoTemp)

    ShowInfo("super Mario")