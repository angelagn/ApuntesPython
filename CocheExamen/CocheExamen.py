'''21. Crearemos el siguiente proyecto POO
- Crear una clase llamada CocheExamen
- Tendrá un constructor para asignar un valor gasolina cuando se cree el objeto
- Tendrá un método de arrancar, que nos sacará un mensaje si tenemos gasolina o no
- Tendrá un método de conducir, que nos sacará un mensaje si andamos porque tenemos gas o no,
restará algo de gasolina del trayecto realizado
'''

class CocheExamen:
    def __init__(self, gasolina):
        self.combustible = gasolina

    def arrancar(self):
        if self.combustible >= 10:
            self.combustible -= 10
            print("El coche ha arrancado. Combustible disponible: {}%.".format(self.combustible))
        else:
            print("No hay suficiente combustible para arrancar.")

    def conducir(self):
        if self.combustible >= 20:
            self.combustible -= 10
            print("El coche está en movimiento. Combustible disponible: {}%.".format(self.combustible))
        else:
            print("No hay suficiente combustible para conducir.")


            
gasolina = input("¿Tenemos gasolina? (si/no): ")
if gasolina == "si":
    cantidad_gasolina = int(input("Ingrese la cantidad de gasolina en porcentaje: "))
    coche = CocheExamen(cantidad_gasolina)
    coche.arrancar()
    coche.conducir()
    coche.conducir()
    coche.conducir()
    coche.conducir()




else:
    print("Es necesario recargar gasolina.")



