import math 
import os
import random
import re
import sys

def tablerocerrado (fila, columna, tablero):
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

def movimiento(fila, columna, tablero):
    while fila == 1:
        if tablero[fila+1][columna] != '':
            tablero[fila-1][columna] == tablero[fila][columna]
            tablero[fila][columna]= ''
        else:
            tablero[fila+1][columna] == tablero[fila][columna]:
            tablero[fila][columna]= ''
    if fila == 0:
        tablero[fila+1][columna] =  tablero[fila][columna]
        tablero[fila][columna]= ''
    elif fila == 2:
        tablero[fila-1][columna] = tablero[fila][columna]
        tablero [fila][columna] = ''

