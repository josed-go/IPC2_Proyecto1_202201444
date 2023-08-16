from dato import dato
import xml.etree.ElementTree as ET
import os.path as path
from os import remove

from lista_datos import lista_datos

lista = lista_datos()

def leer_xml(archivo):
    tree = ET.parse(archivo+".xml")
    root = tree.getroot()

    validar(root, tree)

    if path.exists("archivo_temporal.xml"):
        tree = ET.parse("archivo_temporal.xml")
        root = tree.getroot()

    for senal in root.findall('senal'):
        
        nombre = senal.get('nombre') 
        valor_t = senal.get('t')
        valor_A = senal.get('A')
        
        if validar_tiempo_amplitud(valor_t, valor_A) == True:
            print("Nombre = ", nombre, "| t =",valor_t, "| A =",valor_A)
            datos_senal(senal, valor_t, valor_A)
        elif validar_tiempo_amplitud(valor_t, valor_A) == False:
            print(f"** DATOS NO VALIDOS, VALOR t = {valor_t} o A = {valor_A} PASAN EL RANGO EN LA SEÑAL {senal.get('nombre')}**")
    
    if path.exists("archivo_temporal.xml"):
        remove("archivo_temporal.xml")
    
def datos_senal(senal, t, A):
    for datos in senal.findall('dato'):
        valor_t = datos.get('t')
        valor_A = datos.get('A')

        if validar_datos(valor_t, valor_A, t, A) == True:
            
            valor = datos.text
            if int(valor) > 1:
                valor = 1

            print("t =",datos.get('t'), "| A =",datos.get('A'), "| Valor = ", datos.text, "| Binario =", valor)
            nuevo_dato = dato(datos.get('t'),datos.get('A'),datos.text, valor)
            lista.agregar(nuevo_dato)

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