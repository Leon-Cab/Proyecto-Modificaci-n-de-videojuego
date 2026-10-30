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
    """Dibuja el símbolo 'X' (Jugador 0) en la casilla correspondiente con color azul, grosor y centrado."""
    color('blue')      # Cambia el color a azul
    width(5)           # Define un grosor de línea de 5
    
    # Margen para centrar la X en la casilla de 133x133 sin tocar los bordes
    margin = 25
    
    # Dibuja la primera línea diagonal centrada
    up()
    goto(x + margin, y + margin)
    down()
    goto(x + 133 - margin, y + 133 - margin)
    
    # Dibuja la segunda línea diagonal centrada
    up()
    goto(x + margin, y + 133 - margin)
    down()
    goto(x + 133 - margin, y + margin)


def drawo(x, y):
    """Dibuja el símbolo 'O' (Jugador 1) en la casilla correspondiente con color rojo, grosor y centrado."""
    color('red')       # Cambia el color a rojo
    width(5)           # Define un grosor de línea de 5
    
    # Posiciona y dibuja el círculo exactamente en el centro de la casilla
    up()
    goto(x + 66.5, y + 20)  # Punto inferior central para el trazado del círculo
    down()
    circle(46.5)            # Radio ajustado para que quede perfectamente centrado


def floor(value):
    """Calcula la coordenada de la esquina inferior izquierda de la casilla presionada.
    Ajusta cualquier clic al centro de la cuadrícula de tamaño 133x133."""
    return ((value + 200) // 133) * 133 - 200


# 'state' guarda el estado actual del juego: el turno del jugador y las casillas ocupadas
state = {'player': 0, 'board': {}}

# Lista con las funciones encargadas de dibujar cada símbolo
players = [drawx, drawo]


def tap(x, y):
    """Maneja el evento del clic del usuario en la pantalla."""
    # Redondea las coordenadas del clic para alinearlas a la casilla más cercana
    x = floor(x)
    y = floor(y)
    
    # Valida si la casilla ya está ocupada; si es así, ignora la acción
    if (x, y) in state['board']:
        return
    
    # Obtiene el turno del jugador actual (0 o 1)
    player = state['player']
    
    # Registra la casilla como ocupada por el jugador actual
    state['board'][(x, y)] = player
    
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