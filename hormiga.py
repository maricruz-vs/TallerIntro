import pygame
import pickle
import easygui
from random import randint

def obtener_nueva_orientacion(orientacion_actual, tipo_giro):
    """Funcion que determina hacia donde debe mirar la hormiga despues de girar a la izquierda o a la derecha."""
    
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
    """Funcion que actualiza las coordenadas de la hormiga avanzando un paso en la direccion a la que esta mirando."""
    
    if orientacion == "arriba":
        return eje_x, eje_y + 1
    elif orientacion == "abajo":
        return eje_x, eje_y - 1
    elif orientacion == "derecha":
        return eje_x + 1, eje_y
    elif orientacion == "izquierda":
        return eje_x - 1, eje_y

def obtener_siguiente_estado(indice_actual, secuencia_reglas):
    """Esta funcion calcula el siguiente indice de color de forma ciclica segun la longitud de la cadena de reglas."""
    
    return (indice_actual + 1) % len(secuencia_reglas)

def crear_paleta_rgb(cantidad_colores):
    """Esta funcion genera una lista de colores RGB utilizando formulas matematicas para diferenciar los estados."""
    
    paleta = []
    for valor in range(1, cantidad_colores + 1):
        rojo = int((valor * 107) % 256)
        verde = int((valor * 12) % 256)
        azul = int((valor * 26) % 256)
        if (rojo, verde, azul) not in paleta:
            paleta.append((rojo, verde, azul))
            
    return paleta

def inicializar_cuadricula(total_filas, total_columnas):
    """Funcion que crea y retorna una matriz llena de ceros."""
    
    cuadricula = [[0 for _ in range(total_columnas)] for _ in range(total_filas)]
    
    return cuadricula

def solicitar_parametros():
    """Solicita los parametros iniciales al usuario usando easygui"""
    global limite_filas, limite_columnas, escala_pixel, reglas_hormiga
    
    mensaje = "Ingrese los parametros iniciales del Automata Celular (Hormiga de Langton)"
    titulo = "Configuracion del Automata"
    
    campos = [
        "Numero de filas",
        "Numero de columnas", 
        "Tamano de las celdas (pixeles)",
        "Reglas de la hormiga (ej. RLR o LLRR)"
    ]
    
    valores = [str(limite_filas), str(limite_columnas), str(escala_pixel), reglas_hormiga]
    
    respuestas = easygui.multenterbox(mensaje, titulo, campos, valores)
    
    if respuestas:
        try:
            limite_filas = int(respuestas[0])
            limite_columnas = int(respuestas[1])
            escala_pixel = int(respuestas[2])
            reglas_hormiga = respuestas[3].upper()
            return True
        except:
            easygui.msgbox("Error en los parametros. Usando valores por defecto.", "Error")
            return False
    return False

def guardar_estado(tablero_estados, pos_x, pos_y, orientacion_hormiga, filename="hormiga_save.pkl"):
    """Guarda el estado completo en un archivo usando pickle"""
    global limite_filas, limite_columnas, escala_pixel, reglas_hormiga, espectro_colores
    
    datos = {
        'tablero': tablero_estados,
        'pos_x': pos_x,
        'pos_y': pos_y,
        'orientacion': orientacion_hormiga,
        'filas': limite_filas,
        'columnas': limite_columnas,
        'escala': escala_pixel,
        'reglas': reglas_hormiga,
        'paleta': espectro_colores
    }
    try:
        with open(filename, 'wb') as f:
            pickle.dump(datos, f)
        easygui.msgbox(f"Estado guardado en {filename}", "Guardado exitoso")
        return True
    except Exception as e:
        easygui.msgbox(f"Error al guardar: {e}", "Error")
        return False

