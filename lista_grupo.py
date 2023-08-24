from nodo_grupo import nodo_grupo

class lista_grupo:
    def __init__(self):
        self.primero = None
        self.size = 1
        self.datos = ""

    def agregar_grupo(self, grupo):

        nuevo_nodo = nodo_grupo(grupo = grupo)

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
            valor_actual = self.actual
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration

    def obtener_size(self):
        return self.size

    def generar_grafica(self):
        texto = ""
        actual = self.primero

        sentinela = actual.grupo.grupo
        
        fila = False
        while actual != None:
            
            self.datos += actual.grupo.datos_grupo.generar_grafica(f"G = {actual.grupo.grupo} (t = {actual.grupo.tiempos})")
            actual = actual.siguiente
        texto += "\n"+self.datos+"\n"
        return texto
        

    def mostrar_lista(self):
        print("TOTAL GRUPOS:", self.size-1)
        print("")

        actual = self.primero
        while actual != None:
            print("-------------------------------------------------------------")
            print("Grupo:", actual.grupo.grupo, "| Tiempos:", actual.grupo.tiempos)
            print("")
            print("DATOS:")
            actual.grupo.datos_grupo.mostrar_lista()
            print("-------------------------------------------------------------")
            actual = actual.siguiente
