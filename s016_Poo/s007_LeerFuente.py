from s006_FuenteDeClases import Persona

persona1 = Persona("angela", 45)
print(persona1.nombre)

from s006_FuenteDeClases import Square

obj1 = Square(5)
#se guarda en una variable temporal
val = obj1.getVal()
print(val)


from s006_FuenteDeClases import SumaResta

obj2 = SumaResta()
#ejecuta el método en el print
print(f"de la clase sumaresta: suma {obj2.suma(2,4)}")
print(f"de la clase sumaresta: resta {obj2.resta(10, 5)}")