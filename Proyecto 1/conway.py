import pygame
from random import randint

def generar_matriz_aleatoria(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]

def generar_matriz_vacia(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con en 0."""
    return [[0 for c in range(columnas)] for f in range(filas)]

def obtener_vecinos(M, f, c):
    """Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M."""
    vecinos = []
    for df in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if df==0 and dc==0:
                continue
            nf = (f+df)%len(M)
            nc = (c+dc)%len(M[0])
            vecinos.append(M[nf][nc])

    return vecinos

def transicion_celula(estado, vecinos, reglas="B3/S23"):
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos y a las reglas Life-Like.

    Las reglas se expresan como "Bx/Sy", donde x son los
    vecinos que generan nacimiento y y son los vecinos que
    permiten supervivencia.

    Restricciones:
    1. Las reglas deben ser una cadena con el formato "Bx/Sy".  
    2. x e y deben ser dígitos entre 0 y 8, sin repeticiones.
    """
    regla = reglas.upper().replace(" ", "")
    if "/" not in regla:
        raise ValueError(f"Reglas inválidas: {reglas}")

    partes = regla.split("/", 1)
    if len(partes) != 2 or not partes[0].startswith("B") or not partes[1].startswith("S"):
        raise ValueError(f"Reglas inválidas: {reglas}")

    nacimiento = set()
    supervivencia = set()

    for ch in partes[0][1:]:
        if not ch.isdigit():
            raise ValueError(f"Reglas inválidas: {reglas}")
        n = int(ch)
        if n > 8:
            raise ValueError(f"Reglas inválidas: {reglas}")
        nacimiento.add(n)

    for ch in partes[1][1:]:
        if not ch.isdigit():
            raise ValueError(f"Reglas inválidas: {reglas}")
        n = int(ch)
        if n > 8:
            raise ValueError(f"Reglas inválidas: {reglas}")
        supervivencia.add(n)

    vivos = vecinos.count(1)
    if estado == 0:
        return 1 if vivos in nacimiento else 0
    return 1 if vivos in supervivencia else 0

def transicion(M, reglas="B3/S23"):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    nueva_matriz = []
    for f in range(len(M)):
        fila = []
        for c in range(len(M[0])):
            vecinos = obtener_vecinos(M, f, c)
            nuevo_estado = transicion_celula(M[f][c], vecinos, reglas)
            fila.append(nuevo_estado)
        nueva_matriz.append(fila)
    return nueva_matriz

tam = 10
filas = 50
columnas = 50
tick = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    M = generar_matriz_aleatoria(filas, columnas)
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))
    loop = True
    pausa = False
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]:
                    pausa = not pausa
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tam
                    c = x // tam
                    M[f][c] = (M[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tam, tam))
        if not pausa:
            M = transicion(M)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()