''' Crea una lista en python que almacene los nombres de los jugadores de un equipo de futbol,
seguidamente:'''
equipo = ["Juno", "Jdos", "Jtres", "Jcuatro", "Jcinco"]
print(equipo)

#Mostrar el primer jugador
print(equipo[0])
#Mostrar el último jugador
print(equipo[-1])
#- Mostrar el jugador que esté en la posición 2
print(equipo[1])
#Añadir también el nombre del entrenador en la lista
equipo.append("Entrenador")
print(equipo)
#Borra uno de los jugadores de la lista, simulará una baja del equipo
equipo.remove("Jcuatro")
#Imprimir los valores actualizados de la lista (Jugadores + Entrenador)
print(equipo)
#Imprimir una conversión de la lista actualizada a tuple
print(tuple(equipo))