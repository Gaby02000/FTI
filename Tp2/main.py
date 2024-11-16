import turtle
import random
import platform
from os import system
from InquirerPy import prompt
from rich.console import Console

console = Console()

angulo_rotacion = 36  
longitud_linea = 0

tamanio_linea={
    1: 70,
    2: 60,  
    3: 50,
    4: 45,
    5: 40,
    6: 35,
    7: 30,
    8: 25,
    9: 20,
    10: 10,
    11: 5
}

reglas={
    'A': 'CF++DF----BF[-CF----AF]++',
    'B': '+CF--DF[---AF--BF]+',
    'C': '-AF++BF[+++CF++DF]-',
    'D': '--CF++++AF[+DF++++BF]--BF',
    'F': None
}

velocidades = {
    'Rapidisimo 🏎️' :  0,
    'Rapido 🚗'    :  10,
    'Normalito 🚌'  :  6,
    'Lento 🐎'    :  3,
    'Lenteja modo turtle 🐢' :  1
}

def mostrar_titulo_ascii(titulo):
    marco = "═" * (len(titulo) + 4)
    console.print(f"╔{marco}╗", style="bold yellow")
    console.print(f"║ {titulo} ║", style="bold green")
    console.print(f"╚{marco}╝", style="bold yellow")
    
def obtener_cadena():
    mostrar_titulo_ascii("⛓️‍💥 DESEA INGRESAR OTRA CADENA? ⛓️‍💥")
    respuesta = [
        {
            "type": "list",
            "message": "🚽",
            "choices": ["Si", "No"],
            "name": "opcion"
        },
    ]
    respuesta = prompt(respuesta)
    
    if respuesta['opcion'] == "No":
        cadena = "[B]++[B]++[B]++[B]++[B]"
    else:
        pregunta_cadena = [
            {
                "type": "input",
                "name": "cadena",
                "message": "Ingrese la cadena:",
                "default": "[B]++[B]++[B]++[B]++[B]",
            },
        ]
        respuesta_cadena = prompt(pregunta_cadena)
        cadena = respuesta_cadena['cadena']
    
    return cadena

def obtener_iteraciones():
    mostrar_titulo_ascii("🎡 INGRESE LAS ITERACIONES 🎡")
    respuesta = [
        {
            "type": "input",
            "name": "iteraciones",
            "message": "💀 =>",
        },
    ]
    respuesta = prompt(respuesta)
    return respuesta['iteraciones']

def obtener_velocidad():
    mostrar_titulo_ascii("🎰 SELECCIONE LA VELOCIDAD 🎰")
    respuesta = [
        {
            "type": "list",
            "name": "velocidad",
            "message": "🗿",
            "choices": list(velocidades.keys())
        },
    ]
    respuesta = prompt(respuesta)
    return velocidades[respuesta['velocidad']]

def obtener_colores():
    mostrar_titulo_ascii("🎨 SELECCIONE LOS COLORES 🎨")
    lista_colores = [
        "white", "black", "red", "green", "blue", "cyan", "yellow", "magenta",
        "maroon", "lime", "navy", "teal", "purple", "olive", "gray", "silver",
        "orange", "brown", "pink", "gold", "violet", "indigo", "turquoise"
    ]
    
    pregunta_colores = [
        {
            "type": "list",
            "name": "color1",
            "message": "Seleccione el primer color:",
            "choices": lista_colores
        },
        {
            "type": "list",
            "name": "color2",
            "message": "Seleccione el segundo color:",
            "choices": lista_colores
        }
    ]
    
    respuestas = prompt(pregunta_colores)
    return respuestas['color1'], respuestas['color2']
def menu():
    global longitud_linea
    limpiar_consola()
    colores = obtener_colores()
    limpiar_consola()
    while True:
        velocidad = int(obtener_velocidad())
        if velocidad >= 0 and velocidad <= 10:
            break
        else:
            limpiar_consola()
            print('Valor invalido.')
    limpiar_consola()
    while True:
        iteraciones = int(obtener_iteraciones())
        if iteraciones in tamanio_linea:
            longitud_linea = tamanio_linea[iteraciones]
            break
        else:
            limpiar_consola()
            print('Valor invalido.')
    limpiar_consola()
    return colores, iteraciones, velocidad

def aplicar_reglas(cadena, iteraciones):
    i = 0
    while i<iteraciones:
        nueva_cadena = ''
        for x in cadena:
            if x in reglas:
                if x == 'F':
                    pass
                else: 
                    nueva_cadena += reglas[x]
            else:
                nueva_cadena += x
        cadena = nueva_cadena
        i += 1
    #print(cadena)
    return cadena

def dibujar(cadena,colores):
    pila = []
    for char in cadena:
        if char == 'F':
            turtle.forward(longitud_linea)#Dibuja una linea
        elif char == '+':
            turtle.left(angulo_rotacion) #Gira a la izquierda
        elif char == '-':
            turtle.right(angulo_rotacion) #Gira a la derecha
        elif char == '[':
            if len(pila) % 2 == 0:
                turtle.fillcolor(colores[0])  
            else:
                turtle.fillcolor(colores[1])  
                turtle.begin_fill()
            pila.append((turtle.position(), turtle.heading())) #Apilo
        elif char == ']':
            turtle.end_fill()
            posicion, heading = pila.pop() #Despilo
            turtle.penup()
            turtle.setposition(posicion)
            turtle.setheading(heading)
            turtle.pendown()
    print('Dibujo terminado')

def limpiar_consola():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def config_pantalla():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  
    screen.title("TP2 Grupo 6")
    screen.bgcolor("#09090b")
    screen.cv._rootwindow.attributes("-fullscreen", True) 
    return screen


    
def config_turtle(velocidad):
    turtle.speed(velocidad)  
    turtle.pencolor('white')
    turtle.pensize(1)
    turtle.goto(0, 0)

if __name__ == '__main__':
    limpiar_consola()
    cadena_inicial = obtener_cadena()
    colores, iteraciones, velocidad = menu()
    screen = config_pantalla()
    config_turtle(velocidad)
    print('Dibujando...')
    try:
        cadena = aplicar_reglas(cadena_inicial, iteraciones)
        dibujar(cadena,colores)
        turtle.done() 
        
    except KeyboardInterrupt as e:
        print("Chau")