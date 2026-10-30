from random import *
from turtle import *

from freegames import path

car = path('car.gif')

# MODIFICACIÓN: dimensiones del tablero configurables (antes eran fijas: 8x8 = 64 casillas).
# Para cambiar el número de casillas basta con modificar ROWS y COLUMNS.
# El total de casillas (ROWS * COLUMNS) debe ser par para poder formar pares.
ROWS = 6
COLUMNS = 6
TILE_SIZE = 50  # MODIFICACIÓN: tamaño en píxeles de cada casilla
assert (ROWS * COLUMNS) % 2 == 0, 'El número de casillas debe ser par'

# MODIFICACIÓN: medidas del tablero y desplazamiento para mantenerlo centrado
WIDTH = COLUMNS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE
ORIGIN_X = -WIDTH // 2  # esquina inferior izquierda del tablero (antes: -200)
ORIGIN_Y = -HEIGHT // 2

# MODIFICACIÓN: total de pares según el tamaño del tablero (antes: 32 fijo)
TOTAL_PAIRS = (ROWS * COLUMNS) // 2
tiles = list(range(TOTAL_PAIRS)) * 2
# Se agrega 'pairs' al estado para contar los pares descubiertos
state = {'mark': None, 'pairs': 0}
hide = [True] * len(tiles)  # MODIFICACIÓN: antes era [True] * 64


def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(TILE_SIZE)  # MODIFICACIÓN: antes era 50 fijo
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas (x, y) al índice de la ficha."""
    # MODIFICACIÓN: usa el origen y el número de columnas configurables
    return int((x - ORIGIN_X) // TILE_SIZE + ((y - ORIGIN_Y) // TILE_SIZE) * COLUMNS)


def xy(count):
    """Convierte el número de ficha a coordenadas (x, y)."""
    # MODIFICACIÓN: usa el origen y el número de columnas configurables
    return (count % COLUMNS) * TILE_SIZE + ORIGIN_X, (count // COLUMNS) * TILE_SIZE + ORIGIN_Y


def tap(x, y):
    """Actualiza la marca y las fichas ocultas según el clic."""
    # MODIFICACIÓN: se ignoran los clics fuera del tablero (por ejemplo,
    # en la zona del contador), que antes podían causar un error de índice
    if not (ORIGIN_X <= x < ORIGIN_X + WIDTH and ORIGIN_Y <= y < ORIGIN_Y + HEIGHT):
        return

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # Solo se cuenta el par si ambas fichas seguían ocultas,
        # así evitamos contar dos veces un par que ya había sido descubierto
        if hide[spot] and hide[mark]:
            state['pairs'] += 1  # Se suma un par descubierto

        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Dibuja la imagen, las fichas y el contador de pares."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(len(tiles)):  # MODIFICACIÓN: antes era range(64)
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Se despliega el contador de pares sobre el tablero
    # MODIFICACIÓN: la posición se calcula según el tamaño del tablero
    up()
    goto(ORIGIN_X, ORIGIN_Y + HEIGHT + 5)
    color('black')
    write('Pares descubiertos: {} / {}'.format(state['pairs'], TOTAL_PAIRS),
          font=('Arial', 16, 'bold'))

    # MODIFICACIÓN: se detecta que todos los cuadros fueron destapados
    # (ya no queda ninguna casilla oculta en la lista 'hide')
    if not any(hide):
        # Se despliega un mensaje debajo del tablero
        up()
        goto(ORIGIN_X, ORIGIN_Y - 25)
        color('green')
        write('¡Todos los cuadros fueron destapados!',
              font=('Arial', 14, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
# MODIFICACIÓN: el tamaño de la ventana se ajusta al tamaño del tablero
# (antes: setup(420, 500, 370, 0)); se deja espacio extra para el contador
setup(WIDTH + 20, HEIGHT + 60, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()