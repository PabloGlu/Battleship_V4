# Intento de pasar juego a clases
import numpy as np
import random
# import import_ipynb
# import Battleship_V5 as bs
import time

# Tab def, tab at, barcos, create tab, disparar, recibir disparo
class Player:
    
    def __init__(self):
        self.name = 'Player'
        self.tab_def_p1 = np.full((10,10)," ")
        self.tab_at_p1 = np.full((10,10)," ")
        self.barcos_p1 = []
        

    # def crea_tablero(self, lado = 10):
    #     tablero = np.full((lado,lado)," ")
    #     return tablero

    # tablero = crea_tablero(10)

    def coloca_barco_plus_p1(self,tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
        tablero_temp = tablero.copy()
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        for pieza in barco:
            fila = pieza[0]
            columna = pieza[1]
            if fila < 0  or fila >= num_max_filas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if columna <0 or columna>= num_max_columnas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if tablero[pieza] == "O" or tablero[pieza] == "X":
                print(f"No puedo poner la pieza {pieza} porque hay otro barco")
                return False
            tablero_temp[pieza] = "O"
        return tablero_temp

    def crea_barco_aleatorio_p1(self, tablero, eslora = 4, num_intentos = 1000):
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        
        while num_intentos > 0:
            barco = []
            # Construimos el hipotetico barco
            pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
            print("Pieza original:", pieza_original)
            barco.append(pieza_original)
            orientacion = random.choice(["N","S","O","E"])
            print("Con orientacion", orientacion)
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
            print("Tengo que intentar colocar otro barco")

    def create_p1_def(self):
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 6)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 5)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 4)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 3)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 3)
        self.tab_def_p1 = self.crea_barco_aleatorio_p1(self.tab_def_p1, eslora = 2)
        return self.tab_def_p1
    
    def disparar_p1_manual_v2(self, tablero_at, tablero_def, enemigo):
        d_list = []
        d = input(f'Dame una coordenada (2 números seguidos del 0 al 9) ')
        for x in d:
            d_list.append(int(x))

        coordenada = tuple(d_list)
            
        if tablero_def[coordenada] == "O":
            tablero_at[coordenada] = "H"
            print("P1, le has dado a la maquina!")
            print(tablero_at)
            d_list = []
            d = input(f'Has dado en el clavo en la coordenada ({coordenada[0]}, {coordenada[1]}). \n Dame otra coordenada: ')
            try:
                for x in d:
                    d_list.append(int(x))
                coordenada = tuple(d_list)
                self.disparar_p1_esp_v2(tablero_at, tablero_def, coordenada, enemigo)
            except Exception as e:
                print(f"ERROR {e}")
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
        print(f"Tablero de ataque de P1 \n {tablero_at}")
        print('*'*50)
        return(tablero_at)


# In[ ]:

    def disparar_p1_esp_v2(self, tablero_at, tablero_def, coordenada, enemigo):
        if tablero_def[coordenada] == "O":
            tablero_at[coordenada] = "H"
            print('*'*50)
            print(f"Tablero de ataque de P1 \n {tablero_at}")
            print('*'*50)
            print("P1, le has dado a la maquina! Pero que maquina!")
            d_list = []
            d = input(f'Has vuelto a dar en el clavo en la coordenada ({coordenada[0]},  {coordenada[1]}). \n Dame otra coordenada, campeon!')
            try:
                for x in d:
                    d_list.append(int(x))
                coordenada = tuple(d_list)
                self.disparar_p1_esp_v2(tablero_at, tablero_def, coordenada, enemigo)
            except Exception as e:
                print(f"ERROR {e}")

        elif tablero_def[coordenada] == "X":
            print("Agonia, la antesala de la muerte, eres especial pero dispara a otro sitio")
        elif tablero_def[coordenada] == " ":
            tablero_at[coordenada] = 'W'
            print("Agua, la maquina se ha librado, do better")
        elif tablero_def[coordenada] == "_":
            print("Agua, pero ya era agua. Estás bien?")
        else:
            print("¿Cuando llega aquí?")
        enemigo.recibir_disparo_m1_v2(tablero_def, coordenada)
        
        return(tablero_at)
    
    def recibir_disparo_p1(self, tablero_def, coordenada):
        if tablero_def[coordenada] == "O":
            tablero_def[coordenada] = "X"
            print("P1! Te han dado")
        elif tablero_def[coordenada] == "X" or tablero_def[coordenada] == "_":
            print("Ha repetido un disparo. Estamos bien!")
        else:
            tablero_def[coordenada] = "_"
            print("Uff, menos mal")
        print(f"Tablero de defensa de P1 \n {tablero_def}")
        print('*'*50)
        return tablero_def
    


class Machine:
    # Tab def, tab at, barcos, create tab, disparar, recibir disparo
    def __init__(self):
        self.name = 'Terminator'
        self.tab_def_m1 = np.full((10,10)," ")
        self.tab_at_m1 = np.full((10,10)," ")
    
    barcos_m1 = []

    def crea_tablero(self, lado = 10):
        tablero = np.full((lado,lado)," ")
        return tablero

    tablero = crea_tablero(10)

    def coloca_barco_plus_m1(self, tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
        tablero_temp = tablero.copy()
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        for pieza in barco:
            fila = pieza[0]
            columna = pieza[1]
            if fila < 0  or fila >= num_max_filas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if columna <0 or columna>= num_max_columnas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if tablero[pieza] == "O" or tablero[pieza] == "X":
                print(f"No puedo poner la pieza {pieza} porque hay otro barco")
                return False
            tablero_temp[pieza] = "O"
        return tablero_temp

    def crea_barco_aleatorio_m1(self, tablero, eslora = 4, num_intentos = 1000):
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        
        while num_intentos > 0:
            barco = []
            # Construimos el hipotetico barco
            pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
            print("Pieza original:", pieza_original)
            barco.append(pieza_original)
            orientacion = random.choice(["N","S","O","E"])
            print("Con orientacion", orientacion)
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
            tablero_temp = self.coloca_barco_plus_m1(tablero, barco)
            if type(tablero_temp) == np.ndarray:
                return tablero_temp
            print("Tengo que intentar colocar otro barco")

    def create_m1_def(self):
        self.tab_def_m1 = self.crea_barco_aleatorio_m1(self.tablero, eslora = 6)
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
        elif tablero_def[coordenada] == "X" or tablero_def[coordenada] == "_":
            print("Pobre humano")
        else:
            tablero_def[coordenada] = "_"
            print("Bip Bup, you just hit water")
        # print(f"Tablero de defensa de M1 \n {tablero_def}")
        print('*'*50)
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

        
   






