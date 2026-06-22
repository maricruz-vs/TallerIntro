import pygame
import logica_1 as analisis

# parte grafica del proyecto hecha con pygame
#se dibuja el treemap los colores la leyenda y las listas

ANCHO = 1280
ALTO = 720

# niveles de profundidad que se dibujan como dice el pdf
MAX_NIVEL = 6


# arma una paleta de colores para diferenciar los elementos
def crear_colores():
    # devolver una lista de colores distintos
    return []

# dibuja un rectangulo del treemap
def dibujar_rect(pantalla, x, y, ancho, alto, color, nombre):
    # pygame.draw.rect y poner el nombre si cabe
    pass


# recursivo
def dibujar_treemap(pantalla, nodo, x, y, ancho, alto, nivel):
    # si paso el nivel maximo parar
    # repartir el espacio segun el tamano de cada hijo
    # llamar recursivamente a  dibujar_treemap para cada hijo
    pass


# escribe la lista de los 10 archivos mas grandes
def dibujar_lista_archivos(pantalla, archivos):
    # recorrer y escribir ruta nombre tamano
    pass


# escribe la lista de los 10 directorios con mas archivos
def dibujar_lista_directorios(pantalla, directorios):
    pass




def main():
    # pedir la carpeta al usuario
    # llamar al analisis del compañero
    # iniciar pygame y abrir la ventana
    # mensaje de bienvenida o titulo arriba
    # ciclo principal que dibuja y revisa eventos
    # cerrar bien cuando se sale
    pass


main()