def cargar_estado(filename="hormiga_save.pkl"):
    """Carga el estado completo desde un archivo usando pickle"""
    global limite_filas, limite_columnas, escala_pixel, reglas_hormiga, espectro_colores
    try:
        with open(filename, 'rb') as f:
            datos = pickle.load(f)
        limite_filas = datos['filas']
        limite_columnas = datos['columnas']
        escala_pixel = datos['escala']
        reglas_hormiga = datos['reglas']
        espectro_colores = datos['paleta']
        easygui.msgbox(f"Estado cargado desde {filename}", "Carga exitosa")
        return datos
    except FileNotFoundError:
        easygui.msgbox(f"No se encontro el archivo {filename}", "Error")
        return None
    except Exception as e:
        easygui.msgbox(f"Error al cargar: {e}", "Error")
        return None

def reiniciar_aleatorio():
    """Reinicia la matriz con valores aleatorios"""
    global limite_filas, limite_columnas, reglas_hormiga
    tablero = [[randint(0, len(reglas_hormiga)-1) for _ in range(limite_columnas)] for _ in range(limite_filas)]
    return tablero

def reiniciar_neutro():
    """Reinicia la matriz con valores neutros (ceros)"""
    global limite_filas, limite_columnas
    return [[0 for _ in range(limite_columnas)] for _ in range(limite_filas)]

