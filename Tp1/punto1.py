import re
import sys

def reemplazar(match, reglas):
    return reglas[match.group(0)]
def cifrar(texto, reglas):
        patron = '|'.join(re.escape(clave) for clave in reglas.keys()) #busca la clave en el dic de reglas
        def reemplazar(match): #reemplaza usando las reglas
            return reglas[match.group(0)]
        texto_cifrado = re.sub(patron, reemplazar, texto)
        return texto_cifrado

def descifrar(texto, reglas):
        patron = '|'.join(re.escape(valor) for valor in reglas.values())#buca los valores en el diccionario
        reglas_invertidas = {v: k for k, v in reglas.items()}# Invertir las reglas para el descifrado
        def reemplazar(match):
            return reglas_invertidas[match.group(0)]
        texto_descifrado = re.sub(patron, reemplazar, texto)
        return texto_descifrado

def main():
    
    reemplazos = {
        'la': '1',
        'un': '2',
        'do': '3'
    }
    while True:
        cadena=input('Ingrese una cadena o 0 para salir: ')
        if cadena == '0':
            break    
        texto_original = cadena
        texto_cifrado = cifrar(texto_original, reemplazos)
        print(f"Cifrado: {texto_cifrado}")

        texto_descifrado = descifrar(texto_cifrado, reemplazos)
        print(f"Descifrado: {texto_descifrado}")


if __name__ == "__main__":
    main()