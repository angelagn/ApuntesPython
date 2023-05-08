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
        nuevoTemp = Heroe
        print("mi nombre nuevo es", nuevoTemp)

    ShowInfo("super Mario")