def main():
    """Esta es la funcion principal que inicializa Pygame, pide los datos al usuario y corre el ciclo de animacion."""
    
    global limite_filas, limite_columnas, escala_pixel, reglas_hormiga, espectro_colores
    
    # Variables globales para la configuracion
    limite_filas = 150
    limite_columnas = 150
    escala_pixel = 4
    reglas_hormiga = "RLR"
    
    # Solicitar parametros al inicio
    if not solicitar_parametros():
        easygui.msgbox("Usando valores por defecto", "Informacion")

    pygame.init()
    
    ventana_simulacion = pygame.display.set_mode((limite_columnas * escala_pixel, limite_filas * escala_pixel))
    pygame.display.set_caption("Generalizacion de la Hormiga - Langton's Ant")
    
    tablero_estados = inicializar_cuadricula(limite_filas, limite_columnas)
    espectro_colores = crear_paleta_rgb(len(reglas_hormiga))
    
    pos_x = limite_columnas // 2
    pos_y = limite_filas // 2
    orientacion_hormiga = "arriba"
    
    ventana_simulacion.fill(espectro_colores[0])
    simulacion_activa = True
    pausa = False
    velocidad = 80  # Pasos por frame
    
    control_fps = pygame.time.Clock()

    while simulacion_activa:
        for evento_pygame in pygame.event.get():
            if evento_pygame.type == pygame.QUIT:
                simulacion_activa = False
            
            if evento_pygame.type == pygame.KEYDOWN:
                # Tecla espacio para pausar/continuar
                if evento_pygame.key == pygame.K_SPACE:
                    pausa = not pausa
                
                # Tecla G para guardar
                elif evento_pygame.key == pygame.K_g:
                    guardar_estado(tablero_estados, pos_x, pos_y, orientacion_hormiga)
                
                # Tecla C para cargar
                elif evento_pygame.key == pygame.K_c:
                    datos_cargados = cargar_estado()
                    if datos_cargados is not None:
                        tablero_estados = datos_cargados['tablero']
                        pos_x = datos_cargados['pos_x']
                        pos_y = datos_cargados['pos_y']
                        orientacion_hormiga = datos_cargados['orientacion']
                        # Actualizar dimensiones de la ventana
                        ventana_simulacion = pygame.display.set_mode((limite_columnas * escala_pixel, limite_filas * escala_pixel))
                        # Redibujar todo el tablero
                        ventana_simulacion.fill(espectro_colores[0])
                        for fila in range(limite_filas):
                            for columna in range(limite_columnas):
                                color = espectro_colores[tablero_estados[fila][columna]]
                                coord_y_dibujo = limite_filas - 1 - fila
                                pygame.draw.rect(ventana_simulacion, color, 
                                               (columna * escala_pixel, coord_y_dibujo * escala_pixel, escala_pixel, escala_pixel))
                        pygame.display.flip()
                
                # Tecla R para reiniciar con valores aleatorios
                elif evento_pygame.key == pygame.K_r:
                    tablero_estados = reiniciar_aleatorio()
                    pos_x = limite_columnas // 2
                    pos_y = limite_filas // 2
                    orientacion_hormiga = "arriba"
                    # Redibujar todo el tablero
                    ventana_simulacion.fill(espectro_colores[0])
                    for fila in range(limite_filas):
                        for columna in range(limite_columnas):
                            color = espectro_colores[tablero_estados[fila][columna]]
                            coord_y_dibujo = limite_filas - 1 - fila
                            pygame.draw.rect(ventana_simulacion, color, 
                                           (columna * escala_pixel, coord_y_dibujo * escala_pixel, escala_pixel, escala_pixel))
                    pygame.display.flip()
                
                # Tecla B para reiniciar con valores neutros (ceros)
                elif evento_pygame.key == pygame.K_b:
                    tablero_estados = reiniciar_neutro()
                    pos_x = limite_columnas // 2
                    pos_y = limite_filas // 2
                    orientacion_hormiga = "arriba"
                    # Redibujar todo el tablero
                    ventana_simulacion.fill(espectro_colores[0])
                    for fila in range(limite_filas):
                        for columna in range(limite_columnas):
                            color = espectro_colores[tablero_estados[fila][columna]]
                            coord_y_dibujo = limite_filas - 1 - fila
                            pygame.draw.rect(ventana_simulacion, color, 
                                           (columna * escala_pixel, coord_y_dibujo * escala_pixel, escala_pixel, escala_pixel))
                    pygame.display.flip()
            
            if evento_pygame.type == pygame.MOUSEBUTTONDOWN and evento_pygame.button == 1:
                # Cambiar estado de la celula con clic del mouse
                x, y = pygame.mouse.get_pos()
                columna = x // escala_pixel
                fila = y // escala_pixel
                if 0 <= fila < limite_filas and 0 <= columna < limite_columnas:
                    # Convertir coordenadas de pantalla a coordenadas del tablero
                    fila_tablero = limite_filas - 1 - fila
                    estado_actual = tablero_estados[fila_tablero][columna]
                    nuevo_estado = (estado_actual + 1) % len(reglas_hormiga)
                    tablero_estados[fila_tablero][columna] = nuevo_estado
                    # Dibujar la celda actualizada
                    pygame.draw.rect(ventana_simulacion, espectro_colores[nuevo_estado], 
                                   (columna * escala_pixel, fila * escala_pixel, escala_pixel, escala_pixel))
                    pygame.display.update()

        if not pausa:
            for _ in range(velocidad): 
                pos_x = pos_x % limite_columnas
                pos_y = pos_y % limite_filas
                
                estado_casilla = tablero_estados[pos_y][pos_x]
                letra_giro = reglas_hormiga[estado_casilla]
                
                estado_futuro = obtener_siguiente_estado(estado_casilla, reglas_hormiga)
                tablero_estados[pos_y][pos_x] = estado_futuro
                
                coord_y_dibujo = limite_filas - 1 - pos_y
                pygame.draw.rect(ventana_simulacion, espectro_colores[estado_futuro], 
                               (pos_x * escala_pixel, coord_y_dibujo * escala_pixel, escala_pixel, escala_pixel))
                
                orientacion_hormiga = obtener_nueva_orientacion(orientacion_hormiga, letra_giro)
                pos_x, pos_y = calcular_siguiente_posicion(orientacion_hormiga, pos_x, pos_y)
        
        # Mostrar informacion en pantalla
        font = pygame.font.Font(None, 24)
        info_text = f"Reglas: {reglas_hormiga} | {'PAUSADO' if pausa else 'EJECUTANDO'}"
        text = font.render(info_text, True, (255, 255, 255))
        ventana_simulacion.blit(text, (10, 10))
        
        # Mostrar controles
        controles = font.render("ESPACIO:Pausa  G:Guardar  C:Cargar  R:Aleatorio  B:Limpiar  Click:Celda", True, (200, 200, 200))
        ventana_simulacion.blit(controles, (10, limite_filas * escala_pixel - 25))
        
        pygame.display.flip()
        control_fps.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()