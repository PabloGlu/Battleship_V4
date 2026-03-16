import pygame as py 
import sys
import numpy as np
import Battleship_Test as bp


py.init()
ANCHO, ALTO = 800, 600
screen = py.display.set_mode((ANCHO, ALTO))
py.display.set_caption("Battleship - Tu código NumPy aquí")
CELL_SIZE = 40  # Cuadrados 40px
reloj = py.time.Clock()

# Colores (RGB)
NEGRO = (0, 0, 0)
AZUL = (0, 100, 200)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

# Tu tablero NumPy (integra aquí)
tablero_def = np.full((10,10), " ")  # De tu código

def dibuja_tablero(screen, tablero, x, y):
    for i in range(10):
        for j in range(10):
            rect = py.Rect(x + j*CELL_SIZE, y + i*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = BLANCO
            if tablero[i,j] == "X": color = ROJO
            elif tablero[i,j] == "O": color = VERDE  # Oculto en juego real
            elif tablero[i,j] == "_": color = AZUL
            py.draw.rect(screen, color, rect)
            py.draw.rect(screen, NEGRO, rect, 2)  # Grid

if py.event.type == py.MOUSEBUTTONDOWN:
    coord = (row, col)
    tab_at_p1 = disparar(tab_at_p1, tab_def_m1, coord)
    py.display.flip()


running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            mx, my = py.mouse.get_pos()
            col = (mx - 50) // CELL_SIZE  # Tablero en (50,50)
            row = (my - 50) // CELL_SIZE
            if 0 <= row < 10 and 0 <= col < 10:
                print(f"Click en [{row},{col}]")  # Integra tu disparar()

    screen.fill(NEGRO)
    dibuja_tablero(screen, tablero_def, 50, 50)  # Tablero enemigo
    dibuja_tablero(screen, tab_at_p1, 450, 50)   # Tu tablero ataque
    py.display.flip()
    reloj.tick(60)  # 60 FPS

py.quit()
sys.exit()
