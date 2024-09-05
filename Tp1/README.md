# Proyecto de Cifrado y Descifrado de Texto

Este es un proyecto simple desarrollado por Agustín Bowen, Scott Ellis y Gabriel José Federico Miguel Guimenez, como parte de un ejercicio universitario. El programa permite cifrar y descifrar texto basado en reglas predefinidas.

## Descripción

El programa utiliza expresiones regulares para reemplazar cadenas de texto según un diccionario de reglas. Hay dos funciones principales:

- **Cifrado:** Reemplaza ciertas secuencias de caracteres en el texto por valores asociados.
- **Descifrado:** Revierte el proceso de cifrado utilizando el diccionario invertido para restaurar el texto original.

### Reglas de Cifrado/Descifrado

El diccionario de reemplazos contiene las siguientes reglas:

- "la" → "1"
- "un" → "2"
- "do" → "3"

Estas reglas se aplican tanto en el proceso de cifrado como en el de descifrado.

## Ejecución del Programa

Para ejecutar el programa, sigue los siguientes pasos:

1. Clona el repositorio o descarga el archivo `main.py`.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta el programa con el siguiente comando en la terminal:

```bash
python main.py
```

4. El programa solicitará ingresar una cadena de texto. Tras ingresar el texto, el programa mostrará la versión cifrada y, posteriormente, descifrada.
5. Ingresa `0` para salir del programa.

## Ejemplo de Uso

```bash
Ingrese una cadena o 0 para salir: hola mundo
Cifrado: ho13 mu2
Descifrado: hola mundo
```

## Dependencias

El programa solo requiere Python 3.x y utiliza la librería estándar `re` para manejar expresiones regulares.


