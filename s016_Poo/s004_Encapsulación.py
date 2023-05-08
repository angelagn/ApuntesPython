'''encapsilación, el método de hacer algo privado
que no sea accesible'''

class A:
    def __init__(self):
        #el self es para que busque una variable interna 
        self._contador = 0 #un guion bajo para decir que el atributo es privado
    def incrementa(self):
        #self busca las variables internas
        self._contador += 1

    '''no es necesario poner private ni nada, solo el guion bajo
    para declarar la variable como privada'''
    def cuenta(self):
        return self._contador

obj1 = A()
obj1.incrementa()
obj1.incrementa()
obj1.incrementa()
print(obj1.cuenta())
#acceder a la variable privada
print(obj1._contador)

# #clase B heredea de tipo objeto
# class B(object):
#     #contructor
#     def __init__(self):
#         self._contador = 0
