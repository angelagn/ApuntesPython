class Truangulo:
    lado1 = 0
    lado2 = 0
    lado3 = 0

    def inicializar(self):
        self.lado1 = int(input("Ingrese el lado1 del triangulo"))
        self.lado2 = int(input("Ingrese el lado2 del triangulo"))
        self.lado3 = int(input("Ingrese el lado3 del triangulo"))

    #Método setter
    def setLado1(self, lado1):
        self.lado1 = lado1

    def setLado2(self, lado2):
        self.lado2 = lado2

    def setLado3(self, lado3):
        self.lado3 = lado3


    #Método getter
    def getLado1(self, lado1):
        self.lado1 = lado1

    def getLado2(self, lado2):
        self.lado2 = lado2

    def getLado3(self, lado3):
        self.lado3 = lado3


# comprobamos el lado mayor
	
    def mayor(self):
        print("El lado mayor es")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print("Lado 1: ",self.lado1)
        elif self.lado2>self.lado3:
            print("Lado 2: ",self.lado2)
        else:
            print("Lado 3: ",self.lado3)

