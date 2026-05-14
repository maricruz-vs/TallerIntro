alfabeto ="abcdefghijklmnñopqrstuvwxyz"

########################################################################################################
# Funciones auxiliares

#esto antes era revisionTexto
def normalizar_texto(texto):
    """
    Normaliza el texto: minúsculas, reemplaza acentos, elimina caracteres no alfabéticos (excepto espacios).
    Entradas: texto (str)
    Salidas: str normalizado
    Restricciones: texto debe ser string no vacío
    """
    if type(texto) !=str:
        raise Exception("El texto debe ser un string")
    if len(texto.strip()) ==0:
        raise Exception("El texto no puede estar vacío")
    
    #aqui las hace minusculas
    texto =texto.lower()
    resultado =[]
    for c in texto:
        #quita tildes
        if c in "á":
            c ="a"
        elif c in "é":
            c ="e"
        elif c in "í":
            c ="i"
        elif c in "ó":
            c ="o"
        elif c in "ú":
            c ="u"
        # conserva letras del alfabeto (incluyendo ñ) y espacios
        if c in alfabeto or c ==" ":
            resultado.append(c)
    return "".join(resultado)

def normalizar_palabra_clave(palabra):
    """
    Normaliza la palabra clave: minúsculas, sin acentos, elimina letras repetidas,
    conserva solo letras del alfabeto.
    Entradas: palabra (str)
    Salidas: str con letras únicas en orden de aparición
    Restricciones: palabra no vacía, sin espacios, solo letras
    """
    if type(palabra) !=str:
        raise Exception("La palabra clave debe ser un string")
    if len(palabra.strip()) ==0:
        raise Exception("La palabra clave no puede estar vacía")
    if " " in palabra:
        raise Exception("La palabra clave no debe contener espacios")

    #minuscula
    palabra =palabra.lower()
    #quita tildes, este metodo es mas eficiente y se ve mas bonito
    palabra =palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    
    #quita repetidas
    letras_unicas =[]
    for c in palabra:
        if c in alfabeto and c not in letras_unicas:
            letras_unicas.append(c)
    if len(letras_unicas) ==0:
        raise Exception("La palabra clave no contiene letras válidas (solo a-z, ñ)")
    return "".join(letras_unicas)

# auxiliares de playfair

def generar_matriz_playfair(palabra_clave):
    """
    Genera la matriz de 6x5 para el cifrado PlayFair.
    Entradas: palabra_clave (str) ya normalizada y sin repetidos
    Salidas: matriz 6x5 (lista de listas)
    """
       
    # Obtener letras que faltan del alfabeto
    letras_restantes =[]
    for letra in alfabeto:
        if letra not in palabra_clave:
            letras_restantes.append(letra)
    

    matriz =[]
    caracteres =list(palabra_clave) +letras_restantes+["1", "2", "3"]
    
    for i in range(6):
        fila =[]
        for j in range(5):
            fila.append(caracteres[i * 5 + j])
        matriz.append(fila)

    return matriz

def encontrar_posicion(matriz, caracter):
    """
    Encuentra la fila y columna de un caracter en la matriz.
    Entradas: matriz 6x5, caracter a buscar
    Salidas: (fila, columna)
    """
    for i in range(6):
        for j in range(5):
            if matriz[i][j] ==caracter:
                return (i, j)
    return None


def procesar_texto_playfair(texto):
    """
    Prepara el texto para el cifrado PlayFair:
    - Elimina espacios
    - Separa letras repetidas con '1'
    - Agrupa en pares
    - Si es impar, agrega '1' al final
    Entradas: texto (str)
    Salidas: lista de pares (cada par es un string de 2 caracteres)
    """
    # Eliminar espacios
    texto_sin_espacios =""
    for c in texto:
        if c !=" ":
            texto_sin_espacios +=c
    
    # Separar letras repetidas con '1'
    texto_procesado =""
    i =0
    while i < len(texto_sin_espacios):
        texto_procesado +=texto_sin_espacios[i]
        if i + 1 < len(texto_sin_espacios) and texto_sin_espacios[i] ==texto_sin_espacios[i+1]:
            texto_procesado +="1"
        i+=1
    
    # Agrupar en pares
    pares =[]
    i =0
    while i < len(texto_procesado):
        if i + 1 < len(texto_procesado):
            pares.append(texto_procesado[i] + texto_procesado[i+1])
        else:
            # Si es impar, agregar '1' al final
            pares.append(texto_procesado[i] + "1")
        i +=2
    
    return pares

def codificar_par_playfair(par, matriz):
    """
    Codifica un par de caracteres segun las reglas de PlayFair.
    Entradas: par (string de 2 caracteres), matriz 6x5
    Salidas: par codificado (string de 2 caracteres)
    """
    a, b =par[0], par[1]
    fila_a, col_a =encontrar_posicion(matriz, a)
    fila_b, col_b =encontrar_posicion(matriz, b)
    
    # Caso1: Diferente fila, diferente columna
    if fila_a !=fila_b and col_a !=col_b:
        return matriz[fila_a][col_b] + matriz[fila_b][col_a]
    
    # Caso2: Misma fila, diferente columna (mover a la derecha)
    elif fila_a ==fila_b and col_a !=col_b:
        nueva_col_a =(col_a + 1) % 5
        nueva_col_b =(col_b + 1) % 5
        return matriz[fila_a][nueva_col_a] + matriz[fila_a][nueva_col_b]
    
    # Caso3: Diferente fila, misma columna (mover hacia abajo)
    elif fila_a !=fila_b and col_a ==col_b:
        nueva_fila_a =(fila_a + 1) % 6
        nueva_fila_b =(fila_b + 1) % 6
        return matriz[nueva_fila_a][col_a] + matriz[nueva_fila_b][col_a]
    
    # Misma fila, misma columna (no deberia pasar)
    else:
        return par

def decodificar_par_playfair(par, matriz):
    """
    Decodifica un par de caracteres segun las reglas de PlayFair (inverso).
    Entradas: par (string de 2 caracteres), matriz 6x5
    Salidas: par decodificado (string de 2 caracteres)
    """
    a, b =par[0], par[1]
    fila_a, col_a =encontrar_posicion(matriz, a)
    fila_b, col_b =encontrar_posicion(matriz, b)
    
    # Caso1: Diferente fila, diferente columna(es igual que en cod)
    if fila_a !=fila_b and col_a !=col_b:
        return matriz[fila_a][col_b] + matriz[fila_b][col_a]
    
    # Caso2: Misma fila, diferente columna (mover a la izquierda)
    elif fila_a ==fila_b and col_a !=col_b:
        nueva_col_a =(col_a - 1) % 5
        nueva_col_b =(col_b - 1) % 5
        return matriz[fila_a][nueva_col_a] + matriz[fila_a][nueva_col_b]
    
    # Caso3:Diferente fila, misma columna (mover hacia arriba)
    elif fila_a !=fila_b and col_a ==col_b:
        nueva_fila_a =(fila_a - 1) % 6
        nueva_fila_b =(fila_b - 1) % 6
        return matriz[nueva_fila_a][col_a] + matriz[nueva_fila_b][col_a]
    
    else:
        return par
