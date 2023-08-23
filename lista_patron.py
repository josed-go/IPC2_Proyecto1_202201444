from nodo_patron import nodo_patron

class lista_patron:
    def __init__(self):
        self.primero = None
        self.size = 1

    def agregar_patron(self, dato_patron):

        nuevo_nodo = nodo_patron(dato_patron = dato_patron)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.size += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = nuevo_nodo
        self.size += 1

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual.dato_patron
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration
        
    def obtener_size(self):
        return self.size

    def mostrar_lista(self):
        print("TOTAL PATRONES:", self.size)
        print("")
        print("")
        print("")

        actual = self.primero
        while actual != None:
            print("Tiempo:", actual.dato_patron.tiempo, "| Patron:", actual.dato_patron.patron)
            actual = actual.siguiente