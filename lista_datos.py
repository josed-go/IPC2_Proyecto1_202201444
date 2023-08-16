from nodo import nodo

class lista_datos:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def esta_vacia(self):
        return self.primero == None

    def agregar(self, dato):

        nuevo_nodo = nodo(dato)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

        self.size += 1
        
    def mostrar_lista(self):
        auxiliar = self.primero
        while auxiliar != None:
            print("t=", auxiliar.dato.tiempo, "| A =", auxiliar.dato.amplitud, "| Valor =", auxiliar.dato.valor, "| Binario =", auxiliar.dato.valor_binario)
            auxiliar = auxiliar.siguiente