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


def correctAttr(attr, typ, attrname, objname): 
    currentType = type(attr)
    try:
        if isinstance(attr, typ):
            return True
        else:
            raise AttributeError()
    except AttributeError:
        print(f"{bcolors().FAIL}[✘]{bcolors().HEADER}[{objname}]{bcolors().FAIL} El atributo '{attrname}' no corresponde al tipo ingresado {attr} ({currentType}). Debe ser una instancia de {typ} {bcolors().HEADER}[{objname}]{bcolors().FAIL}[✘]{bcolors().ENDC}")
        return False

class Vehiculo:

    def __init__(self, tipo, patente, marca, precio, multas, fechareg, nomDueño):
        try:
            if correctAttr(tipo, str, attrname='Tipo', objname="Vehiculo"):
                self.tipo = tipo
            else:
                raise AttributeError
            if correctAttr(patente, str, attrname='Patente', objname="Vehiculo"):
                self.patente = patente
            else:
                raise AttributeError
            if correctAttr(marca, str, attrname='Marca', objname="Vehiculo"):
                self.marca = marca
            else:
                raise AttributeError
            if correctAttr(precio, int, attrname='Precio', objname="Vehiculo"):
                self.precio = precio
            else:
                raise AttributeError
            if correctAttr(multas, list, attrname='Multas', objname="Vehiculo"):
                self.multas = multas
            else:
                raise AttributeError
            if correctAttr(fechareg, str, attrname='Fecha Registro', objname="Vehiculo"):
                self.fechareg = fechareg
            else:
                raise AttributeError
            if correctAttr(nomDueño, str, attrname='Nombre Dueño', objname="Vehiculo"):
                self.nomDueño = nomDueño
            else:
                raise AttributeError
            print(f"{bcolors().OKGREEN}[✓]{bcolors().ENDC} {bcolors().OKCYAN}{bcolors().HEADER}[Vehiculo] {bcolors().OKCYAN}Creado correctamente {bcolors().HEADER}[Vehiculo]{bcolors().ENDC} {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
        except AttributeError as er:
            print(f"{bcolors().FAIL}[✘]{bcolors().HEADER}[Vehiculo]{bcolors().ENDC} {bcolors().FAIL}No se pudo inicializar paciente. Comprueba que los datos estén correctamente ingresados{bcolors().FAIL} {bcolors().HEADER}[Vehiculo]{bcolors().FAIL}[✘]{bcolors().ENDC}")

    def contructor(self):
        self.tipo = ""
        self.patente = ""
        self.marca = ""
        self.precio = 0
        self.multas = []
        self.fechareg = ""
        self.nomDueño = ""

    def imprimirDatosVehiculo(self):    
    
        print(" ______________________________________________________________________________")
        print("|------------------------------------------------------------------------------|")
        print("|\n|-------------------------INFORMACION VEHICULO-------------------------------|")
        print(f"|--------------------------NUMERO DE PATENTE {self.patente}--------------------------------|")
        print(
            f"|\n|                        Vehiculo de {self.nomDueño}                             |\n|")
        print("|------------------------------------------------------------------------------|")
        print(
            f"|   Fecha de registro: {self.fechareg}                                                     |\n|")
        print(
            f"|                                                                                   |\n|\n|")
        print("|------------------------------------------------------------------------------|\n|")
        print(f"|   DETALLE\n|")
        print("|------------------------------------------------------------------------------|")
        print(
            f"|                                                                                   |")
        print(
            f"|   Tipo:         {self.tipo}                                                    |\n|")
        print(
            f"|   Patente:       {self.patente}                                                     |\n|")
        print(
            f"|   Marca:            {self.marca}                          |\n|")
        print(
            f"|   Precio:   {self.precio}                                                   |\n|")
        print(
            f"|   Multas     Monto:{self.multas[0]}    |   Fecha: {self.multas[1]}        |\n|")
        print("|------------------------------------------------------------------------------|")
        print(" ______________________________________________________________________________")