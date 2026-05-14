def railfenceCod(texto):
    """
    Codifica usando cifrado Rail Fence.
    Entradas: texto (str)
    Salidas: texto codificado (str)
    Restricciones: texto no vacio
    """
    texto_norm = normalizar_texto(texto)
    
    texto_guiones = ""
    for c in texto_norm:
        if c == " ":
            texto_guiones += "-"
        else:
            texto_guiones += c
    
    largo = len(texto_guiones)
    while largo % 4 != 0:
        texto_guiones += "-"
        largo += 1
    
    linea1 = ""
    linea2 = ""
    linea3 = ""
    
    for i in range(largo):
        resto = i % 4
        if resto == 0:
            linea1 += texto_guiones[i]
        elif resto == 1 or resto == 3:
            linea2 += texto_guiones[i]
        else:
            linea3 += texto_guiones[i]
    
    union = linea1 + linea2 + linea3
    
    resultado = ""
    for i in range(0, len(union), 5):
        resultado += union[i:i+5] + " "
    
    return resultado.strip()


def railfenceDec(texto):
    """
    Decodifica usando cifrado Rail Fence.
    Entradas: texto codificado (str)
    Salidas: texto original (str)
    Restricciones: texto no vacio
    """
    union = ""
    for c in texto:
        if c != " ":
            union += c
    
    if len(union) % 4 != 0:
        raise Exception("El texto codificado no tiene longitud multiple de 4")
    
    largo_total = len(union)
    largo_fila = largo_total // 4
    
    linea1 = union[:largo_fila]
    linea2 = union[largo_fila:largo_fila + largo_fila * 2]
    linea3 = union[largo_fila + largo_fila * 2:]
    
    resultado = ""
    i1 = 0
    i2 = 0
    i3 = 0
    
    for i in range(largo_total):
        resto = i % 4
        if resto == 0:
            resultado += linea1[i1]
            i1 += 1
        elif resto == 1:
            resultado += linea2[i2]
            i2 += 1
        elif resto == 2:
            resultado += linea3[i3]
            i3 += 1
        else:
            resultado += linea2[i2]
            i2 += 1
    
    resultado_final = ""
    for c in resultado:
        if c == "-":
            resultado_final += " "
        else:
            resultado_final += c
    
    while resultado_final.endswith(" "):
        resultado_final = resultado_final[:-1]
    
    return resultado_final