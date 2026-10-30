# Proyecto-Modificacion-de-videojuego

# Pacman: juego y modificaciones

## Juego original

Pacman hecho en Python con `turtle` y `freegames`. Pacman se mueve con las flechas, come puntos y evita a 4 fantasmas; si uno lo toca, el juego termina.

- **Tablero:** lista `tiles` de 400 valores (20x20 casillas de 20 px). `0` = pared, `1` = camino con comida, `2` = camino sin comida.
- **Pacman:** vector `pacman` con su posición y `aim` con su dirección (avanza 5 px por ciclo).
- **Fantasmas:** lista `ghosts`, cada uno con posición y dirección (5 px por ciclo). Al chocar con una pared eligen una dirección al azar.
- **Funciones clave:** `world()` dibuja el tablero y la comida, `move()` es el ciclo principal (cada 100 ms) y `valid()` revisa que no haya paredes.

## Modificaciones (acumulativas)

### Versión 1: nuevo tablero
Se reemplazó `tiles` por un laberinto más ancho (17x17), simétrico y con una cámara central. Mantiene los 400 valores para no tocar el resto del código, y Pacman y los fantasmas inician en caminos válidos.

### Versión 2: nueva comida
Se agregó la función `food(x, y)`, que dibuja la comida como un **rombo naranja**, y `world()` la usa en lugar del punto blanco. Al terminar, `food()` devuelve el color de `path` a azul para que `square()` siga funcionando.

### Versión 3: fantasmas más rápidos
La velocidad de los fantasmas pasó de 5 a **10 px por ciclo**, tanto en `ghosts` como en `options` dentro de `move()`. Ahora van al doble de velocidad que Pacman. El valor debe dividir a 20 para no desalinearse de la cuadrícula.

## Resumen

| Versión | Archivo | Cambio acumulado |
|---|---|---|
| Original | `pacman.py` | Juego base |
| 1 | `pacman_v1.py` | Tablero nuevo |
| 2 | `pacman_v2.py` | + comida en rombo naranja |
| 3 | `pacman_v3.py` | + fantasmas al doble de velocidad |
