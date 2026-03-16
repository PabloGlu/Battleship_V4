# Battleship V7 - Juego de Batalla Naval en Clases (Python)

## Descripción
Implementación orientada a objetos del clásico Battleship usando NumPy para tableros 10x10. El jugador compite contra una IA "Terminator". 
Cada barco se guarda como objeto único de la clase Barco, permitiendo rastrear toques individuales y anunciar hundimientos cuando todos sus segmentos son impactados.

## Características Principales
- **Coordenadas Incorrectas**: Si introduces una coordenada inválida (no dos dígitos 0-9), el sistema te asigna automáticamente una aleatoria con `missile()` para no perder turno.
- **Barcos como Objetos**: Cada barco (Giant=6, Carrier=5, Battleship=4, etc.) es un objeto único con coordenadas, hits y estado sunked; muestra "tocado" por segmento y "hundido" al completarse.
- **Whiteflag**: La máquina tiene 1% de probabilidad de rendirse aleatoriamente (dos randoms ==1 en 0-99).
- **Dificultades**:
  - Normal: Máquina tira 1 vez.
  - Difícil: Máquina tira 2 veces por turno (`dispararm1v2hard`).
- **Modos de Juego**:
  - Normal: Disparos manuales estándar.
  - Semiautomático: Disparo extra al acertar (jugador y máquina).
  - Automático: Colocación y lógica fully aleatoria (ver funciones disparar y create).

## Instalación y Uso
1. Instala NumPy: `pip install numpy`
2. Ejecuta: `python Battleship_V7_class.py`
3. Elige dificultad y modo al iniciar.
4. Ingresa coordenadas como "34" (fila 3, columna 4).

## Estructura de Clases
- **Player**: Tableros, barcos lista, disparos manuales.
- **Machine**: Similar, con lógica hard y whiteflag.
- **Barco**: Objetos por barco con hit/checksunked.

## Archivos
- `Battleship_V7_class.py`: Código principal.
- `Battleship_Test_Manual_V3_Class_Hard.py`: Test manual para modo difícil.

¡Diviértete hundiendo barcos!
