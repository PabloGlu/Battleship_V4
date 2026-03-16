# Intento de pasar juego a clases

import numpy as np
import random
import time
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Resetea el color automáticamente tras cada print


def print_tablero(tablero, titulo="Tablero"):
    """
    Imprime un tablero numpy con colores:
      ' '  → fondo azul (agua vacía)
      'O'  → verde (barco intacto)
      'X'  → rojo (barco tocado/hundido)
      'H'  → rojo (impacto registrado en tablero de ataque)
      'W'  → azul oscuro (agua ya disparada)
      '_'  → azul oscuro (agua ya disparada, variante)
    """
    CELDA = {
        ' ':  Back.BLUE   + Fore.BLUE    + ' ~ ' + Style.RESET_ALL,
        'O':  Back.GREEN  + Fore.WHITE   + ' O ' + Style.RESET_ALL,
        'X':  Back.RED    + Fore.WHITE   + ' X ' + Style.RESET_ALL,
        'H':  Back.RED    + Fore.WHITE   + ' H ' + Style.RESET_ALL,
        'W':  Back.CYAN   + Fore.BLUE    + ' W ' + Style.RESET_ALL,
        '_':  Back.CYAN   + Fore.BLUE    + ' _ ' + Style.RESET_ALL,
    }

    print(f"\n{'='*35}")
    print(f"  {titulo}")
    print(f"{'='*35}")
    # Cabecera de columnas
    print("    " + "  ".join(str(i) for i in range(tablero.shape[1])))
    for i, fila in enumerate(tablero):
        fila_str = f" {i} |"
        for celda in fila:
            fila_str += CELDA.get(celda, f' {celda} ')
        print(fila_str)
    print()

