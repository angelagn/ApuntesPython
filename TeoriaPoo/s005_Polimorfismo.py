#capacidad que tenermos de darle diferentes formas a un método
#creo tres clases
class Perro:
    def sonido(self):
        print("Guauuuu")

class Gato:
    def sonido(self):
       print("Miauuuu") 

class vaca:
    def sonido(self):
       print("Muuuu") 


#LÓGICA DEL PROGRAMA  
#creo el objeto
perro1 = Perro() 
#llamo a su método
perro1.sonido()

gato1 = Gato()
gato1.sonido()

vaca1 = vaca()
vaca1.sonido()

#Método que recorre una lista
#Funcion propia del archivo, no es de nunguna clase
def aCantar(animales):
    for animal in animales:
        animal.sonido()
#creo lista con los objetos de arriba
granja = [perro1, gato1, vaca1 ]
aCantar(granja)
