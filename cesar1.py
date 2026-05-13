def cesarCod(texto, desplazamiento):
    """
    Codifica usando cifrado César.
    Entradas: texto (str), desplazamiento (int)
    Salidas: texto codificado (str)
    Restricciones: texto no vacío, desplazamiento entero
    """
    texto_norm = normalizar_texto(texto)
    desp = validar_desplazamiento(desplazamiento)
    
    #asegurarse que este en rango 0.. 26
    desplazamiento_efectivo = desp%len(alfabeto)
    
    resultado = []
    for letra in texto_norm:
        if letra == " ":
            resultado.append(" ")
        else:
            posicion_actual = alfabeto.index(letra)
            nueva_posicion = (posicion_actual + desplazamiento_efectivo) % len(alfabeto)
            resultado.append(alfabeto[nueva_posicion])
    
    return "".join(resultado)


def cesarDec(texto, desplazamiento):
    """
    Decodifica usando cifrado César.
    Entradas: texto codificado (str), desplazamiento (int)
    Salidas: texto original (str)
    Restricciones: texto no vacío, desplazamiento entero
    """
     #decodificar es exactamente igual que codificar
     #pero con desplazamiento negativo
    return cesarCod(texto, -desplazamiento)