# Tab def, tab at, barcos, create tab, disparar, recibir disparo
class Player:
    
    def __init__(self):
        """
        Esta función inicializa un objeto Player, asignando un nombre por defecto "Player", creando dos tableros numpy de 10x10 vacíos (uno para defensa y otro para ataque) y una lista vacía para almacenar los barcos del jugador como objetos únicos de la clase Barco.
        """
        self.name = 'Player'
        self.tab_def_p1 = np.full((10,10)," ")
        self.tab_at_p1 = np.full((10,10)," ")
        self.barcos_p1 = []
        

    def missile(self):
        """
        Genera y devuelve una coordenada aleatoria para disparo, simulando un misil con dos números enteros entre 0 y 9 usando numpy.random.randint; se usa cuando el jugador ingresa una coordenada incorrecta, asignándole automáticamente una para no perder el turno.
        """
        missile = tuple(np.random.randint(0, 10, size=2))
        return missile

    def coloca_barco_plus_p1(self,tablero, barco):
        """
        Intenta colocar un barco específico (lista de coordenadas) en el tablero de defensa del jugador verificando límites y solapamientos; si es posible, marca las posiciones con 'O' y devuelve el tablero actualizado, de lo contrario retorna False con un mensaje de error.
        """
        tablero_temp = tablero.copy()
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        for pieza in barco:
            fila = pieza[0]
            columna = pieza[1]
            if fila < 0  or fila >= num_max_filas:
                # print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if columna <0 or columna>= num_max_columnas:
                # print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if tablero[pieza] == "O" or tablero[pieza] == "X":
                # print(f"No puedo poner la pieza {pieza} porque hay otro barco")
                return False
            tablero_temp[pieza] = "O"
        return tablero_temp

    def crea_barco_aleatorio_p1(self, tablero, eslora = 4, num_intentos = 1000):
        """
        Genera un barco aleatorio de eslora dada en el tablero del jugador, probando hasta 1000 veces: elige posición inicial, orientación (N,S,O,E) y extiende coordenadas; usa colocabarcoplusp1 para validar y lo guarda en la lista de barcos si tiene éxito.
        """
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        
        while num_intentos > 0:
            barco = []
            # Construimos el hipotetico barco
            pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
            # print("Pieza original:", pieza_original)
            barco.append(pieza_original)
            orientacion = random.choice(["N","S","O","E"])
            # print("Con orientacion", orientacion)
            fila = pieza_original[0]
            columna = pieza_original[1]
            for i in range(eslora -1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion  == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                else:
                    columna -= 1
                pieza = (fila,columna)
                barco.append(pieza)
            tablero_temp = self.coloca_barco_plus_p1(tablero, barco)
            if type(tablero_temp) == np.ndarray:
                self.barcos_p1.append(barco)
                return tablero_temp
            # print("Tengo que intentar colocar otro barco")

    def create_p1_def(self):
        """
        Crea el tablero de defensa completo del jugador colocando secuencialmente barcos de esloras 6,5,4,3,3 y 2 de forma aleatoria mediante creabarcoaleatoriop1, actualizando el tablero cada vez y retornando el tablero final con posiciones 'O'.
        """
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 6)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 5)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 4)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 3)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 3)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 2)
        return self.tab_def_p1
    
    def disparar_p1_manual_v2(self, tablero_at, tablero_def, enemigo):
        """
        Maneja el disparo manual del jugador: solicita coordenadas, valida entrada y si falla asigna una aleatoria con missile; chequea impacto ('O'), agua (' ') o tocado previo ('X'), permite disparo extra en acierto y actualiza el tablero de ataque.
        """
        d_list = []
        d = input(f'Dame una coordenada (2 números seguidos del 0 al 9) ')
        try:
            for x in d:
                d_list.append(int(x))

            coordenada = tuple(d_list)
        except Exception as e:
                print(f"Pierdes el turno {e}, aprende a seguir instrucciones")
                coordenada = self.missile()
                print(f"Me has dado pena, tu nuevo turno es ({coordenada[0]},{coordenada[1]})")
                
        if tablero_def[coordenada] == "O":
            tablero_at[coordenada] = "H"
            print("P1, le has dado a la maquina!")
            print_tablero(tablero_at, "Tablero de ataque P1")
            enemigo.recibir_disparo_m1_v2_esp(tablero_def, coordenada)
            d_list = []
            d = input(f'Has dado en el clavo en la coordenada ({coordenada[0]}, {coordenada[1]}). \n Dame otra coordenada: ')
            try:
                for x in d:
                    d_list.append(int(x))
                coordenada = tuple(d_list)
                self.disparar_p1_esp_v2(tablero_at, tablero_def, coordenada, enemigo)
            except Exception as e:
                print(f"Pierdes el turno {e}, aprende a seguir instrucciones")
                coordenada = self.missile()
                print(f"Me has dado pena, tu nuevo turno es {coordenada}")
            
        elif tablero_def[coordenada] == "X":
            print("Agonia, la antesala de la muerte, deja de perder el tiempo, dispara a otro sitio")
        elif tablero_def[coordenada] == " ":
            tablero_at[coordenada] = 'W'
            print("Agua, la maquina se ha librado")
        elif tablero_def[coordenada] == "_":
            print("Agua, pero ya era agua. Que estás haciendo?")
        else:
            print("¿Cuando llega aquí?")
        enemigo.recibir_disparo_m1_v2(tablero_def, coordenada)
        print_tablero(tablero_at, "Tablero de ataque P1")
        print('*'*50)
        return(tablero_at)


