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


# VIGENERE
def vigenereCod(texto, palabra_clave):
    """
    Codifica un texto usando cifrado Vigenere.
    Entradas: texto y palabra_clave (str)
    Salidas: texto codificado (str)
    Restricciones: palabra_clave no vacia, texto normalizable
    """
    texto_norm =normalizar_texto(texto)
    clave_norm =normalizar_palabra_clave(palabra_clave)
    
    clave_posiciones =[]
    for letra in clave_norm:
        clave_posiciones.append(alfabeto.index(letra))
    
    resultado =[]
    idx_clave =0
    longitud_clave =len(clave_posiciones)
    
    for letra in texto_norm:
        if letra ==" ":
            resultado.append(" ")
        else:
            pos_texto =alfabeto.index(letra)
            pos_clave =clave_posiciones[idx_clave % longitud_clave]
            nueva_pos =(pos_texto +pos_clave) % len(alfabeto)
            resultado.append(alfabeto[nueva_pos])
            idx_clave +=1
    
    return "".join(resultado)

def vigenereDec(texto, palabra_clave):
    """
    Decodifica un texto cifrado con Vigenere.
    Entradas: texto codificado y palabra_clave (str)
    Salidas: texto original (str)
    Restricciones: palabra_clave no vacía, texto normalizable
    """
    texto_norm =normalizar_texto(texto)
    clave_norm =normalizar_palabra_clave(palabra_clave)
    
    clave_posiciones =[]
    for letra in clave_norm:
        clave_posiciones.append(alfabeto.index(letra))
    
    resultado =[]
    idx_clave =0
    longitud_clave =len(clave_posiciones)
    
    for letra in texto_norm:
        if letra ==" ":
            resultado.append(" ")
        else:
            #lo mismo pero restando
            #checkear si esto funciona pls
            pos_cifrada =alfabeto.index(letra)
            pos_clave =clave_posiciones[idx_clave % longitud_clave]
            nueva_pos =(pos_cifrada - pos_clave) % len(alfabeto)
            resultado.append(alfabeto[nueva_pos])
            idx_clave +=1
    
    return "".join(resultado)
