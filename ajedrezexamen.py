import math 
import os
import random
import re
import sys
from random import randint

def encerrada (fila, columna):
    if fila ==0 and tablero [fila+1][columna] != '':
        fallo= True

    elif fila == 1:
        if tablero [fila+1][columna] != '' and tablero[fila-1][columna] != '':
            fallo = True

        else:
            fallo= False
    elif fila == 2 and tablero [fila-1][columna] != '':
        fallo = True
    else:
        fallo = True
    return fallo

def enseñartablero (tablero):
    contador = 0
    for tablero[contador] in tablero:
        print(tablero[contador])
    print("\n")

def movimiento(fila, columna):
    while fila == 1:
        if tablero[fila+1][columna] != '':
            tablero[fila-1][columna] == tablero[fila][columna]
            tablero[fila][columna]= ''
        else:
            tablero[fila+1][columna] == tablero[fila][columna]
            tablero[fila][columna]= ''
    if fila == 0:
        tablero[fila+1][columna] =  tablero[fila][columna]
        tablero[fila][columna]= ''
    elif fila == 2:
        tablero[fila-1][columna] = tablero[fila][columna]
        tablero [fila][columna] = ''

def cambio(fila, columna):
    if fila == 0:
        fila += 1
    elif fila == 1:
        if tablero[fila+1][columna] != '':
            fila -= 1
        else:
            fila+= 1
    elif fila == 2:
        fila -= 1
    return fila

#creacion del tablero

tablero= [
    [' ',' ',' '],

    [' ',' ',' '],

    [' ',' ',' '],
]

x = randint(0,2)
y = randint(0,2)
z = randint(0,2)
a = randint(0,2)
b = randint(0,2)
c = randint(0,2)

while x == a:
    a = randint(0,2)
while y == b:
    b = randint(0,2)
while z == c:
    c = randint(0,2)

(tablero[x])[0] = "♜"
(tablero[y])[1] = "♜"
(tablero[z])[2] = "♜"
(tablero[a])[0] = "♖"
(tablero[b])[1] = "♖"
(tablero[c])[2] = "♖"

print(tablero)

encerradax = encerrada(x, 0)
encerraday = encerrada(y, 1)
encerradaz = encerrada(z, 2)
encerradaa = encerrada(a, 0)
encerradab = encerrada(b, 1)
encerradac = encerrada(c, 2)


if encerradax == True and encerraday == True and encerradaz == True:
        print("El jugador blanco no se puede mover, volvemos a crear el tablero")
        pass
elif encerradaa == True and encerradab == True and encerradac == True:
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
        pass
else:
    breakpoint


turno = randint(0, 1)

while True:
    if turno == 1:
        if encerradax == False and encerradaa == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            encerradaa = encerrada(a, 0)
        elif encerraday == False and encerradab == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            encerradab = encerrada(b, 1)
        elif encerradaz == False and encerradac == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            encerradac = encerrada(c, 2)
        elif encerradax == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            encerradaa = encerrada(a, 0)
        elif encerraday == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            encerradab = encerrada(b, 1)
        elif encerradaz == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            encerradac = encerrada(c, 2)
        else:
            break
        turno = 0

    elif turno == 0:
        if encerradaa == False and encerradax == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            encerradax = encerrada(x, 0)
        elif encerradab == False and encerraday == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            encerraday = encerrada(y, 1)
        elif encerradac == False and encerradaz == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            encerradaz = encerrada(z, 2)
        elif encerradaa == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            encerradax = encerrada(x, 0)
        elif encerradab == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            encerraday = encerrada(y, 1)
        elif encerradac == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            encerradac = encerrada(z, 2)
        else:
            break
        turno = 1
    enseñartablero(tablero)

enseñartablero(tablero)
if encerradax == True and encerraday == True and encerradaz == True:
    print("Gana el jugador negro ya que el blanco no se puede mover")
elif encerradaa == True and encerradab == True and encerradac == True:
    print("Gana el jugador blanco ya que el negro no se puede mover")