# In[ ]:

    def disparar_p1_esp_v2(self, tablero_at, tablero_def, coordenada, enemigo):
        """
        Versión especial para disparos extras del jugador tras acierto: chequea impacto en tablero enemigo, actualiza con 'H' si tocado, permite otro disparo o asigna aleatorio en error, y maneja mensajes para 'X', agua o repeticiones.
        """
        if tablero_def[coordenada] == "O":
            tablero_at[coordenada] = "H"
            print('*'*50)
            print_tablero(tablero_at, "Tablero de ataque P1")
            print('*'*50)
            print("P1, le has dado a la maquina! Pero que maquina!")
            enemigo.recibir_disparo_m1_v2_esp(tablero_def, coordenada)
            d_list = []
            d = input(f'Has vuelto a dar en el clavo en la coordenada ({coordenada[0]},  {coordenada[1]}). \n Dame otra coordenada, campeon!')
            try:
                for x in d:
                    d_list.append(int(x))
                coordenada = tuple(d_list)
                self.disparar_p1_esp_v2(tablero_at, tablero_def, coordenada, enemigo)
            except Exception as e:
                print(f"Pierdes el turno {e}, aprende a seguir instrucciones")
                coordenada = self.missile()
                print(f"Me has dado pena, tu nuevo turno es {coordenada}")

        elif tablero_def[coordenada] == "X":
            print("Agonia, la antesala de la muerte, eres especial pero dispara a otro sitio")
        elif tablero_def[coordenada] == " ":
            tablero_at[coordenada] = 'W'
            print("Agua, la maquina se ha librado, do better")
        elif tablero_def[coordenada] == "_":
            print("Agua, pero ya era agua. Estás bien?")
        else:
            print("¿Cuando llega aquí?")
        # enemigo.recibir_disparo_m1_v2(tablero_def, coordenada)
        
        return(tablero_at)
    
    def recibir_disparo_p1(self, tablero_def, coordenada):
        """
        Procesa disparos recibidos en el tablero de defensa del jugador: marca impactos en barcos ('O' o 'X') con mensaje de toque, ignora repeticiones y agua previa, actualizando y mostrando el tablero.
        """
        if tablero_def[coordenada] == "O":
            tablero_def[coordenada] = "X"
            print("P1! Te han dado")
        elif tablero_def[coordenada] == "X" or tablero_def[coordenada] == "_":
            print("Ha repetido un disparo. Estamos bien!")
        else:
            tablero_def[coordenada] = "_"
            print("Uff, menos mal")
        print_tablero(tablero_def, "Tablero de defensa P1")
        print('*'*50)
        return tablero_def
    


