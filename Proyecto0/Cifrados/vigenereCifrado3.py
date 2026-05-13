def vigenereCod(texto, palabra_clave):
    """
    Codifica un texto usando cifrado Vigenere.
    Entradas: texto y palabra_clave (str)
    Salidas: texto codificado (str)
    Restricciones: palabra_clave no vacia, texto normalizable
    """
    texto_norm = normalizar_texto(texto)
    clave_norm = normalizar_palabra_clave(palabra_clave)
    
    clave_posiciones = []
    for letra in clave_norm:
        clave_posiciones.append(alfabeto.index(letra))
    
    resultado = []
    idx_clave = 0
    longitud_clave = len(clave_posiciones)
    
    for letra in texto_norm:
        if letra == " ":
            resultado.append(" ")
        else:
            pos_texto = alfabeto.index(letra)
            pos_clave = clave_posiciones[idx_clave % longitud_clave]
            nueva_pos = (pos_texto + pos_clave) % len(alfabeto)
            resultado.append(alfabeto[nueva_pos])
            idx_clave += 1
    
    return "".join(resultado)


def vigenereDec(texto, palabra_clave):
    """
    Decodifica un texto cifrado con Vigenere.
    Entradas: texto codificado y palabra_clave (str)
    Salidas: texto original (str)
    Restricciones: palabra_clave no vacía, texto normalizable
    """
    texto_norm = normalizar_texto(texto)
    clave_norm = normalizar_palabra_clave(palabra_clave)
    
    clave_posiciones = []
    for letra in clave_norm:
        clave_posiciones.append(alfabeto.index(letra))
    
    resultado = []
    idx_clave = 0
    longitud_clave = len(clave_posiciones)
    
    for letra in texto_norm:
        if letra == " ":
            resultado.append(" ")
        else:
            #lo mismo pero restando
            #checkear si esto funciona pls
            pos_cifrada = alfabeto.index(letra)
            pos_clave = clave_posiciones[idx_clave % longitud_clave]
            nueva_pos = (pos_cifrada - pos_clave) % len(alfabeto)
            resultado.append(alfabeto[nueva_pos])
            idx_clave += 1
    
    return "".join(resultado)