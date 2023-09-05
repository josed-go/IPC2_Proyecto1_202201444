import funciones_archivo as fa
from lista_datos import lista_datos
import os.path as path

class archivo:
    def __init__(self, archivo):
        self.archivo = archivo

    def set_archivo(self, archivo):
        self.archivo = archivo

    def get_archivo(self):
        return self.archivo

arch = archivo("")

def main():
    print("---------------------------------------------------")
    print("** PROYECTO 1 - INTRODUCCIÓN A LA PROGRAMACIÓN 2 **")
    print("---------------------------------------------------")
    menu()

def menu():
    print("")
    print("-------------------------------------------------------")
    print("############# SISTEMA DE SEÑALES DE AUDIO #############")
    print("-------------------------------------------------------")

    print("-------------------------------------------------------")
    print("| 1. CARGAR ARCHIVO                                   |")
    print("| 2. PROCESAR ARCHIVO                                 |")
    print("| 3. ESCRIBIR ARCHIVO SALIDA                          |")
    print("| 4. DATOS DEL ESTUDIANTE                             |")
    print("| 5. GENERAR GRÁFICA                                  |")
    print("| 6. INICIALIZAR SISTEMA                              |")
    print("| 7. SALIR                                            |")
    print("-------------------------------------------------------")

    print("")
    print("## INGRESE UNA OPCION: ##")
    opcion = input()
    print("")

    if opcion == "1":
        nombre = input("INGRESE EL NOMBRE DEL ARCHIVO: ")
        arch.set_archivo(nombre)
        try:
            if path.exists(arch.get_archivo()+".xml") == False:
                arch.set_archivo("")
                print("** ARCHIVO NO ENCONTRADO **")
            else:
                print("\n## ARCHIVO CARGADO CON EXITO ##")
        except:
            print("** ERROR **")
        menu()
    elif opcion == "2":
        if arch.get_archivo() != "":
            fa.leer_xml(arch.get_archivo())
        else:
            print("** PRIMERO DEBES CARGAR UN ARCHIVO **")
        
        menu()
    elif opcion == "3":
        if arch.get_archivo() != "":
            #fa.mostrar_datos()
            nombre_archivo = input("INGRESE EL NOMBRE DE PARA GUARDAR EL ARCHIVO: ")
            print("")
            fa.generar_xml(nombre_archivo)
        else:
            print("** PRIMERO DEBES CARGAR UN ARCHIVO **")
            
        menu()
    elif opcion == "4":
        datos_estudiante()
        menu()
    elif opcion == "5":
        if arch.get_archivo() != "":
            if fa.obtener_tamanio_senales() > 0:

                opcion_graficar()
            else:
                print("** PRIMERO DEBES PROCESAR EL ARCHIVO **")
        else:
            print("** PRIMERO DEBES CARGAR UN ARCHIVO **")
        
        menu()
    elif opcion == "6":
        print("-> LIMPIANDO DATOS...")
        fa.limpiar_datos()
        arch.set_archivo("")
        menu()
    elif opcion == "7":
        print("## SALIENDO... ##")
    else:
        print("** OPCIÓN NO VÁLIDA **")
        menu()

def opcion_graficar():
    print("## SEÑALES DISPONIBLES ##")
    fa.mostrar_senales()
    print("")
    nombre = input("INGRESE EL NOMBRE DE LA SEÑAL A GRAFICAR: ")
    print("")
    if fa.validar_nombre_senal(nombre) == False:
        print("** NO EXISTE UNA SEÑAL CON ESE NOMBRE **")
    else:
        print("## ¿QUÉ TIPO DE GRAFICA DESEA GRAFICAR? ##")
        print("## 1. ORIGINAL ##")
        print("## 2. PATRONES ##")
        print("## 3. REDUCIDA ##")
        opcion_grafica = input("INGRESE LA OPCIÓN A GRAFICAR: ")
        print("")

        if opcion_grafica == "1":
            print("")
            print("## GENERANDO GRAFICA... ##")
            print("")
            nombre_archivo = input("INGRESE EL NOMBRE DE LA GRAFICA: ")
            print("")
            fa.generar_grafica_original(nombre,nombre_archivo)
        
        elif opcion_grafica == "2":
            print("")
            print("## GENERANDO GRAFICA... ##")
            print("")
            nombre_archivo = input("INGRESE EL NOMBRE DE LA GRAFICA: ")
            print("")
            fa.generar_grafica_patrones(nombre, nombre_archivo)

        elif opcion_grafica == "3":
            print("")
            print("## GENERANDO GRAFICA... ##")
            print("")
            nombre_archivo = input("INGRESE EL NOMBRE DE LA GRAFICA: ")
            print("")
            fa.generar_grafica_reducida(nombre, nombre_archivo)
            
        else:
            print("** OPCIÓN NO VÁLIDA **")
            opcion_graficar()

def datos_estudiante():
    print("------------------------------------------------")
    print("############# DATOS DEL ESTUDIANTE #############")
    print("------------------------------------------------")
    print("-> José David Góngora Olmedo ")
    print("-> 202201444 ")
    print("-> Introducción a la Programación y Computación 2 sección ""D"" ")
    print("-> Ingenieria en Ciencias y Sistemas ")
    print("-> 4to Semestre ")


main()