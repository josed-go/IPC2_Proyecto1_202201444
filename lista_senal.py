from nodo_senal import nodo_senal

class lista_senal:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar_senal(self, senal):
        nodo_nuevo = nodo_senal(senal = senal)
        if self.primero is None:
            self.primero = nodo_nuevo
            self.size +=1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = nodo_nuevo
        self.size += 1

    def mostrar_lista(self):
        print("TOTAL DE SEÑALES:", self.size)
        print("")
        print("")
        actual = self.primero

        while actual != None:
            print("Señal:", actual.senal.nombre, "| Tiempo:", actual.senal.tiempo, "| Amplitud:", actual.senal.amplitud)
            print("Datos")
            actual.senal.lista_datos.mostrar_lista()
            print("Patrones")
            actual.senal.lista_patrones.mostrar_lista()

            actual = actual.siguiente