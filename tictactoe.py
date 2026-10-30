"""Tic Tac Toe
Editado por Max Karol de Jesus Bruno (A01714206)

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

# Importa todas las funciones de la librería gráfica Turtle para dibujar en pantalla
from turtle import *

# Importa la función 'line' del módulo freegames para trazar líneas rápidamente
from freegames import line


def grid():
    """Dibuja la cuadrícula del tablero de juego (tres por tres)."""
    # Dibuja las dos líneas verticales para dividir el tablero en 3 columnas
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    
    # Dibuja las dos líneas horizontales para dividir el tablero en 3 filas
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el símbolo 'X' (Jugador 0) en la casilla correspondiente."""
    # Dibuja la primera línea diagonal (de abajo-izquierda a arriba-derecha)
    line(x, y, x + 133, y + 133)
    # Dibuja la segunda línea diagonal (de arriba-izquierda a abajo-derecha)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Dibuja el símbolo 'O' (Jugador 1) en la casilla correspondiente."""
    up()  # Levanta el lápiz para no dejar rastro al mover la tortuga
    goto(x + 67, y + 5)  # Se posiciona en la base donde trazará el círculo
    down()  # Baja el lápiz para empezar a dibujar
    circle(62)  # Dibuja un círculo de radio 62 unidades


def floor(value):
    """Calcula la coordenada de la esquina inferior izquierda de la casilla presionada.
    Ajusta cualquier clic al centro de la cuadrícula de tamaño 133x133."""
    return ((value + 200) // 133) * 133 - 200


# 'state' guarda el estado actual del juego. 'player' 0 representa la X, y 1 representa el O.
state = {'player': 0}

# Lista con las funciones encargadas de dibujar cada símbolo
players = [drawx, drawo]


def tap(x, y):
    """Maneja el evento del clic del usuario en la pantalla."""
    # Redondea las coordenadas del clic para alinearlas a la casilla más cercana
    x = floor(x)
    y = floor(y)
    
    # Obtiene el turno del jugador actual (0 o 1)
    player = state['player']
    
    # Selecciona la función de dibujo correspondiente (drawx o drawo)
    draw = players[player]
    
    # Ejecuta el dibujo del símbolo en la casilla alineada
    draw(x, y)
    
    # Refresca el lienzo para mostrar los cambios en pantalla
    update()
    
    # Cambia de turno: de 0 (falso) a 1 (verdadero) o viceversa
    state['player'] = not player


# Configuración de la ventana gráfica (ancho: 420, alto: 420, posición X: 370, posición Y: 0)
setup(420, 420, 370, 0)

# Oculta el icono del puntero/flecha de Turtle
hideturtle()

# Desactiva la animación automática para que el dibujo sea instantáneo
tracer(False)

# Dibuja las líneas iniciales del tablero
grid()

# Actualiza la pantalla para visualizar el tablero dibujado
update()

# Asocia el evento del clic del ratón con la función 'tap'
onscreenclick(tap)

# Mantiene la ventana abierta esperando las interacciones del usuario
done()