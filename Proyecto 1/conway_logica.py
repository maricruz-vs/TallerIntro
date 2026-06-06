from random import randint
def generar_matriz(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]

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

def transicion_celula(estado, vecinos):
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos.
    Si estado == 0 y tiene 3 vecinos vivos --> viva
    Si estado == 1 y tiene menos de 2 vecinos vivos --> muere
    Si estado == 1 y tiene más de 3 vecinos vivos --> muere
    Cualquier otra combinación, el estado sigue igual."""
    if estado==0 and vecinos.count(1) == 3:
        return 1
    elif estado == 1 and vecinos.count(1)<2:
        return 0
    elif estado == 1 and vecinos.count(1)>3:
        return 0
    else:
        return estado

def transicion(M):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    nueva_matriz = []
    for f in range(len(M)):
        fila = []
        for c in range(len(M[0])):
            vecinos = obtener_vecinos(M, f, c)
            nuevo_estado = transicion_celula(M[f][c], vecinos)
            fila.append(nuevo_estado)
        nueva_matriz.append(fila)
    return nueva_matriz