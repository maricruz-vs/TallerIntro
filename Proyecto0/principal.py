alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Funciones auxiliares

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
    #quita tildes, este metodo es mas eficiente y se ve mas bonito
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


# Funciones decodificadoras

# CESAR
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
    # decodificar es exactamente igual que codificar
    # pero con desplazamiento negativo
    return cesarCod(texto, -desplazamiento)

# MONOALFABETICO
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

# VIGENERE
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

# PLAYFAIR
def playfairCod(texto, palabra):
    """
    Codifica usando cifrado PlayFair.
    Entradas: texto (str), palabra clave (str)
    Salidas: texto codificado (str)
    Restricciones: palabra clave no vacia
    """
    texto_norm = normalizar_texto(texto)
    palabra_norm = normalizar_palabra_clave(palabra)
    return "por implementar"

def playfairDec(texto, palabra):
    """
    Decodifica usando cifrado PlayFair.
    Entradas: texto codificado (str), palabra clave (str)
    Salidas: texto original (str)
    Restricciones: palabra clave no vacia
    """
    palabra_norm = normalizar_palabra_clave(palabra)
    return "por implementar"


# RAIL FENCE
def railfenceCod(texto):
    """
    Codifica usando cifrado Rail Fence.
    Entradas: texto (str)
    Salidas: texto codificado (str)
    Restricciones: texto no vacio
    """
    texto_norm = normalizar_texto(texto)
    return "por implementar"

def railfenceDec(texto):
    """
    Decodifica usando cifrado Rail Fence.
    Entradas: texto codificado (str)
    Salidas: texto original (str)
    Restricciones: texto no vacio
    """
    return "por implementar"

# ESCITALA
def escitalaCod(texto, lineas):
    """
    Codifica usando cifrado Escitala.
    Entradas: texto (str), lineas (int)
    Salidas: texto codificado (str)
    Restricciones: lineas > 1 entero
    """
    if type(lineas) != int or lineas <= 1:
        raise Exception("El numero de lineas debe ser un entero mayor que 1")
    texto_norm = normalizar_texto(texto)
    return "por implementar"

def escitalaDec(texto, lineas):
    """
    Decodifica usando cifrado Escitala.
    Entradas: texto codificado (str), lineas (int)
    Salidas: texto original (str)
    Restricciones: lineas > 1 entero
    """
    if type(lineas) != int or lineas <= 1:
        raise Exception("El numero de lineas debe ser un entero mayor que 1")
    return "por implementar"

# FUNCION GENERICA PARA CODIFICAR y DECODIFICAR 
def ejecutar_cifrado(nombre, func_cod, func_dec, necesita_palabra=False, necesita_desplazamiento=False, necesita_lineas=False):
    """
    Funcion generica para ejecutar cualquier cifrado
    """
    print(f"\n--- {nombre} ---")
    while True:
        try:
            print("1. Codificar")
            print("2. Decodificar")
            opcion = input("Seleccione: ")
            if opcion not in ("1", "2"):
                raise Exception("Opcion invalida")
            
            texto = input("Ingrese el mensaje: ")
            if not texto:
                raise Exception("El mensaje no puede estar vacio")
            
            #cesar
            if necesita_desplazamiento:
                desplazamiento = int(input("Ingrese el desplazamiento (entero): "))
            #mono, vigenere, playfair
            if necesita_palabra:
                palabra = input("Ingrese la palabra clave (sin espacios): ")
            
            if necesita_lineas:
                lineas = int(input("Ingrese el numero de lineas (mayor que 1): "))
                if lineas <= 1:
                    raise Exception("El numero de lineas debe ser mayor que 1")
            
            #codficaciones
            if opcion == "1":
                #mono, vigenere, playfair, 
                if necesita_palabra:
                    resultado = func_cod(texto, palabra)
                #cesar
                elif necesita_desplazamiento:
                    resultado = func_cod(texto, desplazamiento)
                #esci
                elif necesita_lineas:
                    resultado = func_cod(texto, lineas)
                #rail
                else:
                    resultado = func_cod(texto)
                print(f"\nTexto CODIFICADO: {resultado}")
            else:
                if necesita_palabra:
                    resultado = func_dec(texto, palabra)
                elif necesita_desplazamiento:
                    resultado = func_dec(texto, desplazamiento)
                elif necesita_lineas:
                    resultado = func_dec(texto, lineas)
                else:
                    resultado = func_dec(texto)
                print(f"\nTexto DECODIFICADO: {resultado}")
            break
            
        except ValueError:
            print("\nError: Debe ingresar un numero entero")
        except Exception as e:
            print(f"\nError: {e}")
        print("Intente nuevamente.\n")

# MENU
def mostrar_menu():
    print("\n" + "=" * 50)
    print("0. Salir")
    print("1. Cifrado Cesar")
    print("2. Cifrado Monoalfabetico")
    print("3. Cifrado Vigenere")
    print("4. Cifrado PlayFair")
    print("5. Cifrado Rail Fence")
    print("6. Cifrado Escitala")
    print("-" * 50)


# MAIN
def main():
    print("=" * 50)
    print("    TALLER DE PROGRAMACION - PROYECTO 0")
    print("   Jose Daniel Jimenez y Maricruz Vasquez")
    print("=" * 50)
    print("\nBienvenidx al programa de cifrado y descifrado!")
    print("Este programa le permite codificar y decodificar mensajes")
    print("utilizando diferentes metodos criptograficos.\n")

    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "0":
            print("\nGracias por usar el programa! Hasta luego.\n")
            return
        elif opcion == "1":
            ejecutar_cifrado("CIFRADO CESAR", cesarCod, cesarDec, necesita_desplazamiento=True)
        elif opcion == "2":
            ejecutar_cifrado("CIFRADO MONOALFABETICO", monoCod, monoDec, necesita_palabra=True)
        elif opcion == "3":
            ejecutar_cifrado("CIFRADO VIGENERE", vigenereCod, vigenereDec, necesita_palabra=True)
        elif opcion == "4":
            ejecutar_cifrado("CIFRADO PLAYFAIR", playfairCod, playfairDec, necesita_palabra=True)
        elif opcion == "5":
            ejecutar_cifrado("CIFRADO RAIL FENCE", railfenceCod, railfenceDec)
        elif opcion == "6":
            ejecutar_cifrado("CIFRADO ESCITALA", escitalaCod, escitalaDec, necesita_lineas=True)
        else:
            print("\nOpcion no valida. Elija una opcion del 0 al 6.\n")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()