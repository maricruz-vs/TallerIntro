from itertools import cycle
alfabetoCompleto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ "
alfabeto= "abcdefghijklmnñopqrstuvwxyz"

def Main():
    while True:
        try:
            print("Bienvenido, en que desea codificar?")
            print("Salida= 0")
            print("Cifrado cesar, (texto, desplazamiento)= 1")
            print("Ciifrado monoalfabético, (texto, Palabra clave)= 2")
            print("Cifrado vigenere, (texto, Palabra clave)= 3")
            print("Cifrado PlayFair, (texto, Palabra clave)= 4")
            print("Cifrado RailFence, (texto)= 5")
            print("Cifrado Escitala, (texto, lineas)= 6")
            try:
                Entrada=int(input("Digite su respuesta: "))
            except ValueError:
                print("La entrada debe ser un numero entero del 1 al 6")
            try:
                if type(Entrada)!= int or Entrada<1 or Entrada>6:
                    raise Exception("La entrada debe ser un numero entero del 1 al 6")
            except Exception as e:
                print()
                print(f"Error: {e}")
                print()
            if Entrada == 0:
                print("Saliendo...")
                break
            if Entrada == 1:
                print()
                print("Cesar Codificación")
                print()
                print("Codificación: 1")
                print("Decodificación: 2")
                try:
                    Entrada=int(input("Digite su respuesta: "))
                except ValueError:
                    print()
                    print("Debe elegie entre 1 y 2")
                    print()
                if Entrada==1:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                    try:
                        desplazamiento=int(input("Digite el desplazamiento: "))
                    except ValueError:
                        print()
                        print("El desplazamiento debe ser un entero")
                        print()
                    cesarCod(texto, desplazamiento)    
                if Entrada==2:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                        return
                    try:
                        desplazamiento=int(input("Digite el desplazamiento: "))
                    except ValueError:
                        print()
                        print("El desplazamiento debe ser un entero")
                        print()
                    cesarDec(texto, desplazamiento)
            if Entrada == 2:
                print()
                print("Monoalfabeto Codificación")
                print()
                print("Codificación: 1")
                print("Decodificación: 2")
                try:
                    Entrada=int(input("Digite su respuesta: "))
                except ValueError:
                    print()
                    print("Debe elegie entre 1 y 2")
                    print()
                if Entrada==1:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                    try:
                        Palabra_Clave=input("Digite la palabra clave: ")
                    except ValueError:
                        print()
                        print("La palabra clave debe ser un texto sin espacios")
                        print()
                    try:
                        for letra in Palabra_Clave:
                            if letra == " ":
                                return Exception("La palabra clave debe ser un texto sin espacios")
                    except Exception as e:
                        print(f"Error:{e}")
                    monoCod(texto, Palabra_Clave)    
                if Entrada==2:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                        return
                    try:
                        Palabra_Clave=input("Digite la palabra clave: ")
                    except ValueError:
                        print()
                        print("La palabra clave debe ser un texto sin espacios")
                        print()
                    try:
                        for letra in Palabra_Clave:
                            if letra == " ":
                                return Exception("La palabra clave debe ser un texto sin espacios")
                    except Exception as e:
                        print(f"Error:{e}")
                    monoDec(texto, Palabra_Clave)
            if Entrada == 3:
                print()
                print("Viegenere Codificación")
                print()
                print("Codificación: 1")
                print("Decodificación: 2")
                try:
                    Entrada=int(input("Digite su respuesta: "))
                except ValueError:
                    print()
                    print("Debe elegie entre 1 y 2")
                    print()
                if Entrada==1:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                    try:
                        Palabra_Clave=input("Digite la palabra clave: ")
                    except ValueError:
                        print()
                        print("La palabra clave debe ser un texto sin espacios")
                        print()
                    try:
                        for letra in Palabra_Clave:
                            if letra == " ":
                                return Exception("La palabra clave debe ser un texto sin espacios")
                    except Exception as e:
                        print(f"Error:{e}")
                    vigenereCod(texto, Palabra_Clave)    
                if Entrada==2:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                        return
                    try:
                        Palabra_Clave=input("Digite la palabra clave: ")
                    except ValueError:
                        print()
                        print("La palabra clave debe ser un texto sin espacios")
                        print()
                    try:
                        for letra in Palabra_Clave:
                            if letra == " ":
                                return Exception("La palabra clave debe ser un texto sin espacios")
                    except Exception as e:
                        print(f"Error:{e}")
                    vigenereDec(texto, Palabra_Clave)
            if Entrada == 4:
                print()
                print("Playfair Codificación")
                print()
                print("Codificación: 1")
                print("Decodificación: 2")
                try:
                    Entrada=int(input("Digite su respuesta: "))
                except ValueError:
                    print()
                    print("Debe elegie entre 1 y 2")
                    print()
                if Entrada==1:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                    try:
                        Palabra_Clave=input("Digite la palabra clave: ")
                    except ValueError:
                        print()
                        print("La palabra clave debe ser un texto sin espacios")
                        print()
                    try:
                        for letra in Palabra_Clave:
                            if letra == " ":
                                return Exception("La palabra clave debe ser un texto sin espacios")
                    except Exception as e:
                        print(f"Error:{e}")
                    playfairCod(texto, Palabra_Clave)    
                if Entrada==2:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                        return
                    try:
                        Palabra_Clave=input("Digite la palabra clave: ")
                    except ValueError:
                        print()
                        print("La palabra clave debe ser un texto sin espacios")
                        print()
                    try:
                        for letra in Palabra_Clave:
                            if letra == " ":
                                return Exception("La palabra clave debe ser un texto sin espacios")
                    except Exception as e:
                        print(f"Error:{e}")
                    playfairDec(texto, Palabra_Clave)
            if Entrada == 5:
                print()
                print("Railfance Codificación")
                print()
                print("Codificación: 1")
                print("Decodificación: 2")
                try:
                    Entrada=int(input("Digite su respuesta: "))
                except ValueError:
                    print()
                    print("Debe elegie entre 1 y 2")
                    print()
                if Entrada==1:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()

                    railfenceCod(texto, Palabra_Clave)    
                if Entrada==2:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                        return
                    railfenceDec(texto)
                    
            if Entrada == 6:
                print()
                print("Escitala Codificación")
                print()
                print("Codificación: 1")
                print("Decodificación: 2")
                try:
                    Entrada=int(input("Digite su respuesta: "))
                except ValueError:
                    print()
                    print("Debe elegie entre 1 y 2")
                    print()
                if Entrada==1:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                    try:
                        Palabra_Clave=input("Digite la palabra clave: ")
                    except ValueError:
                        print()
                        print("La palabra clave debe ser un texto sin espacios")
                        print()
                    try:
                        for letra in Palabra_Clave:
                            if letra == " ":
                                return Exception("La palabra clave debe ser un texto sin espacios")
                    except Exception as e:
                        print(f"Error:{e}")
                    escitalaCod(texto, lineas)    
                if Entrada==2:
                    try:
                        texto=input("Digite el texto: ")
                    except ValueError:
                        print()
                        print("El texto debe ser una frase o palabra sin comillas")
                        print()
                        return
                    try:
                        lineas=int(input("Digite las lineas: "))
                    except ValueError:
                        print()
                        print("Las lineas debe ser un entero mayor que 1")
                        print()
                    try:
                        if lineas<1:
                            raise Exception ("Las lineas debe ser un entero mayor que 1")
                    except:
                        print(f"Error: {e}")
                    
                    escitalaDec(texto, lineas)
        except Exception as e:
            print()
            print("Reiniciando...")
            print()
        except ValueError:
            print()
            print("Reiniciando...")
            print()

   
Main()
