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


# ESCITALA
def escitalaCod(texto, lineas):
    """
    Codifica usando cifrado Escitala.
    Entradas: texto (str), lineas (int) - cantidad de letras por vuelta
    Salidas: texto codificado (str)
    Restricciones: lineas > 1 entero, texto no vacio
    """
    if type(lineas) !=int or lineas <=1:
        raise Exception("El numero de lineas debe ser un entero mayor que 1")
    
    texto_norm =normalizar_texto(texto)
    
    texto_guiones =""
    for c in texto_norm:
        if c ==" ":
            texto_guiones +="-"
        else:
            texto_guiones +=c
    
    largo =len(texto_guiones)
    while largo % lineas !=0:
        texto_guiones +="-"
        largo +=1
    
    lineas_texto =[]
    for i in range(lineas):
        lineas_texto.append("")
    
    for i in range(largo):
        pos_fila =i % lineas
        lineas_texto[pos_fila] +=texto_guiones[i]
    
    union =""
    for fila in lineas_texto:
        union +=fila
    
    resultado =""
    for i in range(0, len(union), 5):
        resultado +=union[i:i+5] + " "
    
    return resultado.strip()


def escitalaDec(texto, lineas):
    """
    Decodifica usando cifrado Escitala.
    Entradas: texto codificado (str), lineas (int)
    Salidas: texto original (str)
    Restricciones: lineas >1 entero
    """
    if type(lineas)!=int or lineas<=1:
        raise Exception("El numero de lineas debe ser un entero mayor que 1")
    
    union =""
    for c in texto:
        if c !=" ":
            union+=c
    
    largo_total =len(union)
    
    if largo_total % lineas !=0:
        raise Exception("El texto codificado no tiene longitud multiple de lineas")
    
    largo_fila =largo_total//lineas
    
    lineas_texto =[]
    inicio =0
    for i in range(lineas):
        lineas_texto.append(union[inicio:inicio + largo_fila])
        inicio +=largo_fila
    
    resultado =""
    for i in range(largo_total):
        pos_fila =i % lineas
        resultado +=lineas_texto[pos_fila][i//lineas]
    
    resultado_final =""
    for c in resultado:
        if c =="-":
            resultado_final +=" "
        else:
            resultado_final +=c
    
    while resultado_final.endswith(" "):
        resultado_final =resultado_final[:-1]
    
    return resultado_final
