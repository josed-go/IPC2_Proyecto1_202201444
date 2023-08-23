from nodo import nodo
import os

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
    
    def generar_grafica_original(self, nombre_senal, tiempo, amplitud, nombre_grafica):
        f = open('bb.dot', 'w')

        texto = """
                digraph G {"t = """+tiempo+"""","A = """+amplitud+""""->" """+nombre_senal+ """" bgcolor="white" style="filled"
            subgraph cluster1 {fillcolor="white" style="filled"
            node [shape=box fillcolor="white" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="white" gradientangle="315">\n"""
        
        actual = self.primero
        sentinela = actual.dato.tiempo
        fila = False

        while actual != None:
            if sentinela != actual.dato.tiempo:
                sentinela = actual.dato.tiempo
                fila = False

                texto += """</TR>\n"""
            if fila == False:
                fila = True
                texto += """<TR>"""
                texto += """<TD border="3" bgcolor="white">"""+str(actual.dato.valor)+"""</TD>\n"""
            else:
                texto += """<TD border="3" bgcolor="white">"""+str(actual.dato.valor)+"""</TD>\n"""
            actual = actual.siguiente
        texto += """ </TR></TABLE>>];
                    }
                    }\n"""
        print(texto)
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o {nombre_grafica}.png')
        print("## GRAFICA GENERADA ##")

    def mostrar_lista(self):
        auxiliar = self.primero
        while auxiliar != None:
            print("t=", auxiliar.dato.tiempo, "| A =", auxiliar.dato.amplitud, "| Valor =", auxiliar.dato.valor, "| Binario =", auxiliar.dato.valor_binario, "| Señal =", auxiliar.dato.nombre_senal)
            auxiliar = auxiliar.siguiente