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

# auxiliar de cesar
def validar_desplazamiento(desplazamiento):
    """
    Valida que el desplazamiento sea entero.
    Entradas: desplazamiento (cualquier tipo)
    Salidas: int (el mismo desplazamiento)
    Restricciones: debe ser entero
    """
    if type(desplazamiento) !=int:
        raise Exception("El desplazamiento debe ser un número entero")
    return desplazamiento


# CESAR
def cesarCod(texto, desplazamiento):
    """
    Codifica usando cifrado César.
    Entradas: texto (str), desplazamiento (int)
    Salidas: texto codificado (str)
    Restricciones: texto no vacío, desplazamiento entero
    """
    texto_norm =normalizar_texto(texto)
    desp =validar_desplazamiento(desplazamiento)
    
    #asegurarse que este en rango 0.. 26
    desplazamiento_efectivo =desp%len(alfabeto)
    
    resultado =[]
    for letra in texto_norm:
        if letra ==" ":
            resultado.append(" ")
        else:
            posicion_actual =alfabeto.index(letra)
            nueva_posicion =(posicion_actual + desplazamiento_efectivo) % len(alfabeto)
            resultado.append(alfabeto[nueva_posicion])
    
    return "".join(resultado)

def cesarDec(texto, desplazamiento):
    """
    Decodifica usando cifrado César.
    Entradas: texto codificado (str), desplazamiento (int)
    Salidas: texto original (str)
    Restricciones: texto no vacío, desplazamiento entero
    """
    # decodificar es exactamente igual que codificar pero con desplazamiento negativo
    return cesarCod(texto, -desplazamiento)
