import pygame
import logica_1 as analisis

# parte grafica del proyecto hecha con pygame
#se dibuja el treemap los colores la leyenda y las dos listas

ANCHO = 1280
ALTO = 720

# niveles de profundidad que se dibujan como dice el pdf
MAX_NIVEL = 6

# area donde va el treemap, el resto es para titulo y listas
TREEMAP_X = 20
TREEMAP_Y = 60
TREEMAP_ANCHO = 800
TREEMAP_ALTO = 380

# colores fijos de la interfaz
FONDO = (30, 30, 40)
BLANCO = (240, 240, 240)
NEGRO = (0, 0, 0)


# arma una paleta de colores para diferenciar los elementos
def crear_colores():
    colores = []
    colores.append((220, 80, 80))
    colores.append((80, 180, 220))
    colores.append((120, 200, 120))
    colores.append((230, 180, 70))
    colores.append((180, 120, 220))
    colores.append((240, 140, 90))
    colores.append((90, 200, 190))
    colores.append((210, 100, 160))
    colores.append((150, 170, 90))
    colores.append((110, 140, 230))
    return colores


# escoge un color de la paleta segun la posicion
def color_para(indice, colores):
    return colores[indice % len(colores)]


# dibuja un rectangulo del treemap con su nombre si cabe
def dibujar_rect(pantalla, fuente, x, y, ancho, alto, color, nombre, tamano):
    # solo dibujar si el rectangulo tiene tamano visible
    if ancho < 1 or alto < 1:
        return
    rect = pygame.Rect(int(x), int(y), int(ancho), int(alto))
    pygame.draw.rect(pantalla, color, rect)
    pygame.draw.rect(pantalla, NEGRO, rect, 1)
    # poner el nombre solo si el rectangulo es suficientemente grande
    if ancho > 55 and alto > 18:
        texto = nombre + " " + analisis.formato_tamano(tamano)
        img = fuente.render(texto, True, NEGRO)
        # recortar el texto al ancho del rectangulo
        pantalla.set_clip(rect)
        pantalla.blit(img, (x + 3, y + 2))
        pantalla.set_clip(None)


# recursivo
def dibujar_treemap(pantalla, fuente, nodo, x, y, ancho, alto, nivel, colores):
    # si ya se llego al nivel maximo no se sigue dibujando hacia adentro
    if nivel >= MAX_NIVEL:
        return

    hijos = nodo["hijos"]
    if len(hijos) == 0:
        return

    total = nodo["tamano"]
    # si el nodo no tiene tamano no se puede repartir
    if total <= 0:
        return

    #para que se vea ordenado
    hijos = sorted(hijos, key=lambda h: h["tamano"], reverse=True)

    # se reparte el espacio alternando horizontal y vertical por nivel
    horizontal = (nivel % 2 == 0)
    desplazado = 0.0

    indice = 0
    for hijo in hijos:
        if hijo["tamano"] <= 0:
            continue
        # proporcion del hijo respecto al total del padre
        proporcion = hijo["tamano"]/total
        color =color_para(indice, colores)

        if horizontal:
            w = ancho*proporcion
            dibujar_rect(pantalla, fuente, x + desplazado, y, w, alto,
                         color, hijo["nombre"], hijo["tamano"])
            # dibujar lo de adentro un poco mas pequeno para ver el borde
            if hijo["es_carpeta"]:
                dibujar_treemap(pantalla, fuente, hijo,
                                x + desplazado + 2, y + 16, w - 4, alto - 18,
                                nivel + 1, colores)
            desplazado += w
        else:
            h = alto*proporcion
            dibujar_rect(pantalla, fuente, x, y + desplazado, ancho, h,
                         color, hijo["nombre"], hijo["tamano"])
            if hijo["es_carpeta"]:
                dibujar_treemap(pantalla, fuente, hijo,
                                x + 2, y + desplazado + 16, ancho - 4, h - 18,
                                nivel + 1, colores)
            desplazado += h
        indice = indice + 1


