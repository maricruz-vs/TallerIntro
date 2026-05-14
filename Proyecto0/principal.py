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


def mostrar_menu():
    print("\n" + "=" * 50)
    print("    TALLER DE PROGRAMACION - PROYECTO 0")
    print("   Jose Daniel Jimenez y Maricruz Vasquez")
    print("=" * 50)
    print("0. Salir")
    print("1. Cifrado Cesar")
    print("2. Cifrado Monoalfabetico")
    print("3. Cifrado Vigenere")
    print("4. Cifrado PlayFair")
    print("5. Cifrado Rail Fence")
    print("6. Cifrado Escitala")
    print("-" * 50)


# ==================== MAIN ====================

def main():
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