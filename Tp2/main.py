import turtle
import random
import platform
from os import system
from InquirerPy import prompt

anguloRotacion = 36  
longitudLinea = 0

tamanioLinea={
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

def obtener_cadena():
    respuesta = [
        {
            "type": "list",
            "message": "¿Desea ingresar otra cadena?",
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
    respuesta = [
        {
            "type": "input",
            "name": "iteraciones",
            "message": "Ingrese las iteraciones",
        },
    ]
    respuesta = prompt(respuesta)
    return respuesta['iteraciones']

def obtener_velocidad():
    respuesta = [
        {
            "type": "input",
            "name": "velocidad",
            "message": "Ingrese la velocidad",
        },
    ]
    respuesta = prompt(respuesta)
    return respuesta['velocidad']

def obtener_colores():
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
    global longitudLinea
    limpiarConsola()
    colores = obtener_colores()
    limpiarConsola()
    while True:
        velocidad = int(obtener_velocidad())
        if velocidad >= 0 and velocidad <= 10:
            break
        else:
            limpiarConsola()
            print('Valor invalido.')
    limpiarConsola()
    while True:
        iteraciones = int(obtener_iteraciones())
        if iteraciones in tamanioLinea:
            longitudLinea = tamanioLinea[iteraciones]
            break
        else:
            limpiarConsola()
            print('Valor invalido.')
    limpiarConsola()
    return colores, iteraciones, velocidad

def aplicarReglas(cadena, iteraciones):
    i = 0
    while i<iteraciones:
        nuevaCadena = ''
        for x in cadena:
            if x in reglas:
                if x == 'F':
                    pass
                else: 
                    nuevaCadena += reglas[x]
            else:
                nuevaCadena += x
        cadena = nuevaCadena
        i += 1
    #print(cadena)
    return cadena

def dibujar(cadena,colores):
    pila = []
    for char in cadena:
        if char == 'F':
            turtle.forward(longitudLinea)#Dibuja una linea
        elif char == '+':
            turtle.left(anguloRotacion) #Gira a la izquierda
        elif char == '-':
            turtle.right(anguloRotacion) #Gira a la derecha
        elif char == '[':
            if len(pila) % 2 == 0:
                turtle.fillcolor(colores[0])  
            else:
                turtle.fillcolor(colores[1])  
            #turtle.color(random.choice(colores))
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

def limpiarConsola():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def configPantalla():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  
    screen.title("TP2 Grupo 6")
    screen.bgcolor("#09090b")
    screen.cv._rootwindow.attributes("-fullscreen", True) 
    return screen


    
def configTurtle(velocidad):
    turtle.speed(velocidad)  
    turtle.pencolor('white')
    turtle.pensize(1)
    turtle.goto(0, 0)

if __name__ == '__main__':
    limpiarConsola()
    cadenaInicial = obtener_cadena()
    colores, iteraciones, velocidad = menu()
    screen = configPantalla()
    configTurtle(velocidad)
    #centrarDibujo(screen) 
    print('Dibujando...')
    try:
        cadena = aplicarReglas(cadenaInicial, iteraciones)
        dibujar(cadena,colores)
        turtle.done() 
        
    except KeyboardInterrupt as e:
        print("Chau")