# escribe el titulo arriba con el nombre y tamano de la raiz
def dibujar_titulo(pantalla, fuente_grande, raiz):
    texto = "Graficador de espacio  -  " + raiz["nombre"]
    texto = texto + "  (" + analisis.formato_tamano(raiz["tamano"]) + ")"
    img = fuente_grande.render(texto, True, BLANCO)
    pantalla.blit(img, (20, 18))


# escribe la lista de los 10 archivos mas grandes
def dibujar_lista_archivos(pantalla, fuente, fuente_titulo, archivos):
    x = 850
    y = 60
    titulo = fuente_titulo.render("10 archivos mas grandes", True, BLANCO)
    pantalla.blit(titulo, (x, y))
    y = y + 26
    for a in archivos:
        # mostrar nombre y tamano la ruta completa va en la otra lista por espacio
        texto = a["nombre"]
        if len(texto) > 38:
            texto = texto[:38] + "..."
        texto = texto + "  " + analisis.formato_tamano(a["tamano"])
        img = fuente.render(texto, True, BLANCO)
        pantalla.blit(img, (x, y))
        y = y + 18


# escribe la lista de los 10 directorios con mas archivos
def dibujar_lista_directorios(pantalla, fuente, fuente_titulo, directorios):
    x = 850
    y = 400
    titulo = fuente_titulo.render("10 directorios con mas archivos", True, BLANCO)
    pantalla.blit(titulo, (x, y))
    y = y + 26
    for d in directorios:
        texto = d["nombre"]
        if len(texto) > 30:
            texto = texto[:30] + "..."
        texto = texto + "  (" + str(d["archivos_directos"]) + ")"
        img = fuente.render(texto, True, BLANCO)
        pantalla.blit(img, (x, y))
        y = y + 18


# dibuja una leyenda chica abajo del treemap
def dibujar_leyenda(pantalla, fuente, colores):
    x = TREEMAP_X
    y = TREEMAP_Y + TREEMAP_ALTO + 15
    nota = fuente.render("colores usados para separar elementos del treemap",
                         True, BLANCO)
    pantalla.blit(nota, (x, y))
    y = y + 20
    cx = x
    for c in colores:
        pygame.draw.rect(pantalla, c, pygame.Rect(cx, y, 24, 16))
        cx = cx + 30


# pide la carpeta y corre logica
def preparar_datos():
    ruta = input("ingrese la carpeta a analizar: ")
    if not analisis.es_carpeta(ruta):
        print("la ruta no es una carpeta valida")
        return None
    print("analizando... esto puede tardar segun el tamano")
    raiz = analisis.analizar(ruta)
    return raiz


def main():
    # pedir carpeta y analizar antes de abrir la ventana
    raiz = preparar_datos()
    if raiz is None:
        return

    # sacar los reportes una sola vez
    archivos = analisis.archivos_grandes(raiz)
    directorios = analisis.directorios_llenos(raiz)
    colores = crear_colores()

    # iniciar pygame y abrir la interfaz
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Graficador de espacio en disco")
    fuente = pygame.font.SysFont("consolas", 13)
    fuente_titulo = pygame.font.SysFont("consolas", 16, True)
    fuente_grande = pygame.font.SysFont("consolas", 22, True)

    # ciclo principal dibuja y revisa eventos
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            # cerrar la ventana
            if evento.type == pygame.QUIT:
                corriendo = False
            # salir tambien con la tecla escape
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    corriendo = False

        pantalla.fill(FONDO)
        dibujar_titulo(pantalla, fuente_grande, raiz)
        # dibujar el treemap dentro de su area
        dibujar_treemap(pantalla, fuente, raiz,
                        TREEMAP_X, TREEMAP_Y, TREEMAP_ANCHO, TREEMAP_ALTO,
                        0, colores)
        dibujar_leyenda(pantalla, fuente, colores)
        dibujar_lista_archivos(pantalla, fuente, fuente_titulo, archivos)
        dibujar_lista_directorios(pantalla, fuente, fuente_titulo, directorios)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
