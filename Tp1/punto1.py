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
    'salida': '18'
}

def cifrar(texto, reglas):
    patron = '|'.join(re.escape(clave) for clave in reglas.keys())
    return re.sub(patron, lambda match: reglas[match.group(0)], texto)

def descifrar(texto, reglas):
    patron = '|'.join(re.escape(valor) for valor in reglas.values())
    reglas_invertidas = {v: k for k, v in reglas.items()}
    return re.sub(patron, lambda match: reglas_invertidas[match.group(0)], texto)

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
