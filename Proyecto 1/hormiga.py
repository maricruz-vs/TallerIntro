import pygame
import easygui

def obtener_nueva_orientacion(orientacion_actual, tipo_giro):
    """Función que determina hacia dónde debe mirar la hormiga después de girar a la izquierda o a la derecha."""
    
    if tipo_giro == "L":
        if orientacion_actual == "arriba":
            return "izquierda"
        elif orientacion_actual == "abajo":
            return "derecha"
        elif orientacion_actual == "derecha":
            return "arriba"
        elif orientacion_actual == "izquierda":
            return "abajo"
            
    if tipo_giro == "R":
        if orientacion_actual == "arriba":
            return "derecha"
        elif orientacion_actual == "abajo":
            return "izquierda"
        elif orientacion_actual == "derecha":
            return "abajo"
        elif orientacion_actual == "izquierda":
            return "arriba"

def calcular_siguiente_posicion(orientacion, eje_x, eje_y):
    """Función que actualiza las coordenadas de la hormiga avanzando un paso en la dirección a la que está mirando."""
    
    if orientacion == "arriba":
        return eje_x, eje_y + 1
    elif orientacion == "abajo":
        return eje_x, eje_y - 1
    elif orientacion == "derecha":
        return eje_x + 1, eje_y
    elif orientacion == "izquierda":
        return eje_x - 1, eje_y

def obtener_siguiente_estado(indice_actual, secuencia_reglas):
    """Esta función calcula el siguiente índice de color de forma cíclica según la longitud de la cadena de reglas."""
    
    return (indice_actual + 1) % len(secuencia_reglas)

def crear_paleta_rgb(cantidad_colores):
    """Esta función genera una lista de colores RGB utilizando fórmulas matemáticas para diferenciar los estados."""
    
    paleta = []
    for valor in range(1, cantidad_colores + 1):
        rojo = int((valor * 107) % 256)
        verde = int((valor * 12) % 256)
        azul = int((valor * 26) % 256)
        if (rojo, verde, azul) not in paleta:
            paleta.append((rojo, verde, azul))
            
    return paleta

def inicializar_cuadricula(total_filas, total_columnas):
    """Función que crea y retorna una matriz llena de ceros."""
    
    cuadricula = [[0 for _ in range(total_columnas)] for _ in range(total_filas)]
    
    return cuadricula

def main():
    """Esta es la función principal que inicializa Pygame, pide los datos al usuario y corre el ciclo de animación."""
    
    patron_usuario = easygui.enterbox("Digita las reglas de la hormiga (ej. RLR):", "Automata Celular")
    if not patron_usuario: return
    patron_usuario = patron_usuario.upper()

    pygame.init()
    escala_pixel = 4
    limite_y = 150
    limite_x = 150

    ventana_simulacion = pygame.display.set_mode((limite_x * escala_pixel, limite_y * escala_pixel))
    pygame.display.set_caption("Generalizacion de la Hormiga")

    tablero_estados = inicializar_cuadricula(limite_y, limite_x)
    espectro_colores = crear_paleta_rgb(len(patron_usuario))

    pos_x = limite_x // 2
    pos_y = limite_y // 2
    orientacion_hormiga = "arriba"

    ventana_simulacion.fill(espectro_colores[0])
    simulacion_activa = True
    
    control_fps = pygame.time.Clock()

    while simulacion_activa:
        for evento_pygame in pygame.event.get():
            if evento_pygame.type == pygame.QUIT:
                simulacion_activa = False

        for _ in range(80): 
            pos_x = pos_x % limite_x
            pos_y = pos_y % limite_y
            
            estado_casilla = tablero_estados[pos_y][pos_x]
            letra_giro = patron_usuario[estado_casilla]
            
            estado_futuro = obtener_siguiente_estado(estado_casilla, patron_usuario)
            tablero_estados[pos_y][pos_x] = estado_futuro
            
            coord_y_dibujo = limite_y - 1 - pos_y
            pygame.draw.rect(ventana_simulacion, espectro_colores[estado_futuro], 
                             (pos_x * escala_pixel, coord_y_dibujo * escala_pixel, escala_pixel, escala_pixel))
            
            orientacion_hormiga = obtener_nueva_orientacion(orientacion_hormiga, letra_giro)
            pos_x, pos_y = calcular_siguiente_posicion(orientacion_hormiga, pos_x, pos_y)

        pygame.display.flip()
        control_fps.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
