import numpy as np
import signal
from collections import deque
from controlador import sdodb
from controlador.sdodb import ListasNp
from modelo import Vehiculo


def imprimirMenu():
    while True:
        try:
            print(
                f"\n{sdodb.bcolors.HEADER}----Selecciona una de las siguiente opciones-----{sdodb.bcolors.ENDC}\n")
            print("1.-\tAgregar vehiculo")
            print("2.-\tBuscar vehiculo")
            print("3.-\tImprimir certificado")
            print("4.-\tEliminar vechiculo")
            print("5.-\tListar todos los vehículos")
            print("6.-\tSalir\n")
            op = int(
                input(f"{sdodb.bcolors.OKGREEN}---->\t{sdodb.bcolors.ENDC}"))
            if op == 1 and op != None:
                agregarVehiculo()
            elif op == 2 and op != None:
                buscarVehiculo()
            elif op == 3 and op != None:
                imprimirCertificado()
            elif op == 4 and op != None:
                eliminarVehiculo()
            elif op == 5 and op != None:
                imprimirLista()
            elif op == 6 and op != None:
                print(f"{sdodb.bcolors().OKGREEN}Saliendo...{sdodb.bcolors().ENDC}")
                exit(1)

        except Exception as er:
            print("Ha acurrido un error", str(er))


def agregarVehiculo():
    multa = []
    while True:
        try:
            print(
                f"\n{sdodb.bcolors.OKGREEN}---Registrando nuevo vehiculo---{sdodb.bcolors.ENDC}\n")
            tipo = input(
                f"{sdodb.bcolors.OKCYAN}Ingrese el Tipo de vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}")
            patente = input(
                f"{sdodb.bcolors.OKCYAN}Ingrese la Patente del vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}")
            marca = input(
                f"{sdodb.bcolors.OKCYAN}Ingrese la Marca de vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}")
            while True:
                precio = int(input(
                    f"{sdodb.bcolors.OKCYAN}Ingrese el Precio de vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}"))
                if precio > 5000000 and precio != 0:
                    break
                else:
                    print(
                        f"{sdodb.bcolors.WARNING}[!] Debe ingresar un precio superior a $5.000.000. Reintenta nuevamente [!]{sdodb.bcolors.ENDC}")
            while True:
                op = input(
                    f"{sdodb.bcolors.OKCYAN}¿Su vehiculo posee multas? Si/No ---->\t{sdodb.bcolors.ENDC}")
                op = op.lower()
                if op == 'si' or op == 's':
                    pmul = int(input(
                        f"{sdodb.bcolors.OKCYAN}Ingrese el valor de la multa del vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}"))
                    multa.append(pmul)
                    dmul = str(input(
                        f"{sdodb.bcolors.OKCYAN}Ingrese el detalle de la multa del vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}"))
                    multa.append(dmul)
                    break
                elif op == 'no' or op == 'n':
                    multa.append(None)
                    multa.append(None)
                    break
            fecha = input(
                f"{sdodb.bcolors.OKCYAN}Ingrese la fecha de registro del vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}")
            nombre = input(
                f"{sdodb.bcolors.OKCYAN}Ingrese el nombre del dueño del vehiculo {sdodb.bcolors.OKGREEN}--->\t{sdodb.bcolors.ENDC}")
            newVehiculo = Vehiculo.Vehiculo(
                tipo, patente, marca, precio, multa, fecha, nombre)
            if sdodb.rellenarFilaArr(newVehiculo, ListasNp.arrVehiculos) == True:
                break
        except Exception as er:
            print(f"Ha ocurrido un error. {sdodb.bcolors().FAIL}", str(
                er), sdodb.bcolors().ENDC)