class Machine:
    # Tab def, tab at, barcos, create tab, disparar, recibir disparo

    def __init__(self):
        """
        Inicializa la máquina "Terminator" con tableros de 10x10 vacíos y lista para barcos, similar al Player pero con lógica específica para colocación y disparos automáticos.
        """
        self.name = 'Terminator'
        self.tab_def_m1 = np.full((10,10)," ")
        self.tab_at_m1 = np.full((10,10)," ")
    
    barcos_m1 = []

    def crea_tablero(self, lado = 10):
        tablero = np.full((lado,lado)," ")
        return tablero

    tablero = crea_tablero(10)

    def coloca_barco_plus_m1(self, tablero, barco):
    
        tablero_temp = tablero.copy()
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        for pieza in barco:
            fila = pieza[0]
            columna = pieza[1]
            if fila < 0  or fila >= num_max_filas:
                # print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if columna <0 or columna>= num_max_columnas:
                # print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if tablero[pieza] == "O" or tablero[pieza] == "X":
                # print(f"No puedo poner la pieza {pieza} porque hay otro barco")
                return False
            tablero_temp[pieza] = "O"
        return tablero_temp

    def crea_barco_aleatorio_m1(self, tablero, eslora = 4, num_intentos = 1000):
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        
        while num_intentos > 0:
            barco = []
            barco_m1 = Barco(eslora, [])
            pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
            # print("Pieza original:", pieza_original)
            barco.append(pieza_original)
            orientacion = random.choice(["N","S","O","E"])
            # print("Con orientacion", orientacion)
            fila = pieza_original[0]
            columna = pieza_original[1]
            for i in range(eslora -1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion  == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                else:
                    columna -= 1
                pieza = (fila,columna)
                barco.append(pieza)
                barco_m1.add_coordinates(pieza)
            tablero_temp = self.coloca_barco_plus_m1(tablero, barco)
            self.barcos_m1.append(barco_m1)
            if type(tablero_temp) == np.ndarray:
                return tablero_temp
            # print("Tengo que intentar colocar otro barco")

    def create_m1_def(self):
        self.tab_def_m1 = self.crea_barco_aleatorio_m1(self.tab_def_m1, eslora = 6)
        self.tab_def_m1 = self.crea_barco_aleatorio_m1(self.tab_def_m1, eslora = 5)
        self.tab_def_m1 = self.crea_barco_aleatorio_m1(self.tab_def_m1, eslora = 4)
        self.tab_def_m1 = self.crea_barco_aleatorio_m1(self.tab_def_m1, eslora = 3)
        self.tab_def_m1 = self.crea_barco_aleatorio_m1(self.tab_def_m1, eslora = 3)
        self.tab_def_m1 = self.crea_barco_aleatorio_m1(self.tab_def_m1, eslora = 2)
        return self.tab_def_m1
    
    def missile(self):
        missile = tuple(np.random.randint(0, 10, size=2))
        return missile
    
    def recibir_disparo_m1_v2(self, tablero_def, coordenada):
        if tablero_def[coordenada] == "O":
            tablero_def[coordenada] = "X"
            # print("M1! Bip Bup. Te han dado")
            for barco in self.barcos_m1:
                if coordenada in barco.coordinates:
                        barco.hit(coordenada)
        elif tablero_def[coordenada] == "X" or tablero_def[coordenada] == "_":
            print("Pobre humano")
        else:
            tablero_def[coordenada] = "_"
            print("Bip Bup, you just hit water")
        print_tablero(tablero_def, "Tablero de defensa M1")
        print('*'*50)
        return tablero_def
    
    def recibir_disparo_m1_v2_esp(self, tablero_def, coordenada):
        if tablero_def[coordenada] == "O":
            tablero_def[coordenada] = "X"
            for barco in self.barcos_m1:
                if coordenada in barco.coordinates:
                        barco.hit(coordenada)
                        barco.check_sunked()
        return tablero_def

    
    def disparar_m1_v2(self, tablero_at, tablero_def, coordenada, enemigo):
        if tablero_def[coordenada] == "O":
            tablero_at[coordenada] = "H"
            print("M1, bip bup, tocado!")

        elif tablero_def[coordenada] == "X":
            print("Agonia, bip bup, deja de perder el tiempo, dispara a otro sitio")

        else:
            tablero_at[coordenada] = 'W'
            print("Agua, bip bup")
        enemigo.recibir_disparo_p1(tablero_def, coordenada)
        # print(f"Tablero de ataque de la maquina \n {tablero_at}")
        print('*'*50)
        return(tablero_at)
    
    def disparar_m1_v2_hard(self, tablero_at, tablero_def, coordenada, enemigo):
        if tablero_def[coordenada] != 'O':
            print(f'Tiro original ({coordenada[0]}, {coordenada[1]})')
            print('La maquina siempre gana, tiro otra vez')
            print('MUAHAHA')
            print('BIP BUP')
            new_coord = self.missile()
            self.disparar_m1_v2(tablero_at, tablero_def, new_coord, enemigo)
            if tablero_def[coordenada] == "O":
                tablero_at[coordenada] = "H"
                print("M1, bip bup, tocado!")
                enemigo.recibir_disparo_p1(tablero_def, coordenada)
                print('*'*50)
                return(tablero_at)
            
    def white_flag(self):
        """
        Función de rendición: genera dos números aleatorios 0-99 y retorna True solo si ambos son 1 (probabilidad ~1%), permitiendo que la máquina se rinda aleatoriamente.
        """
        lucky_num1 = random.randint(0, 99) # Probabilidad del 1%
        lucky_num2 = random.randint(0, 99)
        if lucky_num1 == lucky_num2:
            return True
        return False

        
class Barco:
    lenght_to_name = {
    6: "Giant",
    5: "Carrier",
    4: "Battleship", 
    3: "Cruiser",
    3: "Submarine",
    2: "Destroyer"
}
    def __init__(self, lenght, coordinates):
        """
        Inicializa cada barco como objeto único con eslora, lista de coordenadas, hits=0, sunked=False y nombre basado en eslora (Giant, Carrier, etc.).
        """
        self.lenght = lenght
        self.coordinates = coordinates
        self.hits = 0
        self.sunked = False
        self.name = self.lenght_to_name[self.lenght]

    def create_boat (self, lenght):
        setattr(lenght)

    def add_coordinates(self, coordinate):
        self.coordinates.append(coordinate)

    def hit(self, coordinates):
        """
        Registra un impacto en coordenada específica del barco si existe, incrementa hits, imprime "tocado" y chequea hundimiento.
        """
        if coordinates in self.coordinates:
            self.hits += 1
            print(f'{self.name} tocado.')
            self.check_sunked()

    def check_sunked(self):
        """
        Verifica si hits >= eslora, marca sunked=True e imprime "Barco [nombre] hundido" para mostrar estado tocado/hundido.
        """
        if self.hits >= self.lenght:
            self.sunked = True
            print(f"Barco {self.name} hundido")

   






