import os

# modulo que analiza el disco con recursion
# arma un arbol de nodos con tamanos y saca los reportes


# convierte bytes a la unidad mas adecuada KB MB GB TB
def formato_tamano(bytes):
    """ convierte una cantidad de bytes a la unidad mas adecuada.
    entradas: bytes (int) cantidad de bytes a convertir.
    salidas: string con el valor y la unidad (ej 1.50 MB).
    restricciones: bytes debe ser un numero entero mayor o igual a cero.
    """
    if not isinstance(bytes, int):
        raise TypeError("bytes debe ser un entero")
    if bytes < 0:
        raise ValueError("bytes no puede ser negativo")

    unidades = ["B", "KB", "MB", "GB", "TB"]
    valor = float(bytes)
    i = 0
    # subir de unidad mientras se pueda
    while valor >= 1024 and i < len(unidades) - 1:
        valor = valor / 1024
        i = i + 1
    return "{:.2f} {}".format(valor, unidades[i])


# revisa si una ruta es carpeta sin reventar por permisos
def es_carpeta(ruta):
    """ revisa si una ruta corresponde a una carpeta existente.
    entradas: ruta (string) ruta a verificar.
    salidas: True si es carpeta False si no lo es.
    restricciones: ruta debe ser un string.
    """
    if not isinstance(ruta, str):
        raise TypeError("ruta debe ser un string")

    try:
        return os.path.isdir(ruta)
    except OSError:
        return False


# crea un nodo nuevo con la estructura que usamos en todo el programa
def nuevo_nodo(ruta):
    """ crea un nodo de carpeta con la estructura usada en el programa.
    entradas: ruta (string) ruta de la carpeta.
    salidas: diccionario con nombre ruta tamano es_carpeta hijos y archivos_directos.
    restricciones: ruta debe ser un string.
    """
    if not isinstance(ruta, str):
        raise TypeError("ruta debe ser un string")

    nodo = {}
    nombre = os.path.basename(ruta)
    # si basename viene vacio (raiz tipo C:\ o /) usar la ruta
    if nombre == "":
        nombre = ruta
    nodo["nombre"] = nombre
    nodo["ruta"] = ruta
    nodo["tamano"] = 0
    nodo["es_carpeta"] = True
    nodo["hijos"] = []
    nodo["archivos_directos"] = 0
    return nodo


# analiza una carpeta de forma recursiva y devuelve su nodo
def analizar(ruta):
    """ analiza una carpeta de forma recursiva y arma su arbol de nodos.
    entradas: ruta (string) ruta de la carpeta a analizar.
    salidas: nodo (diccionario) con el tamano total y los hijos analizados.
    restricciones: ruta debe ser un string y debe ser una carpeta valida.
    """
    if not isinstance(ruta, str):
        raise TypeError("ruta debe ser un string")
    if not os.path.isdir(ruta):
        raise ValueError("la ruta no es una carpeta valida")

    nodo = nuevo_nodo(ruta)

    # si no se puede leer la carpeta se devuelve vacia
    try:
        elementos = os.listdir(ruta)
    except OSError:
        return nodo

    for e in elementos:
        completa = os.path.join(ruta, e)
        try:
            if os.path.isdir(completa):
                #carpeta entonces se llama analizar otra vez (recursion)
                hijo = analizar(completa)
                nodo["hijos"].append(hijo)
                nodo["tamano"] = nodo["tamano"] + hijo["tamano"]
            elif os.path.isfile(completa):
                # archivo entonces se suma su tamano
                tam = os.path.getsize(completa)
                hijo = {}
                hijo["nombre"] = e
                hijo["ruta"] = completa
                hijo["tamano"] = tam
                hijo["es_carpeta"] = False
                hijo["hijos"] = []
                hijo["archivos_directos"] = 0
                nodo["hijos"].append(hijo)
                nodo["tamano"] = nodo["tamano"] + tam
                # se cuenta como archivo directo de esta carpeta
                nodo["archivos_directos"] = nodo["archivos_directos"] + 1
        except OSError:
            #si da error se ignora y se sigue
            continue

    return nodo


