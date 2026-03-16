import import_ipynb

import Battleship_V7_class as bs

import time

from colorama import Fore, Style

p1 = bs.Player()
m1 = bs.Machine()


tab_def_p1 = bs.Player.create_p1_def(p1)
tab_def_m1 = bs.Machine.create_m1_def(m1)

print(Fore.CYAN + "\n  === INICIO DE PARTIDA ===" + Style.RESET_ALL)
print()
print(Fore.WHITE  + "  Jugador  vs  Terminator" + Style.RESET_ALL)
print(Fore.YELLOW + "  Tablero 10x10  ·  6 barcos por bando" + Style.RESET_ALL)
print(Fore.CYAN + "  Reglas:" + Style.RESET_ALL)
print("  · Si aciertas, disparas de nuevo")
print("  · La máquina siempre gana (más o menos)")
print("  · Hay un 1% de que el Terminator se rinda")
print()
bs.print_tablero(p1.tab_def_p1, "Tu flota (defensa)")
bs.print_tablero(p1.tab_at_p1,  "Tu radar (ataque)")
bs.print_tablero(m1.tab_def_m1,  "Por si quieres hacer trampas, el tablero de Terminator")

n = 1
    
while True:
    print(f'Turno {n}: Ataca el P1')
    disparo_p1 = p1.disparar_p1_manual_v2(p1.tab_at_p1, m1.tab_def_m1, m1)
    time.sleep(1)

    if 'O' not in m1.tab_def_m1:
        print('JUGADOR 1 HAS GANADO')
        break

    if m1.white_flag():
        print("LA MAQUINA SE RINDE")
        print('HAS GANADO')
        break

    print(f'Turno {n}: Ataca la maquina M1')
    disparo_m1 = m1.disparar_m1_v2_hard(m1.tab_at_m1, p1.tab_def_p1, m1.missile(), p1)
    n += 1
    time.sleep(1)

    if 'O' not in p1.tab_def_p1:
        print('JUGADOR 1 HAS PERDIDO')
        break

