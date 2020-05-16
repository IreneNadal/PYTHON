# COMMENT = CTRL + K + C
# UNCOMMENT = CTRL + K + U
import os 
os.system("cls") # Clear screen in WINDOWS
import statistics 
import random
import array as arr 
import math 
print('hello, world')
if (13!=13):
    print('13 es mayor que 10')
else:
    print('No va ocurrir')

cociente = 7/3
resto = 7%3
mult = 7*3

# Funcion numeros pares
def es_par(x):
    if (x%2==0):
        print('es par')
    else:
        print('es impar')
#es_par(2)

# Funcion haz el cuadrado de x
def cuadrado(x):
    return x*x
print(cuadrado(2))

# Funcion números primos 
def es_primo(x):
    numbers = 1
    primo = 0
    while numbers<x:
        if(x%numbers==0):
            primo = primo+1
        numbers = numbers+1
    if (primo>1):
        print('El numero no es primo')
    else:
        print('El numero es primo')
#es_primo(8)


# Función para saber si el color es rgb (red - green - blue)
def is_rgb(color):
    colors = ["rojo","verde","azul"]
    rgb = False
    for x in colors:
        if(color==x):
            rgb = True
    if (rgb == True):
        print('Color es RGB')
    else:
        print('El color no es RGB')
#is_rgb("rojo")


# Función para saber que nota has sacado
def is_pass():
    notas = [random.random()*10 for x in range(20)]
    for x in notas:
        if(x<4.5):
            print(round(x,2),'Has supendido, compañero')
        elif(x<5):
            print(round(x,2),'Te hago media')
        elif(x<6):
            print(round(x,2),'Suficiente')
        elif(x<9.5):
            print(round(x,2),'Tienes un notable')
        elif(x<10):
            print(round(x,2),'Matrícula de honor')
    m = statistics.mean(notas)
    print("La media de la clase es",round(m,2))
is_pass()

def is_watermass(temp,salt):
    if temp >= 17.3 and temp <= 17.8 and salt >= 38.3 and salt <= 38.8:
        print('Water mass is WIW') 
    elif temp >= 16.9 and temp <= 17.4 and salt >= 36.5 and salt <= 37.1:
        print('Water mass is SAW')
    else:
        print('I have not found any water mass')

is_watermass(12.5,38.5)

# # price of PAN
# precio = 3.49
# descuento = 0.60
# precio_con_descuento = precio*(1-descuento)
# barras_vendidas = input('Cuantas barras de HOY has vendido:')
# barras_ayer = input('Cuantas barras de AYER has vendido:')
# print((int(barras_vendidas)-int(barras_ayer))*3.49 + int(barras_ayer)*precio_con_descuento)


# CONTRASEÑA
password = 'mango'
password_usuario = input('Introduzca su contraseña: ')
if password_usuario == password:
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')