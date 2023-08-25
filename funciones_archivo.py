from dato import dato
from dato_patron import dato_patron
from dato_grupo import dato_grupo
from grupo import grupo
from senal import senal
import xml.etree.ElementTree as ET
import os.path as path
from os import remove
from lista_datos import lista_datos
from lista_senal import lista_senal
from lista_patron import lista_patron
from lista_grupo import lista_grupo
from lista_dato_grupo import lista_dato_grupo

lista = lista_senal()

def leer_xml(archivo):
    print("-> LEYENDO ARCHIVO...")
    print("")
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
            #print("Nombre = ", nombre, "| t =",valor_t, "| A =",valor_A)

            lista_dato = lista_datos()
            lista_patrones = lista_datos()
            lista_grupos_senal = lista_grupo()

            datos_senal(senal_, valor_t, valor_A, lista_dato, lista_patrones)
            print(F"-> GENERANDO MATRIZ BINARIA DE SEÑAL: {nombre} ...")
            print("")
            matriz_patrones(lista_patrones, valor_t, valor_A,lista_grupos_senal)

            print(f"-> REALIZANDO SUMA DE TUPLAS DE SEÑAL: {nombre} ...\n")
            nueva_senal = senal(nombre, valor_t, valor_A, lista_dato, lista_patrones, lista_grupos_senal)
            lista.verificar_senal(nombre)
            lista.agregar_senal(nueva_senal)
            print("-> PROCESO TERMINADO\n")
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

            #print("t =",datos.get('t'), "| A =",datos.get('A'), "| Valor = ", datos.text, "| Binario =", valor, senal.get('nombre'))
            nuevo_dato = dato(datos.get('t'),datos.get('A'),datos.text, valor, senal.get('nombre'))
            nuevo_patron = dato(datos.get('t'),datos.get('A'),datos.text, valor, senal.get('nombre'))
            lista_dato.agregar(nuevo_dato)
            lista_patrones.agregar(nuevo_patron)

        elif validar_datos(valor_t, valor_A, t, A) == False:
            print(f"** DATOS NO VALIDOS, VALOR t = {valor_t} o A = {valor_A} PASAN EL RANGO **")

def matriz_patrones(lista_patrones, valor_t, valor_A, lista_grupos_senal):
    lista_temporal = lista_patron()
    lista_temporal_2 = lista_patron()
    for t in range(1, int(valor_t)+1):   
        cadena = ""
        for patron in lista_patrones:
            if t == int(patron.dato.tiempo):
                cadena += str(patron.dato.valor_binario)
        
        dato_temporal = dato_patron(t,cadena)
        lista_temporal.agregar_patron(dato_temporal)
        lista_temporal_2.agregar_patron(dato_temporal)

    for patron_temp in lista_temporal:
        validar_patron(lista_temporal_2,patron_temp.patron, lista_patrones, lista_grupos_senal, valor_A)
    

def validar_patron(lista_tempo, patron, lista_patrones, lista_grupos_senal, valor_A):
    tiempos = ""
    for patron_validar in lista_tempo:

        if patron == patron_validar.patron:
            tiempos += str(patron_validar.tiempo)+","

    tiempos_nuevo = tiempos.rstrip(',')

    validar_patron_grupo(lista_patrones, tiempos_nuevo, valor_A, lista_grupos_senal)

def validar_patron_grupo(lista_patrones, tiempos, valor_A, lista_grupos):
    suma = 0
    contador = 0
    tiempo_sin_comas = tiempos.replace(",","")
    lista_temporal = lista_dato_grupo()
    if validar_tiempo_grupo(lista_grupos, tiempos) == False:
        for i in range(1, int(valor_A)+1):
            for datos_lista in lista_patrones:
                if datos_lista.dato.tiempo in tiempos and int(datos_lista.dato.amplitud) == i:
                    suma = suma + int(datos_lista.dato.valor)
                    contador += 1
                    if contador == len(tiempo_sin_comas):
                        dato_grupo_nuevo = dato_grupo(datos_lista.dato.amplitud,suma, tiempos)
                        lista_temporal.agregar_dato_grupo(dato_grupo_nuevo)
            contador = 0
            suma = 0
        nuevo_grupo = grupo(lista_grupos.obtener_size(), tiempos, lista_temporal)
        lista_grupos.agregar_grupo(nuevo_grupo)

    #lista_temporal.mostrar_lista()

def validar_tiempo_grupo(lista_validar, tiempos):
    if lista_validar.obtener_size() == 0: return False

    for datos_grupo in lista_validar:
        if datos_grupo.grupo.tiempos == tiempos:
            return True
    return False

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

def mostrar_senales():
    lista.mostrar_senales()

def generar_grafica_original(nombre_senal, nombre_archivo):
    lista.grafica_original(nombre_archivo, nombre_senal)

def generar_grafica_reducida(nombre_senal, nombre_archivo):
    lista.grafica_grupo(nombre_senal, nombre_archivo)

def validar_nombre_senal(nombre):
    for senales in lista:
        if senales.senal.nombre == nombre:
            return True
    return False

def limpiar_datos():
    lista.limpiar_datos()

def obtener_tamanio_senales():
    return lista.obtener_size()

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