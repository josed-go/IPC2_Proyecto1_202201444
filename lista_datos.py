from nodo import nodo

class lista_datos:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def agregar(self, dato):

        nuevo_nodo = nodo(dato)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (actual.dato.nombre_senal < nuevo_nodo.dato.nombre_senal or (actual.dato.nombre_senal == nuevo_nodo.dato.nombre_senal and (actual.dato.tiempo, actual.dato.amplitud) < (nuevo_nodo.dato.tiempo, nuevo_nodo.dato.amplitud))):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

        self.size += 1
        
    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration
    
    def mostrar_lista(self):
        auxiliar = self.primero
        while auxiliar != None:
            print("t=", auxiliar.dato.tiempo, "| A =", auxiliar.dato.amplitud, "| Valor =", auxiliar.dato.valor, "| Binario =", auxiliar.dato.valor_binario, "| Señal =", auxiliar.dato.nombre_senal)
            auxiliar = auxiliar.siguiente