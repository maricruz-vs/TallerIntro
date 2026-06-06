import pygame
import pickle
import easygui
from random import randint

tam = 10
filas = 50
columnas = 50
tick = 10
reglas_actuales = "B3/S23"

def generar_matriz_aleatoria(filas, columnas):
    """Funcion que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[1 if randint(1, 100) <= 30 else 0 for c in range(columnas)] for f in range(filas)]

def generar_matriz_vacia(filas, columnas):
    """Funcion que retorna una matriz de las dimensiones
    especificadas con en 0."""
    return [[0 for c in range(columnas)] for f in range(filas)]

def obtener_vecinos(M, f, c):
    """Funcion que retorna una lista con los estados de
    los 8 vecinos de la celula en la posicion f, c de M."""
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
    """Retorna el nuevo estado de la celula de acuerdo
    al estado de sus vecinos y a las reglas Life-Like.

    Las reglas se expresan como "Bx/Sy", donde x son los
    vecinos que generan nacimiento y y son los vecinos que
    permiten supervivencia.

    Restricciones:
    1. Las reglas deben ser una cadena con el formato "Bx/Sy".  
    2. x e y deben ser digitos entre 0 y 8, sin repeticiones.
    """
    regla = reglas.upper().replace(" ", "")
    if "/" not in regla:
        raise ValueError(f"Reglas invalidas: {reglas}")

    partes = regla.split("/", 1)
    if len(partes) != 2 or not partes[0].startswith("B") or not partes[1].startswith("S"):
        raise ValueError(f"Reglas invalidas: {reglas}")

    nacimiento = set()
    supervivencia = set()

    for ch in partes[0][1:]:
        if not ch.isdigit():
            raise ValueError(f"Reglas invalidas: {reglas}")
        n = int(ch)
        if n > 8:
            raise ValueError(f"Reglas invalidas: {reglas}")
        nacimiento.add(n)

    for ch in partes[1][1:]:
        if not ch.isdigit():
            raise ValueError(f"Reglas invalidas: {reglas}")
        n = int(ch)
        if n > 8:
            raise ValueError(f"Reglas invalidas: {reglas}")
        supervivencia.add(n)

    vivos = vecinos.count(1)
    if estado == 0:
        return 1 if vivos in nacimiento else 0
    return 1 if vivos in supervivencia else 0

def transicion(M, reglas="B3/S23"):
    """Toma a la matriz completa y le aplica la funcion de
    transicion a cada celula con su propio vecindario y deja
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

def solicitar_parametros():
    """Solicita los parametros iniciales al usuario usando easygui"""
    global filas, columnas, tam, reglas_actuales
    
    mensaje = "Ingrese los parametros iniciales del Automata Celular"
    titulo = "Configuracion del Automata"
    
    campos = [
        "Numero de filas",
        "Numero de columnas", 
        "Tamano de las celdas (pixeles)",
        "Reglas (formato: Bx/Sy, ej: B3/S23)"
    ]
    
    valores = [str(filas), str(columnas), str(tam), reglas_actuales]
    respuestas = easygui.multenterbox(mensaje, titulo, campos, valores)
    
    if respuestas:
        try:
            filas = int(respuestas[0])
            columnas = int(respuestas[1])
            tam = int(respuestas[2])
            reglas_actuales = respuestas[3]
            return True
        except:
            easygui.msgbox("Error en los parametros. Usando valores por defecto.", "Error")
            return False
    return False

def guardar_estado(M, filename="automata_save.pkl"):
    """Guarda el estado completo en un archivo usando pickle"""
    datos = {
        'matriz': M,
        'filas': len(M),
        'columnas': len(M[0]),
        'tam': tam,
        'reglas': reglas_actuales
    }
    try:
        with open(filename, 'wb') as f:
            pickle.dump(datos, f)
        easygui.msgbox(f"Estado guardado en {filename}", "Guardado exitoso")
        return True
    except Exception as e:
        easygui.msgbox(f"Error al guardar: {e}", "Error")
        return False

def cargar_estado(filename="automata_save.pkl"):
    """Carga el estado completo desde un archivo usando pickle"""
    global tam, reglas_actuales, filas, columnas
    
    # Solicitar nombre del archivo
    nombre_archivo = easygui.enterbox("Ingrese el nombre del archivo a cargar (ej. automata_save.pkl):", 
                                      "Cargar estado", default=filename)
    if not nombre_archivo:
        return None
    
    try:
        with open(nombre_archivo, 'rb') as f:
            datos = pickle.load(f)
        tam = datos['tam']
        reglas_actuales = datos['reglas']
        filas = datos['filas']
        columnas = datos['columnas']
        easygui.msgbox(f"Estado cargado desde {nombre_archivo}", "Carga exitosa")
        return datos['matriz']
    except FileNotFoundError:
        easygui.msgbox(f"No se encontro el archivo {nombre_archivo}", "Error")
        return None
    except Exception as e:
        easygui.msgbox(f"Error al cargar: {e}", "Error")
        return None
    
def main():
    global tam, filas, columnas, tick, reglas_actuales
    
    # se solicitan parametros, si no se usan los valores por defecto
    if not solicitar_parametros():
        easygui.msgbox("Usando valores por defecto", "Informacion")
    
    pygame.init()
    clock = pygame.time.Clock()
    M = generar_matriz_aleatoria(filas, columnas)
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Juego de la Vida - Life-Like")
    loop = True
    pausa = False
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            
            if event.type == pygame.KEYDOWN:
                # Tecla espacio para pausar/continuar
                if event.key == pygame.K_SPACE:
                    pausa = not pausa
                
                # Tecla G para guardar
                elif event.key == pygame.K_g:
                    guardar_estado(M)
                
                # Tecla C para cargar
                elif event.key == pygame.K_c:
                    nueva_matriz = cargar_estado()
                    if nueva_matriz is not None:
                        M = nueva_matriz
                        # Actualizar dimensiones de la ventana
                        w, h = columnas * tam, filas * tam
                        window = pygame.display.set_mode((w, h))
                
                # Tecla R para reiniciar con valores aleatorios
                elif event.key == pygame.K_r:
                    M = generar_matriz_aleatoria(filas, columnas)
                
                # Tecla B para reiniciar con valores neutros (ceros)
                elif event.key == pygame.K_b:
                    M = generar_matriz_vacia(filas, columnas)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                f = y // tam
                c = x // tam
                if 0 <= f < filas and 0 <= c < columnas:
                    M[f][c] = (M[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        
        # Dibujar las celulas
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (25, 25, 112), (x, y, tam, tam))
        
        # Dibujar lineas de la cuadricula
        for f in range(filas + 1):
            pygame.draw.line(window, (40, 40, 40), (0, f * tam), (w, f * tam))
        for c in range(columnas + 1):
            pygame.draw.line(window, (40, 40, 40), (c * tam, 0), (c * tam, h))
        
        # Mostrar informacion en pantalla
        font = pygame.font.Font(None, 24)
        info_text = f"Reglas: {reglas_actuales} | {'PAUSADO' if pausa else 'EJECUTANDO'}"
        text = font.render(info_text, True, (255, 255, 255))
        window.blit(text, (10, 10))
        
        # Mostrar controles
        controles = font.render("ESPACIO: Pausa  G: Guardar  C: Cargar  R: Aleatorio  B: Limpiar", True, (200, 200, 200))
        window.blit(controles, (10, h - 25))
        
        if not pausa:
            M = transicion(M, reglas_actuales)
        
        pygame.display.update()
        clock.tick(tick)
    
    pygame.quit()

if __name__ == "__main__":
    main()