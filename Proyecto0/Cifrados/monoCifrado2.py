alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_completo = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ "


############################################################

# Funciones auxiliares

############################################################

#esto antes era revisionTexto
def normalizar_texto(texto):
    """
    Normaliza el texto: minúsculas, reemplaza acentos, elimina caracteres no alfabéticos (excepto espacios).
    Entradas: texto (str)
    Salidas: str normalizado
    Restricciones: texto debe ser string no vacío
    """
    if type(texto) != str:
        raise Exception("El texto debe ser un string")
    if len(texto.strip()) == 0:
        raise Exception("El texto no puede estar vacío")
    
    #aqui las hace minusculas
    texto = texto.lower()
    resultado = []
    for c in texto:
        #quita tildes
        if c in "á":
            c = "a"
        elif c in "é":
            c = "e"
        elif c in "í":
            c = "i"
        elif c in "ó":
            c = "o"
        elif c in "ú":
            c = "u"
        # conserva letras del alfabeto (incluyendo ñ) y espacios
        if c in alfabeto or c == " ":
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
    if type(palabra) != str:
        raise Exception("La palabra clave debe ser un string")
    if len(palabra.strip()) == 0:
        raise Exception("La palabra clave no puede estar vacía")
    if " " in palabra:
        raise Exception("La palabra clave no debe contener espacios")

    #minuscula
    palabra = palabra.lower()
    #quita tildes
    palabra = palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    
    #quita repetidas
    letras_unicas = []
    for c in palabra:
        if c in ALFABETO and c not in letras_unicas:
            letras_unicas.append(c)
    if len(letras_unicas) == 0:
        raise Exception("La palabra clave no contiene letras válidas (solo a-z, ñ)")
    return "".join(letras_unicas)

def validar_desplazamiento(desplazamiento):
    """
    Valida que el desplazamiento sea entero.
    Entradas: desplazamiento (cualquier tipo)
    Salidas: int (el mismo desplazamiento)
    Restricciones: debe ser entero
    """
    if type(desplazamiento) != int:
        raise Exception("El desplazamiento debe ser un número entero")
    return desplazamiento


############################################################

# funciones decodificadoras

############################################################



def monoCod(texto, palabra):
    """
    Algoritmo que codifica un texto utilizando una palabra clave para cambiar el alfabeto
    Entradas y restricciones:
    Palabra calve: Debe ser un string que use unicamente letras del alfabeto.
    texto: debe ser un string que use unicamente letras del alfabeto.
    Salidas:
    Texto Codificado en mono cifrado según la palabra clave indicada.
    """
    texto_norm = normalizar_texto(texto)
    clave_norm = normalizar_palabra_clave(palabra)
    
    #palabra clave + resto del alfabeto en orden
    resto = [c for c in alfabeto if c not in clave_norm]
    alfabeto_cifrado = list(clave_norm) + resto
    
    # mapeo original a cifrada
    mapeo = {}
    #enumerate crea una asignacion indice-letra
    #entonces se ve como (0,a) ... (27, z)
    # luego i seria 0 y letra_orig seria a
    for i, letra_orig in enumerate(alfabeto):
        mapeo[letra_orig] = alfabeto_cifrado[i]
    
    
    # cambio en el texto
    resultado = []
    for c in texto_norm:
        if c == " ":
            resultado.append(" ")
        else:
            resultado.append(mapeo[c])
    return "".join(resultado)

def monoDec(texto, palabra):
     """
    Algoritmo que decodifica un texto codificado en Cifrado Monoalfabético
    Entradas y restricciones:
    Palabra calve: Debe ser un string que use unicamente letras del alfabeto.
    texto: debe ser un string que use unicamente letras del alfabeto.
    Salidas:
    Texto Codificado en mono cifrado según la palabra clave indicada.
    """
    texto_norm = normalizar_texto(texto) 
    clave_norm = normalizar_palabra_clave(palabra)
    
    # alfabeto para cifrar
    resto = [c for c in alfabeto if c not in clave_norm]
    alfabeto_cifrado = list(clave_norm) + resto
    
    # mapeo inverso de cod a og
    mapeo_inverso = {}
    for i, letra_cifrada in enumerate(alfabeto_cifrado):
        mapeo_inverso[letra_cifrada] = alfabeto[i]
    
    # cambia el texto 
    resultado = []
    for c in texto_norm:
        if c == " ":
            resultado.append(" ")
        else:
            if c not in mapeo_inverso:
                raise Exception(f"El carácter '{c}' no pertenece al alfabeto cifrado")
            resultado.append(mapeo_inverso[c])
    return "".join(resultado)