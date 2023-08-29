from nodo_senal import nodo_senal
import os
import xml.etree.ElementTree as ET

class lista_senal:
    def __init__(self):
        self.primero = None
        self.size = 0
        self.grupos = ""
        self.datos_grupos = ""

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

    def verificar_senal(self, nombre_senal):
        senal = None
        actual = self.primero

        while actual:
            if actual.senal.nombre == nombre_senal:
                if senal is None:
                    self.primero = actual.siguiente
                else:
                    senal.siguiente = actual.siguiente
                    print(f"## SEÑAL: {nombre_senal} REPETIDA, SERA ACTUALIZADA ##\n")
                self.size -= 1
                actual = actual.siguiente
            else:
                senal = actual
                actual = actual.siguiente
            
        """actual = self.primero

        while actual != None:
            if actual.senal.nombre == nombre_senal:
                print(f"## SEÑAL: {nombre_senal} REPETIDA, SERA ACTUALIZADA ##")
                del actual
                break
            actual.siguiente"""

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

    def grafica_grupo(self, nombre_senal, nombre_archivo):
        text = ""
        flag = False
        actual = self.primero
        while actual != None:

            if actual.senal.nombre == nombre_senal:
                self.grupos = actual.senal.lista_grupos.generar_grafica()
                flag = True
                break
            if flag != True:
                actual = actual.siguiente
        
        if flag:
            f = open('bb.dot','w')
            text = """ digraph G {
	            a0 [ label=" """+actual.senal.nombre+"""" fontname="Courier New" ] 
                a1 [ label="A = """+actual.senal.amplitud+"""" fontname="Courier New" ]\n
                a2 [ shape="none" fontname="Courier New" label=< <TABLE border="0" cellspacing="10" cellpadding="10" bgcolor="white">\n"""
            text += self.grupos
            text += """</TABLE>>]\n
                        a0 -> a1;\n
                        a0 -> a2;\n}"""
            
            f.write(text)
            f.close()
            os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
            os.system(f'dot -Tpng bb.dot -o {nombre_archivo}.png')
            print(f"## GRAFICA REDUCIDA DE SEÑAL: {nombre_senal} GENERADA ##")

    def limpiar_datos(self):
        while self.primero != None:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
        self.size = 0
        print("-> PROCESO TERMINADO...")

    def obtener_size(self):
        return self.size

    def escribir_xml(self, nombre_archivo):
        data = ET.Element('senalesReducidas')
        actual = self.primero
        while actual != None:

            element = ET.SubElement(data, 'senal', nombre=f'{actual.senal.nombre}', A=f'{actual.senal.amplitud}')
            grupos_ = actual.senal.lista_grupos
            for grupos in grupos_:
                s_element = ET.SubElement(element, 'grupo', g=f'{grupos.grupo.grupo}')
                datos_grupos = grupos.grupo.datos_grupo
                s_element_2 = ET.SubElement(s_element, 'tiempos')
                s_element_2.text = grupos.grupo.tiempos
                s_element_3 = ET.SubElement(s_element, 'datosGrupo')
                for datos in datos_grupos:
                    s_element_4 = ET.SubElement(s_element_3, 'dato', A=f'{datos.amplitud}')
                    s_element_4.text = str(datos.valor)
                    
                
            prueba = ET.tostring(data)
            actual = actual.siguiente
        self.prettify_xml(data)
        tree = ET.ElementTree(data)
        tree.write(nombre_archivo+".xml")
        print("-> PROCESO TERMINADO...\n")
        print(f"## SE CREO CORRECTAMENTE EL ARCHIVO {nombre_archivo}##\n")

    def prettify_xml(self,element, indent='    '):
        queue = [(0, element)]  # (level, element)
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level+1) 
            if queue:
                element.tail = '\n' + indent * queue[0][0]  
            else:
                element.tail = '\n' + indent * (level-1)  
            queue[0:0] = children

    def mostrar_lista(self):
        print("TOTAL DE SEÑALES:", self.size)
        print("")
        print("")
        actual = self.primero

        while actual != None:
            self.grupos = ""
            print("Señal:", actual.senal.nombre, "| Tiempo:", actual.senal.tiempo, "| Amplitud:", actual.senal.amplitud)
            print("Datos")
            actual.senal.lista_datos.mostrar_lista()
            print("Patrones")
            actual.senal.lista_patrones.mostrar_lista()
            print("Grupos")
            actual.senal.lista_grupos.mostrar_lista()

            actual = actual.siguiente
        