# recorre el arbol y junta todos los archivos en una lista
def juntar_archivos(nodo, lista):
    """ recorre el arbol y junta todos los archivos en una lista.
    entradas: nodo (diccionario) raiz del recorrido, lista (list) donde se acumulan.
    salidas: ninguna, la lista se modifica con los archivos encontrados.
    restricciones: nodo debe ser un diccionario y lista debe ser una lista.
    """
    if not isinstance(nodo, dict):
        raise TypeError("nodo debe ser un diccionario")
    if not isinstance(lista, list):
        raise TypeError("lista debe ser una lista")

    for hijo in nodo["hijos"]:
        if hijo["es_carpeta"]:
            juntar_archivos(hijo, lista)
        else:
            lista.append(hijo)


# saca los 10 archivos mas grandes de todo el arbol
def archivos_grandes(nodo):
    """ obtiene los 10 archivos mas grandes de todo el arbol.
    entradas: nodo (diccionario) raiz del arbol analizado.
    salidas: lista con hasta 10 nodos de archivo ordenados de mayor a menor.
    restricciones: nodo debe ser un diccionario.
    """
    if not isinstance(nodo, dict):
        raise TypeError("nodo debe ser un diccionario")

    lista = []
    juntar_archivos(nodo, lista)
    # ordenar de mayor a menor por tamano
    lista.sort(key=lambda a: a["tamano"], reverse=True)
    return lista[:10]


#recorre el arbol y junta todas las carpetas
def juntar_carpetas(nodo, lista):
    """ recorre el arbol y junta todas las carpetas en una lista.
    entradas: nodo (diccionario) raiz del recorrido, lista (list) donde se acumulan.
    salidas: ninguna, la lista se modifica con las carpetas encontradas.
    restricciones: nodo debe ser un diccionario y lista debe ser una lista.
    """
    if not isinstance(nodo, dict):
        raise TypeError("nodo debe ser un diccionario")
    if not isinstance(lista, list):
        raise TypeError("lista debe ser una lista")

    for hijo in nodo["hijos"]:
        if hijo["es_carpeta"]:
            lista.append(hijo)
            juntar_carpetas(hijo, lista)


# saca los 10 directorios con mas archivos directos
def directorios_llenos(nodo):
    """ obtiene los 10 directorios con mas archivos directos.
    entradas: nodo (diccionario) raiz del arbol analizado.
    salidas: lista con hasta 10 nodos de carpeta ordenados por archivos directos.
    restricciones: nodo debe ser un diccionario.
    """
    if not isinstance(nodo, dict):
        raise TypeError("nodo debe ser un diccionario")

    lista = []
    # la raiz tambien cuenta
    lista.append(nodo)
    juntar_carpetas(nodo, lista)
    # ordenar por cantidad de archivos directos
    lista.sort(key=lambda c: c["archivos_directos"], reverse=True)
    return lista[:10]


# main para probar el modulo solo sin la parte grafica
def main():
    """ prueba el modulo solo sin la parte grafica mostrando los reportes en consola.
    entradas: ninguna, pide la carpeta por consola.
    salidas: ninguna, imprime los resultados en pantalla.
    restricciones: la carpeta ingresada debe existir y ser valida.
    """
    ruta = input("ingrese la carpeta a analizar: ")
    if not es_carpeta(ruta):
        print("la ruta no es una carpeta valida")
        return

    raiz = analizar(ruta)
    print("carpeta:", raiz["nombre"], "->", formato_tamano(raiz["tamano"]))

    print("\n10 archivos mas grandes")
    for a in archivos_grandes(raiz):
        print(a["ruta"], "->", formato_tamano(a["tamano"]))

    print("\n10 directorios con mas archivos")
    for d in directorios_llenos(raiz):
        print(d["ruta"], "->", d["archivos_directos"])


if __name__ == "__main__":
    main()
