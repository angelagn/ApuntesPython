class Padre:
    def __init__(self, ojos, cejas):
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre):
    def __init__(self, ojos, cejas, cara):
        Padre.__init__(self, ojos, cejas)
        self.cara = cara


obj1 = Hijo("Marrones", "negras", "larga")
print("Ojos: " + obj1.ojos)
print("cejas:" + obj1.cejas)
print("cara: " + obj1.cara)