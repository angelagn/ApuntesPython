'''20. La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
•Ingredientes vegetarianos: Pimiento y tofu.
•Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos
los ingredientes que lleva.'''

#Declara variables
ingrediente1 = "Mozzarela"
ingrediente2 = "Tomate"
ingrediente3 = ""
seleccion = ""


#Crea una clase con los diferentes menús de la app
class Menu():
    def MenuVegetariana():
        print("Elija un ingrediente")
        print("1. Pimiento")
        print("2. Tofu")

    def MenuCarne():
        print("Elija un ingrediente")
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmón")
    
    def MenuBuenvenido():
        print("===================================")
        print("Bienvenido a La pizzería Bella Napoli")
        print("Elija la opción que desee")
        print("1. Pizza vegetariana")
        print("2. Pizza con carne")
        print("3. salir")



    

  #Clase App que tiene la lógica del programa 
class App():

    Menu.MenuBuenvenido()
    valor1 = int(input("Por favor ingrese un número: \n")) 
    
    #Seleccion del tipo de pizza e ingredientes
    if valor1 == 1:

        #Pizza vegetariana
        seleccion = "Vegetariana"
        Menu.MenuVegetariana()

        #Ingreedientes vegetariana
        valor2 = int(input("Por favor ingrese un número: \n"))
        if valor2 == 1:
            ingrediente3 = "Pimiento"
        elif valor2 == 2:
            ingrediente3 = "Tofu"


    elif valor1 == 2:

        #Pizza de carne
        seleccion = "Carne"
        Menu.MenuCarne()
        #INgredientes pizza carne
        valor3 = int(input("Por favor ingrese un número: \n"))
        if valor3 == 1:
            ingrediente3 = "Peperoni"
        elif valor3 == 2:
            ingrediente3 = "Jamón"
        elif valor3 == 3:
            ingrediente3 = "Salmón"
    else:
        print("Hasta pronto")
    
    #Muestra seleccion al usuario
    print("===================================")
    print("su pizza seleccionada es: ", seleccion)
    print("Los ingredientes que contiene son:\n")
    print(ingrediente1, ingrediente2, ingrediente3)