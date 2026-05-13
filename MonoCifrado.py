alfabetoCompleto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ "
alfabeto= "abcdefghijklmnñopqrstuvwxyz"
def monoCod(Palabra_Clave, texto):
    """
    Algoritmo que codifica un texto utilizando una palabra clave para cambiar el alfabeto
    Entradas y restricciones:
    Palabra calve: Debe ser un string que use unicamente letras del alfabeto.
    texto: debe ser un string que use unicamente letras del alfabeto.
    Salidas:
    Texto Codificado en mono cifrado según la palabra clave indicada.
    """
    try:
        textorev=list(texto)
        for letra in textorev:
            if letra not in alfabetoCompleto:
                raise Exception (f"El texto no puede contener {letra}")
                break
    except Exception as e:
        print(f"Error: {e}")
    try:
        PalabraRev=list(Palabra_Clave)
        for letra in PalabraRev:
            if letra not in alfabetoCompleto:
                raise Exception (f"La palabra clave no puede contener {letra}")
                break
    except Exception as e:
        print(f"Error: {e}")
        return
    revisionTexto(texto)
    revisionPalabraC(Palabra_Clave)
    listaAlfabeto=list(alfabeto)
    ListaTexto=list(revisionTexto(texto))
    PalabraInvertida=revisionPalabraC(Palabra_Clave)[::-1]
    TextoCodificado=""
    for letra in PalabraInvertida:
        if letra in alfabeto:
            listaAlfabeto.remove(letra)
            listaAlfabeto.insert(0, letra)
    for letra in revisionTexto(texto):
        if letra != " ":
            if letra == "a":
                letraF=listaAlfabeto[0]
            if letra == "b":
                letraF=listaAlfabeto[1]            
            if letra == "c":
                letraF=listaAlfabeto[2]
            if letra == "d":
                letraF=listaAlfabeto[3]
            if letra == "e":
                letraF=listaAlfabeto[4]    
            if letra == "f":
                letraF=listaAlfabeto[5]
            if letra == "g":
                letraF=listaAlfabeto[6]
            if letra == "h":
                letraF=listaAlfabeto[7]
            if letra == "i":
                letraF=listaAlfabeto[8]
            if letra == "j":
                letraF=listaAlfabeto[9]
            if letra == "k":
                letraF=listaAlfabeto[10]
            if letra == "l":
                letraF=listaAlfabeto[11]
            if letra == "m":
                letraF=listaAlfabeto[12]
            if letra == "n":
                letraF=listaAlfabeto[13]
            if letra == "ñ":
                letraF=listaAlfabeto[14]
            if letra == "o":
                letraF=listaAlfabeto[15]
            if letra == "p":
                letraF=listaAlfabeto[16]
            if letra == "q":
                letraF=listaAlfabeto[17]
            if letra == "r":
                letraF=listaAlfabeto[18]
            if letra == "s":
                letraF=listaAlfabeto[19]                
            if letra == "t":
                letraF=listaAlfabeto[20]
            if letra == "u":
                letraF=listaAlfabeto[21]
            if letra == "v":
                letraF=listaAlfabeto[22]
            if letra == "w":
                letraF=listaAlfabeto[23]
            if letra == "x":
                letraF=listaAlfabeto[24]
            if letra == "y":
                letraF=listaAlfabeto[25]
            if letra == "z":
                letraF=listaAlfabeto[26]
            TextoCodificado+=letraF
        else:
            TextoCodificado+=letra
    print(f"{TextoCodificado}")          
def revisionTexto(texto):
    """
    Funcion que revisa el texto para que sea adecuado para la codificacion.
    Entradas: ninguna
    Salidas: Texto nuevo, listo para la codificación
    """
    try:
        if type (texto) != str:
            raise Exception ("El texto debe ser un string")
    except Exception as e:
        print(f"Error: {e}")
        return
    texto=texto.lower()
    textoNuevo=""
    letras=list(texto)
    for letra in letras:
        letra
        if letra in alfabetoCompleto:
            if letra=="á":
                letra="a"
            if letra=="é":
                letra="e"
            if letra=="í":
                letra="i"
            if letra=="ó":
                letra="o"
            if letra=="ú":
                letra="u"
            textoNuevo=textoNuevo+letra
    return textoNuevo
