import os

# modulo que analiza el disco con recursion
# aqui va toda la parte de leer carpetas y sacar tamanos

# convierte bytes a la unidad que se vea mejor
def formato_tamano(bytes):
    # falta decidir si usamos 1024 o 1000 (preguntar)
    if bytes < 1024:
        return str(bytes) + " B"
    # hacer el resto de unidades KB MB GB TB
    return "pendiente"






# revisa si una ruta es carpeta
def es_carpeta(ruta):
    # usar os.path.isdir
    return os.path.isdir(ruta)


# analiza una carpeta y devuelve un nodo con su info
def analizar(ruta, nivel):
    # aqui iria la recursion SI TUVIERA UNA

    #un nodo seria algo como nombre tamano hijos
    nodo = {}
    nodo["nombre"] = os.path.basename(ruta)
    nodo["ruta"] = ruta
    nodo["tamano"] = 0
    nodo["hijos"] = []

    #lista de lo que hay adentro
    elementos = os.listdir(ruta)

    for e in elementos:
        completa = os.path.join(ruta, e)
        #si es archivo sumar su tamano
        #si es carpeta llamar analizar otra vez ( la recursion)
        pass

    # falta sumar tamanos de los hijos al nodo
    return nodo


# saca los 10 archivos mas grandes
def archivos_grandes(nodo):
    # recorrer todo el arbol y juntar archivos
    # ordenar por tamano y tomar 10
    return []


# saca los 10 directorios con mas archivos directos
def directorios_llenos(nodo):
    # contar archivos directos de cada carpeta
    # ordenar y tomar 10
    return []


#para probar el modulo solo
def main():
    ruta = input("ingrese la carpeta: ")
    # llamar analizar y mostrar algo basico para ver que sirve
    raiz = analizar(ruta, 0)
    print(raiz)


main()
