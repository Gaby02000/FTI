import re

"""Programe una herramienta que pueda cifrar un texto segÃºn ciertas reglas de reemplazo (por ejemplo, todas las "la" por "1", las "un" por "2", etc.) y luego descifrarlo de nuevo usando expresiones regulares.
Ejemplo:
Entrada: "Hola Mundo"
Cifrado: "Ho1 M2do"
Descifrado: "Hola Mundo"""

reemplazos = {  # Diccionario de reemplazos
    'la': '1',
    'un': '2',
    'do': '3',
    'hola': '4',
    'mundo': '5',
    'es': '6',
    'una': '7',
    'prueba': '8',
    'texto': '9',
    'fundamentos': 'a',
    'teoricos': 'b',
    'noseQueMasPonerAca': 'c',
    
}

def cifrar(texto, diccionario): # Funcion de cifrado
    
    claves = diccionario.keys() 
    patron = '|'.join(claves) 
    reemplazo = lambda match: diccionario[match.group()] # Crear una func de reemplazo
    texto_cifrado = re.sub(patron, reemplazo, texto) # Aplicar el reemplazo
    return texto_cifrado 

def descifrar(texto, diccionario): # Funcion de descifrado
    valores = diccionario.values() 
    patron = '|'.join(valores) 
    dict_invertido = {v: k for k, v in diccionario.items()} # Invertir el diccionario
    reemplazo = lambda match: dict_invertido[match.group()] # Crear el reemplazo
    texto_descifrado = re.sub(patron, reemplazo, texto) # Aplicar el reemplazo
    return texto_descifrado 

def main():
    while True:
        try:
            cadena = input('Ingrese una cadena o 0 para salir: ')
            if cadena == '0':
                break    
            texto_cifrado = cifrar(cadena, reemplazos)
            print(f"Cifrado: {texto_cifrado}")

            texto_descifrado = descifrar(texto_cifrado, reemplazos)
            print(f"Descifrado: {texto_descifrado}")
        except KeyboardInterrupt:
            print("Chau")

if __name__ == "__main__":
    main()