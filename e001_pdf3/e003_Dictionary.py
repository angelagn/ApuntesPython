#Crearemos un Dictionary con los siguientes datos:
#- NombreApellidosAlumnos : NotaEntera
#- Añade 10 alumnos al Dictionary
notas = {"Pablo" : 7, "Juana" : 6, "Juanita": 8, "Pepe": 8, "Maria": 4,
         "Obi": 8, "Sofi" : 7, "Randy": 9, "Mengano" : 8, "Perecnejo" : 10 }

#- Imprime todos los datos del Dictionary
print(notas)
#- Imprime solo las keys
print("Keys del diccionario: \n", notas.keys())
#- Imprime solo las values
print("Valores del diccionario: \n", notas.values())
#- Añade 2 alumnos más
notas["Angela"] = 8
notas["loki"] = 9
print("Diccionario con dos alumnos más: \n",notas)
#- Actualiza los datos de uno de los 2 últimos alumnos
notas["Angela"] = 9
notas["loki"] = 7
#- Imprime todos los datos del dictionary
print("Diccionario actualizado: \n", notas)
#- Borra uno de los alumnos, el que quieras
del notas["Juanita"]
#- Imprime todos los datos del dictionary
print("Diccionario sin un elemento: \n", notas)