def buscarVehiculo():
        try:
            cont = 1
            print("Ingrese la pantente que deseas buscar")
            patente = str(input("----> "))
            lista = sdodb.extraerFilaArr(patente, ListasNp.arrVehiculos, True)
            if lista[1] != None:
                print(
                    f"{sdodb.bcolors().HEADER}\n---Imprimiendo---\n{sdodb.bcolors().ENDC}")
                print(
                    f"{sdodb.bcolors().OKGREEN}Tipo:\t\t\t{lista[0]}{sdodb.bcolors().ENDC}")
                print(
                    f"{sdodb.bcolors().OKGREEN}Patente:\t\t{lista[1]}{sdodb.bcolors().ENDC}")
                print(
                    f"{sdodb.bcolors().OKGREEN}Marca:\t\t\t{lista[2]}{sdodb.bcolors().ENDC}")
                print(
                    f"{sdodb.bcolors().OKGREEN}Precio:\t\t\t{lista[3]}{sdodb.bcolors().ENDC}")
                ls = lista[4]
                if ls[0] != None or ls[1] != None:
                    print(
                        f"{sdodb.bcolors().OKGREEN}Precio Multa:\t\t{ls[0]}{sdodb.bcolors().ENDC}")
                    print(
                        f"{sdodb.bcolors().OKGREEN}Detalle Multa:\t\t{ls[1]}{sdodb.bcolors().ENDC}")
                else:
                    print(f"{sdodb.bcolors().OKGREEN}Multa:\t\t\tNo tiene")
                print(
                    f"{sdodb.bcolors().OKGREEN}Fecha de registro:\t{lista[5]}{sdodb.bcolors().ENDC}")
                print(
                    f"{sdodb.bcolors().OKGREEN}Dueñ@:\t\t\t{lista[6]}{sdodb.bcolors().ENDC}")
        except Exception as er:
            print("Ha acurrido un error", str(er))

def eliminarVehiculo():
    try:
        print("Ingrese la pantente que deseas eliminar")
        patente = str(input("----> "))
        ListasNp().setArrVehiculos(sdodb.vaciarFilaArr(patente, ListasNp().arrVehiculos))
    except Exception as err:
        print("Ha ocurrido un error. ", str(err))

def imprimirCertificado():
        try:
            tip, pat, marca, precio, multas, fechareg, nomDueño = "", "", "", 0, [], "", ""
            cont = 1
            print("Ingrese la pantente que deseas buscar")
            patente = str(input("----> "))
            lista = sdodb.extraerFilaArr(patente, ListasNp.arrVehiculos, True)
            for i in range(len(lista)):
                if i == 0: tip = lista[i]
                if i == 1: pat = lista[i]
                if i == 2: marca = lista[i]
                if i == 3: precio = lista[i]
                if i == 4: multas = lista[i]
                if i == 5: fechareg = lista[i]
                if i == 6: nomDueño = lista[i]
            newVehiculo = Vehiculo.Vehiculo(
                tip, pat, marca, precio, multas, fechareg, nomDueño)
            Vehiculo.Vehiculo.imprimirDatosVehiculo(newVehiculo)
        except Exception as er:
            print("Ha acurrido un error", str(er))


def imprimirLista():
    while True:
        print(f"\n{sdodb.bcolors().HEADER}¿Deseas imprimir sólo los elementos existentes?{sdodb.bcolors().ENDC}")
        print(f"{sdodb.bcolors().HEADER}Si - Mostrará sólo los elementos creados. No - Desplegará todo incluyendo los espacios disponibles.{sdodb.bcolors().ENDC}\n")
        op = str(input(f"{sdodb.bcolors().OKGREEN}---->\t{sdodb.bcolors().ENDC}"))
        print("\n")
        op = op.lower()
        if op == "si" or op == "s":
            newlis = deque()
            for i in range(len(ListasNp.arrVehiculos)):
                if ListasNp.arrVehiculos[i][1] != None:
                    newlis.append(list(sdodb.extraerFilaArr(ListasNp.arrVehiculos[i][1], ListasNp.arrVehiculos, False)))
            rs = np.array(newlis, dtype=object)
            cont = 1
            for i in rs:
                print(f"{sdodb.bcolors().OKGREEN}{cont}.- {list(i)}{sdodb.bcolors().ENDC}")
                cont = cont + 1
            break
        elif op == "no" or op == "n":
            print(ListasNp().arrVehiculos)
            break
        else:
            print(f"{sdodb.bcolors().WARNING}[!] Debes ingresar una opción válida [!]{sdodb.bcolors().ENDC}")

# CTRL+C
def handler(signum, frame):
    print(f"{sdodb.bcolors().OKGREEN}Saliendo...{sdodb.bcolors().ENDC}")
    exit(1)
 
signal.signal(signal.SIGINT, handler)
 

if __name__ == '__main__':
    
    imprimirMenu()
