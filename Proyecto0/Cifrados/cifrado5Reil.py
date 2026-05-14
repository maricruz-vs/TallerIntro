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


# RAIL FENCE
def railfenceCod(texto):
    """
    Codifica usando cifrado Rail Fence.
    Entradas: texto (str)
    Salidas: texto codificado (str)
    Restricciones: texto no vacio
    """
    texto_norm =normalizar_texto(texto)
    
    texto_guiones =""
    for c in texto_norm:
        if c ==" ":
            texto_guiones +="-"
        else:
            texto_guiones +=c
    
    largo =len(texto_guiones)
    while largo % 4 !=0:
        texto_guiones +="-"
        largo +=1
    
    linea1 =""
    linea2 =""
    linea3 =""
    
    for i in range(largo):
        resto =i % 4
        if resto ==0:
            linea1 +=texto_guiones[i]
        elif resto ==1 or resto ==3:
            linea2 +=texto_guiones[i]
        else:
            linea3 +=texto_guiones[i]
    
    union =linea1 +linea2 +linea3
    
    resultado =""
    for i in range(0, len(union), 5):
        resultado +=union[i:i+5] +" "
    
    return resultado.strip()


def railfenceDec(texto):
    """
    Decodifica usando cifrado Rail Fence.
    Entradas: texto codificado (str)
    Salidas: texto original (str)
    Restricciones: texto no vacio
    """
    union =""
    for c in texto:
        if c !=" ":
            union +=c
    
    if len(union) % 4 !=0:
        raise Exception("El texto codificado no tiene longitud multiple de 4")
    
    largo_total =len(union)
    largo_fila =largo_total // 4
    
    linea1 =union[:largo_fila]
    linea2 =union[largo_fila:largo_fila + largo_fila * 2]
    linea3 =union[largo_fila + largo_fila * 2:]
    
    resultado =""
    i1=0
    i2=0
    i3=0
    
    for i in range(largo_total):
        resto =i % 4
        if resto ==0:
            resultado +=linea1[i1]
            i1 +=1
        elif resto ==1:
            resultado +=linea2[i2]
            i2 +=1
        elif resto ==2:
            resultado +=linea3[i3]
            i3 +=1
        else:
            resultado +=linea2[i2]
            i2 +=1
    
    resultado_final =""
    for c in resultado:
        if c =="-":
            resultado_final +=" "
        else:
            resultado_final +=c
    
    while resultado_final.endswith(" "):
        resultado_final =resultado_final[:-1]
    
    return resultado_final
