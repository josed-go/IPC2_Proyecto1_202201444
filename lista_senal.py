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
        
    def mostrar_senales(self):
        print("TOTAL DE SEÑALES:", self.size)
        print("")
        actual = self.primero

        while actual != None:
            print("Señal:", actual.senal.nombre)
            actual = actual.siguiente

    def grafica_original(self, nombre_archivo, nombre_senal):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre == nombre_senal:
                actual.senal.lista_datos.generar_grafica_original(actual.senal.nombre, str(actual.senal.tiempo), str(actual.senal.amplitud), nombre_archivo)

            actual = actual.siguiente

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
            print("Grupos")
            actual.senal.lista_grupos.mostrar_lista()

            actual = actual.siguiente