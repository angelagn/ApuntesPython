'''--Propiedades, son las anotaciones de java, se utoiliza la @ para
metodos set y get, con las notas @property y @key.setter
la @ indica una propiedad del método'''
class Persona:
    def __init__(self, clave, nombre):
        self.__clave = clave
        self.nombre = nombre

    #get definido por el property
    @property #comentario para el get
    def key(self):
        return self.__clave #  get  | variable privada con dos guiones bajos
    
    @key.setter  #comentario para el set
    def key(self, valueTem):
        self.__clave = valueTem  # set


    #get definido por nosotros
    def getClave(self):
        return self.__clave
    
people1 = Persona("asdf", "angela")
print(people1.key)
people1.key = "otra contraseña" #hacemos set para cambiar la contraseña
print(people1.key)