def revisionPalabraC(Palabra_Clave):
    """
    Funcion que revisa la palabra clave para que sea adecuada para la codificacion.
    Entradas: ninguna
    Salidas: palabra nueva, listo para la codificación
    """
    try:
        if type (Palabra_Clave) != str:
            raise Exception ("La palabra clave debe ser un string")
        if len(Palabra_Clave.split())>1:
            raise Exception ("Digite solo una palabra")
    except Exception as e:
        print(f"Error: {e}")
        return
    Palabra_Clave=Palabra_Clave.lower()
    PalabraNuevo=""
    letras=list(Palabra_Clave)
    for letra in letras:
        letra
        if letra in alfabetoCompleto:
            if letra=="á":
                letra="a"
            if letra=="é":
                letra="e"
            if letra=="í":
                letra="i"
            if letra=="ó":
                letra="o"
            if letra=="ú":
                letra="u"
            PalabraNuevo=PalabraNuevo+letra
    return PalabraNuevo

def monoDec(Palabra_Clave, texto):
    """
    Algoritmo que decodifica un texto codificado en Cifrado Monoalfabético
    Entradas y restricciones:
    Palabra calve: Debe ser un string que use unicamente letras del alfabeto.
    texto: debe ser un string que use unicamente letras del alfabeto.
    Salidas:
    Texto Codificado en mono cifrado según la palabra clave indicada.
    """
    try:
        textorev=list(texto)
        for letra in textorev:
            if letra not in alfabetoCompleto:
                raise Exception (f"El texto no puede contener {letra}")
                break
    except Exception as e:
        print(f"Error: {e}")
    try:
        PalabraRev=list(Palabra_Clave)
        for letra in PalabraRev:
            if letra not in alfabetoCompleto:
                raise Exception (f"La palabra clave no puede contener {letra}")
                break
    except Exception as e:
        print(f"Error: {e}")
        return
    revisionTexto(texto)
    revisionPalabraC(Palabra_Clave)
    listaAlfabeto=list(alfabeto)
    ListaTexto=list(revisionTexto(texto))
    PalabraInvertida=revisionPalabraC(Palabra_Clave)[::-1]
    TextoDecodificado=""
    for letra in PalabraInvertida:
        if letra in alfabeto:
            listaAlfabeto.remove(letra)
            listaAlfabeto.insert(0, letra)
    for letra in revisionTexto(texto):
        if letra != " ":
            if letra == listaAlfabeto[0]:
                letraF="a"
            if letra == listaAlfabeto[1]:
                letraF="b"           
            if letra == listaAlfabeto[2]:
                letraF="c"
            if letra == listaAlfabeto[3]:
                letraF="d"
            if letra == listaAlfabeto[4]:
                letraF="e"    
            if letra == listaAlfabeto[5]:
                letraF="f"
            if letra == listaAlfabeto[6]:
                letraF="g"
            if letra == listaAlfabeto[7]:
                letraF="h"
            if letra == listaAlfabeto[8]:
                letraF="i"
            if letra == listaAlfabeto[9]:
                letraF="j"
            if letra == listaAlfabeto[10]:
                letraF="k"
            if letra == listaAlfabeto[11]:
                letraF="l"
            if letra == listaAlfabeto[12]:
                letraF="m"
            if letra == listaAlfabeto[13]:
                letraF="n"
            if letra == listaAlfabeto[14]:
                letraF="ñ"
            if letra == listaAlfabeto[15]:
                letraF="o"
            if letra == listaAlfabeto[16]:
                letraF="p"
            if letra == listaAlfabeto[17]:
                letraF="q"
            if letra == listaAlfabeto[18]:
                letraF="r"
            if letra == listaAlfabeto[19]:
                letraF="s"              
            if letra == listaAlfabeto[20]:
                letraF="t"
            if letra == listaAlfabeto[21]:
                letraF="u"
            if letra == listaAlfabeto[22]:
                letraF="v"
            if letra == listaAlfabeto[23]:
                letraF="w"
            if letra == listaAlfabeto[24]:
                letraF="x"
            if letra == listaAlfabeto[25]:
                letraF="y"
            if letra == listaAlfabeto[26]:
                letraF="z"
            TextoDecodificado+=letraF
        else:
            TextoDecodificado+=letra
    print(f"{TextoDecodificado}")
