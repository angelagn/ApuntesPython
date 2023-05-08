'''18. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que
pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde'''

nombre = input("Por favor ingrese su nombre: \n")
sexo = input("Por favor escriba el sexo: mujer/hombre \n")

def asignacionGrupo():
    if nombre < "m" and sexo == "mujer":
        print(nombre, " se asigna al grupo A")
    elif nombre > "n" and sexo == "hombre":
         print(nombre, "se asigna algrupo B")
    else:
        print("fuera de parametros no se asigna grupo")


asignacionGrupo()