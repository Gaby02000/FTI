import turtle
import random

anguloRotacion = 36  
longitudLinea = 20
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("TP2 Grupo 6")
screen.bgcolor("black")

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
    print(cadena)
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

def configTurtle(velocidad):
    turtle.speed(velocidad)  
    turtle.pencolor('white')
    turtle.pensize(1)

def menu():
    colores = input('Elegi dos colores separados por comas: ')
    while True:
        velocidad = int(input('Elegi la velocidad de dibujo: '))
        if velocidad >= 0 and velocidad <= 10:
            break
        else:
            print('Valor invalido.')
    while True:
        iteraciones = int(input('Elegi la cantidad de iteraciones: '))
        if iteraciones > 0:
            break
        else:
            print('Valor invalido.')
    return colores, iteraciones, velocidad

if __name__ == '__main__':
    x = input('desea agregar otra cadena inicial? (s/n): ')
    if x == 's':
        cadenaInicial = input('ingrese cadena inicial: ')
    else:
        cadenaInicial = "[B]++[B]++[B]++[B]++[B]"
    colores, iteraciones, velocidad = menu()
    configTurtle(velocidad)
    try:
        cadena=aplicarReglas(cadenaInicial, iteraciones)
        dibujar(cadena,colores)
        turtle.done() 
    except KeyboardInterrupt as e:
        print("Chau")