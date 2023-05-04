'''11. Guardar en variables los datos introducidos por teclado 
(input) para almacenar la estructura de un
clienteAutoEscula, si lo necesitas ve parseando 
( int(input(“dato:”) )

IDAlumno ( numerico )
NombreAlumno
ApellidosAlumno
NumTelfAlumno
EmailAlumno
EdadAlumno
AlturaAlumno
Soltero ( true / false )
TipoCarnetPosee
TipoCarnet
'''
soltero = bool

iDAlumno = int(input("Ingrese el numero ID del alumno\n"))
nombreAlumno = input("Ingrese nombre de alumno\n")
apellidosAlumno = input("Ingrese apellidos de alumno\n")
numTelfAlumno = int(input("Ingrese teléfono del alumno\n"))
emailAlumno = input("Ingrese email de alumno\n")
edadAlumno = int(input("Ingrese edad del alumno\n"))
alturaAlumno = int(input("Ingrese altura del alumno\n"))


#Soltero ( true / false )
soltero = input("El alumno es soltero? (si/no)\n")
if soltero == "si":
    soltero = True
else:
    soltero = False
print(soltero)


#TipoCarnetPosee
carnetPosee = input("El alumno posee carnet? (si/no)\n")
if carnetPosee == "si":
    carnetPosee = True
else:
    carnetPosee = False


#Si posee carnet, se pregunta el tipo, si no se omite la pregunta
if carnetPosee == True:
    tipoCarnet = input("Que tipo de carnet posee? (A/B/C)\n")
    aux = ""
    match tipoCarnet:
        case "a":
            aux = "a"
        case "b":
            aux = "b"
        case "c": 
            aux = "c"
    print("el tipo de carnet que tiene es: ", aux)
else:
    print("No posee carnet")     
            

