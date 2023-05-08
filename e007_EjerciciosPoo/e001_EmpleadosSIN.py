

class EmpleadosSIN:
    #contructor
    def __init__(self, clave, nombre, puesto):
        self.clave = "3455"
        self.nombre = "pepe"
        self.puesto = "director"
        
    #metodo para deletrear 
    def toList(self, clave):
        return list(clave)
    #Acceder a la variable
    def printClave(self):
        print(f"el puesto es {self.clave}")
    

#creo el objeto
empleado1 = EmpleadosSIN("45", "pepa", "directora" )
empleado1.nombre = "juan"
print(empleado1.nombre)
print(empleado1.toList(empleado1.clave))
print(empleado1.toList(empleado1.nombre))
#llamar metodo para acceder a variable
empleado1.printClave()


