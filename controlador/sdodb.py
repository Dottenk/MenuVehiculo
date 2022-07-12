import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def rellenarFilaArr(obj, arr):
    obj = list(obj.__dict__.values())
    row, col = arr.shape
    agregado = False
    for i in range(row):
        for j in range(col):
            if arr[i][j] == None:
                arr[i] = obj
                print(f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER}[Agregado]{bcolors().OKCYAN} {obj} {bcolors().HEADER}[Agregado] {bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
                agregado = True
                return agregado
            else:
                break
        if agregado == True:
            return agregado


def vaciarFilaArr(value, arr):
    row, col = arr.shape
    obj = np.empty([col],dtype=object)
    vaciado = False
    for i in range(row):
        for j in range(col):
            print(arr[i][j])
            if arr[i][j] == value:
                arr = np.delete(arr, i, 0)
                print(
                    f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER}[Eliminado]{bcolors().OKCYAN} {value} {bcolors().HEADER}[Eliminado] {bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
                vaciado = True
                return arr
                break
        if vaciado == True:
            break


def filter_where(arr, value):
    return arr[np.where(arr == value)]

def extraerFilaArr(value, arr, mssg):
    row, col = arr.shape
    obj = []
    extraido = False
    for i in range(row):
        for j in range(col):
            if arr[i][j] == value:
                obj = arr[i]
                if mssg == True:
                    print(f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER} [Extraido]{bcolors().OKCYAN} {obj} {bcolors().HEADER}[Extraido] {bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
                extraido = True
                break
        if extraido == True:
            break
    return obj

class ListasNp:
    #Variables Globales - Todas las listas que se deban inicializar
    arrVehiculos = np.empty([50, 7], dtype=object)
    arrVehiculos[0] = ["Camioneta","JGHF-98","Chevrolet",12000000,[None,None],"08/10/2014", "Cristian aguilar"]
    arrVehiculos[1] = ["Sedan", "ABCD-90", "Fiat", 17000000, [70000, "Exceso de velocidad"], "08/02/2022", "Matias Lesquia"]
    def __init__(self):
        self.arrVehiculos = self.arrVehiculos
        

    def setArrVehiculos(self, arr):
        self.arrVehiculos = arr
    
    def getArrVehiculos(self):
        return self.arrVehiculos
