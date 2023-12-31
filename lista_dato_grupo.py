from nodo_dato_grupo import nodo_dato_grupo

class lista_dato_grupo:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar_dato_grupo(self, dato_grupo):

        nuevo_nodo = nodo_dato_grupo(dato_grupo = dato_grupo)

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
            valor_actual = self.actual.dato_grupo
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration
        
    def obtener_size(self):
        return self.size
    
    def generar_grafica(self, grupo):
        datos = ""
        actual = self.primero
        sentinela = actual.dato_grupo.amplitud
        datos += f"""<TR><TD border="1" bgcolor="white">{grupo}</TD>"""
        
        fila = False
        while actual != None:
            if sentinela != actual.dato_grupo.amplitud:
                sentinela = actual.dato_grupo.amplitud
                fila = False
            if fila == False:
                fila = True
                datos += f"""<TD border="1" bgcolor="white">{str(actual.dato_grupo.valor)}</TD>\n"""
            else:
                datos += f"""<TD border="1" bgcolor="white">{str(actual.dato_grupo.valor)}</TD>\n"""
        
            actual = actual.siguiente
        datos += """</TR>\n"""
        
        return datos

    def mostrar_lista(self):
        print("TOTAL DATOS:", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Amplitud:", actual.dato_grupo.amplitud, "| Valor:", actual.dato_grupo.valor, "| Tiempo:", actual.dato_grupo.tiempo)
            actual = actual.siguiente