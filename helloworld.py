import os 
os.system("cls") # Clear screen in WINDOWS

import math 
print('hello, world')
if (13!=13):
    print('13 es mayor que 10')
else:
    print('No va ocurrir')

cociente = 7/3
resto = 7%3
mult = 7*3
print(math.sqrt(8))
print(math.isqrt(8))
print(cociente)

# Funcion numeros pares
def es_par(x):
    if (x%2==0):
        print('es par')
    else:
        print('es impar')
es_par(2)

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
es_primo(8)


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
is_rgb("rojo")
