import numpy as np
import random

def crea_tablero(lado = 10):
    tablero = np.full((lado,lado)," ")
    return tablero

tablero = crea_tablero(10)
print(tablero)


# In[278]:


# Carrier: 5 spaces
# Battleship: 4 spaces
# Cruiser: 3 spaces
# Submarine: 3 spaces
# Destroyer: 2 spaces

## Disparo doble si Hit.
##  Hacer una opción para elegir tipo de juego (auto, semi, manual), elegir dificultad máquina (1, 2, 3).
### En automatico, poner un timeslip (1 segundo si agua, 5 segundos si hit).
### Tipo de juego: Cómo elegir el disparo, cada cuantos turnos participar (bucles con countdown)
### Elegir dificultad: 1 disparo por turno/ 2 disparos por turno/ 3 disparos por turno
### 
## Pintar juego y hacer interfaz


# In[279]:


def recibir_disparo(tablero_def, coordenada):
    if tablero_def[coordenada] == "O":
        tablero_def[coordenada] = "X"
        print("Te han dado")
    elif tablero_def[coordenada] == "X" or tablero_def[coordenada] == "_":
        print("Ha repetido un disparo. Estamos bien!")
    else:
        tablero_def[coordenada] = "_"
        print("Uff, menos mal")
    print(f"Tablero def \n {tablero_def}")
    print('*'*50)
    return tablero_def


# print(tablero_def)


# In[280]:


def recibir_disparo_p1(tablero_def, coordenada):
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


# In[281]:


def recibir_disparo_m1(tablero_def, coordenada):
    if tablero_def[coordenada] == "O":
        tablero_def[coordenada] = "X"
        print("M1! Bip Bup. Te han dado")
    elif tablero_def[coordenada] == "X" or tablero_def[coordenada] == "_":
        print("Pobre humano, repitió disparo")
    else:
        tablero_def[coordenada] = "_"
        print("Bip Bup Water")
    print(f"Tablero de defensa de M1 \n {tablero_def}")
    print('*'*50)
    return tablero_def


# In[282]:


# La funcion disparar tiene que llamar a la funcion recibir disparo

# # def disparar(tablero_at, tablero_def, coordenada):
# #     if tablero_def[coordenada] == "O":
# #         tablero_at[coordenada] = "H"
# #         print("Tocado")
# #     elif tablero_def[coordenada] == "X":
# #         print("Agonia, deja de perder el tiempo, dispara a otro sitio")


# #     else:
# #         tablero_at[coordenada] = 'W'
# #         print("Agua")
# #     recibir_disparo(tablero_def, coordenada)
# #     print(f"Tablero at \n {tablero_at}")
# #     print('*'*50)
# #     return(tablero_at)


# In[ ]:


def disparar_p1_manual(tablero_at, tablero_def):
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
            disparar_p1_esp(tablero_at, tablero_def, coordenada)
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
    recibir_disparo_m1(tablero_def, coordenada)
    print(f"Tablero de ataque de P1 \n {tablero_at}")
    print('*'*50)
    return(tablero_at)


# In[ ]:

def disparar_p1_esp(tablero_at, tablero_def, coordenada):
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
            disparar_p1_esp(tablero_at, tablero_def, coordenada)
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
    recibir_disparo_m1(tablero_def, coordenada)
    
    return(tablero_at)

## Tengo que actualizar semi

def disparar_p1_semi(tablero_at, tablero_def, coordenada):
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
            disparar_p1_esp(tablero_at, tablero_def, coordenada)
        except Exception as e:
            print(f"ERROR {e}. Me salto tu turno")

    elif tablero_def[coordenada] == "X":
        print("Agonia, la antesala de la muerte, deja de perder el tiempo, dispara a otro sitio")

    else:
        tablero_at[coordenada] = 'W'
        print("Agua, la maquina se ha librado")
    recibir_disparo_m1(tablero_def, coordenada)
    print(f"Tablero de ataque de P1 \n {tablero_at}")
    print('*'*50)
    return(tablero_at)


# In[ ]:


