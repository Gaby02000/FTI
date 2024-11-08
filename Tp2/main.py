import turtle
import random
import platform
from os import system

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
    colores = colores.split(", ")
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
    screen.bgcolor("black")
    screen.cv._rootwindow.attributes("-fullscreen", True) 
    return screen


    
def configTurtle(velocidad):
    turtle.speed(velocidad)  
    turtle.pencolor('white')
    turtle.pensize(1)
    turtle.goto(0, 0)

def menu():
    global longitudLinea
    colores = input('Elegi dos colores separados por comas: ')
    limpiarConsola()
    while True:
        velocidad = int(input('Elegi la velocidad de dibujo: '))
        if velocidad >= 0 and velocidad <= 10:
            break
        else:
            limpiarConsola()
            print('Valor invalido.')
    limpiarConsola()
    while True:
        iteraciones = int(input('Elegi la cantidad de iteraciones: '))
        if iteraciones in tamanioLinea:
            longitudLinea = tamanioLinea[iteraciones]
            break
        else:
            limpiarConsola()
            print('Valor invalido.')
    limpiarConsola()
    return colores, iteraciones, velocidad

if __name__ == '__main__':
    
    x = input('desea agregar otra cadena inicial? (s/n): ')
    if x == 's':
        cadenaInicial = input('ingrese cadena inicial: ')
    else:
        cadenaInicial = "[B]++[B]++[B]++[B]++[B]"
    limpiarConsola()
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