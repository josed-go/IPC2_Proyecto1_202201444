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
            print("** PRIMERO DEBES INGRESAR UN ARCHIVO **")
        
        menu()
    elif opcion == "3":
        fa.mostrar_datos()
        menu()
    elif opcion == "4":
        datos_estudiante()
        menu()
    elif opcion == "5":

        menu()
    elif opcion == "6":

        menu()
    elif opcion == "7":
        print("## SALIENDO... ##")
    else:
        print("** OPCIÓN NO VÁLIDA **")
        menu()

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