def disparar_p1(tablero_at, tablero_def, coordenada): # Full auto
    if tablero_def[coordenada] == "O":
        tablero_at[coordenada] = "H"
        print("P1, le has dado a la maquina!")

    elif tablero_def[coordenada] == "X":
        print("Agonia, la antesala de la muerte, deja de perder el tiempo, dispara a otro sitio")

    else:
        tablero_at[coordenada] = 'W'
        print("Agua, la maquina se ha librado")
    recibir_disparo_m1(tablero_def, coordenada)
    print(f"Tablero de ataque de P1 \n {tablero_at}")
    print('*'*50)
    return(tablero_at)


# In[ ]:


def disparar_m1(tablero_at, tablero_def, coordenada):
    if tablero_def[coordenada] == "O":
        tablero_at[coordenada] = "H"
        print("M1, bip bup, tocado!")

    elif tablero_def[coordenada] == "X":
        print("Agonia, bip bup, deja de perder el tiempo, dispara a otro sitio")

    else:
        tablero_at[coordenada] = 'W'
        print("Agua, bip bup")
    recibir_disparo_p1(tablero_def, coordenada)
    print(f"Tablero de ataque de la maquina \n {tablero_at}")
    print('*'*50)
    return(tablero_at)



# In[285]:


def coloca_barco_plus(tablero, barco):
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


# In[286]:


tab_def_p1 = crea_tablero(10)
tab_at_p1 = crea_tablero(10)
tab_def_m1 = crea_tablero(10)
tab_at_m1 = crea_tablero(10)


# In[287]:


def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 1000):
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
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        print("Tengo que intentar colocar otro barco")


# In[288]:


def create_p1_def():
    tab_def_p1 = crea_barco_aleatorio(tablero, eslora = 6)
    tab_def_p1 = crea_barco_aleatorio(tab_def_p1, eslora = 5)
    tab_def_p1 = crea_barco_aleatorio(tab_def_p1, eslora = 4)
    tab_def_p1 = crea_barco_aleatorio(tab_def_p1, eslora = 3)
    tab_def_p1 = crea_barco_aleatorio(tab_def_p1, eslora = 3)
    tab_def_p1 = crea_barco_aleatorio(tab_def_p1, eslora = 2)
    return tab_def_p1

def create_m1_def():
    tab_def_m1 = crea_barco_aleatorio(tablero, eslora = 6)
    tab_def_m1 = crea_barco_aleatorio(tab_def_m1, eslora = 5)
    tab_def_m1 = crea_barco_aleatorio(tab_def_m1, eslora = 4)
    tab_def_m1 = crea_barco_aleatorio(tab_def_m1, eslora = 3)
    tab_def_m1 = crea_barco_aleatorio(tab_def_m1, eslora = 3)
    tab_def_m1 = crea_barco_aleatorio(tab_def_m1, eslora = 2)
    return tab_def_m1



# In[289]:


# def create_p1_at():



# def create_m1_at():


# In[290]:


print(tablero) 


# In[291]:


create_p1_def()


# In[292]:


create_m1_def()


# In[293]:


# Generar una coordenada aleatoria

tuple_random = tuple(np.random.randint(0, 10, size=2))
print(tuple_random)


# In[294]:


def missile():
    missile = tuple(np.random.randint(0, 10, size=2))
    return missile


# In[295]:


tab_def_p1 = create_p1_def()

tab_def_m1 = create_m1_def()


# In[296]:


print(tab_def_p1)
print('*'*50)
print(tab_def_m1)


# In[299]:


# n = 1
# while True:
#     print(f'Turno {n}: Ataca el P1')
#     disparo_p1 = disparar_p1(tab_at_p1, tab_def_m1, missile())

#     if 'O' not in tab_def_m1:
#         print('JUGADOR 1 HAS GANADO')
#         break

#     print(f'Turno {n}: Ataca la maquina M1')
#     disparo_m1 = disparar_m1(tab_at_m1, tab_def_p1, missile())
#     n += 1

#     if 'O' not in tab_def_p1:
#         print('JUGADOR 1 HAS PERDIDO')
#         break

