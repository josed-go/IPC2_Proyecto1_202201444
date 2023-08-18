from dato import dato
from senal import senal
import xml.etree.ElementTree as ET
import os.path as path
from os import remove
from tkinter.filedialog import askopenfilename
from lista_datos import lista_datos
from lista_senal import lista_senal

lista = lista_senal()

def leer_xml(archivo):
    """print("SELECCIONE EL ARCHIVO")
    ruta = askopenfilename()
    archivo = open(ruta, "r")
    archivo.close()"""


    tree = ET.parse(archivo+".xml")
    root = tree.getroot()

    validar(root, tree)

    if path.exists("archivo_temporal.xml"):
        tree = ET.parse("archivo_temporal.xml")
        root = tree.getroot()

    for senal_ in root.findall('senal'):
        
        nombre = senal_.get('nombre') 
        valor_t = senal_.get('t')
        valor_A = senal_.get('A')
        
        if validar_tiempo_amplitud(valor_t, valor_A) == True:
            print("Nombre = ", nombre, "| t =",valor_t, "| A =",valor_A)

            lista_dato = lista_datos()
            lista_patrones = lista_datos()

            datos_senal(senal_, valor_t, valor_A, lista_dato, lista_patrones)

            nueva_senal = senal(nombre, valor_t, valor_A, lista_dato, lista_patrones)

            lista.agregar_senal(nueva_senal)

        elif validar_tiempo_amplitud(valor_t, valor_A) == False:
            print(f"** DATOS NO VALIDOS, VALOR t = {valor_t} o A = {valor_A} PASAN EL RANGO EN LA SEÑAL {senal_.get('nombre')}**")
    
    if path.exists("archivo_temporal.xml"):
        remove("archivo_temporal.xml")
    
def datos_senal(senal, t, A, lista_dato, lista_patrones):
    for datos in senal.findall('dato'):
        valor_t = datos.get('t')
        valor_A = datos.get('A')

        if validar_datos(valor_t, valor_A, t, A) == True:
            
            valor = datos.text
            if int(valor) > 1:
                valor = 1

            print("t =",datos.get('t'), "| A =",datos.get('A'), "| Valor = ", datos.text, "| Binario =", valor, senal.get('nombre'))
            nuevo_dato = dato(datos.get('t'),datos.get('A'),datos.text, valor, senal.get('nombre'))
            nuevo_patron = dato(datos.get('t'),datos.get('A'),valor, valor, senal.get('nombre'))
            lista_dato.agregar(nuevo_dato)
            lista_patrones.agregar(nuevo_patron)

        elif validar_datos(valor_t, valor_A, t, A) == False:
            print(f"** DATOS NO VALIDOS, VALOR t = {valor_t} o A = {valor_A} PASAN EL RANGO **")

def validar(root, tree):
    for senal in root.findall('senal'):
        valor_t = senal.get('t')
        valor_A = senal.get('A')
        coordenadas_existentes = set((dato.get('t'), dato.get('A')) for dato in senal.findall('dato'))
    
        for t in range(1, int(valor_t)+1):  # RANGO DE 1 AL NUMERO t
            for A in range(1, int(valor_A)+1):  # RANGO DE 1 AL NUMERO A
                coordenada = (str(t), str(A))
                if coordenada not in coordenadas_existentes:
                    print("Señal: ", senal.get('nombre'))
                    print("FALTA UN DATO EN TIEMPO =", str(t) , "Y AMPLITUD =", str(A))
                    nuevo_dato = ET.SubElement(senal, 'dato', t=str(t), A=str(A))
                    nuevo_dato.text = '0'

    tree.write('archivo_temporal.xml')

def mostrar_datos():
    lista.mostrar_lista()

def validar_tiempo_amplitud(t, A):
    t = int(t)
    A = int(A)
    if t > 0 and t <= 3600 and A > 0 and A <= 130:
        return True
    else:
        return False

def validar_datos(valor_t, valor_A, t, A):
    if int(valor_t) <= int(t) and int(valor_A) <= int(A):
        return True
    else:
        return False