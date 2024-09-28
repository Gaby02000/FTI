import re

# Diccionario de reemplazos
reemplazos = {
    'la': '1',
    'un': '2',
    'do': '3',
    'hola': '4',
    'mundo': '5',
    'es': '6',
    'una': '7',
    'prueba': '8',
    'texto': '9',
    'cifrar': '10',
    'descifrar': '11',
    'ejemplo': '12',
    'mensaje': '13',
    'clave': '14',
    'valor': '15',
    'cadena': '16',
    'entrada': '17',
    'salida': '18',
    
}

def cifrar(texto, reglas):
    claves = reglas.keys() 
    patron = '|'.join(claves) 
    reemplazo = lambda match: reglas[match.group(0)] # Crear una func de reemplazo
    texto_cifrado = re.sub(patron, reemplazo, texto) # Aplicar el reemplazo
    return texto_cifrado 

def descifrar(texto, reglas):
    valores = reglas.values() 
    patron = '|'.join(valores) 
    reglas_invertidas = {v: k for k, v in reglas.items()} # Invertir el diccionario
    reemplazo = lambda match: reglas_invertidas[match.group(0)] # Crear el reemplazo
    texto_descifrado = re.sub(patron, reemplazo, texto) # Aplicar el reemplazo
    return texto_descifrado 

def main():
    while True:
        cadena = input('Ingrese una cadena o 0 para salir: ')
        if cadena == '0':
            break    
        texto_cifrado = cifrar(cadena, reemplazos)
        print(f"Cifrado: {texto_cifrado}")

        texto_descifrado = descifrar(texto_cifrado, reemplazos)
        print(f"Descifrado: {texto_descifrado}")

if __name__ == "__main__":
    main()
