import numpy as np
from mapa import Pared
from mapa import Mapa
from mapa import Monstruo
from mapa import Personaje
from mapa import MoverPersonaje
from mapa import CeldaGenerica
from problema_espacio_estados import ProblemaWappo
import busqueda_espacio_estados as busqee
import random as rndm
from representacion_grafica import representation
from time import time

# Tipos de casillas:
# 0 -> Normal
# 1 -> Ardiente
# 2 -> Objetivo
# 3 -> Inaccesible
# 4 -> Teletransporte
# 5 -> Fuego

""" MAPAS """

""" NIVEL 0 """
    
matrix = np.zeros((6, 7))

for i in range(0,6):
    matrix[i,6] = 3

matrix[2,6] = 2

pared1 = Pared(0,0,1,0)
pared2 = Pared(1,0,1,1)
pared3 = Pared(2,0,2,1)
pared4 = Pared(3,0,3,1)

paredes = [pared1, pared2, pared3, pared4]

personaje = Personaje(4, 2)

monstruo = Monstruo(1, 0)

mapa = Mapa(matrix, paredes, monstruo, personaje)



""" NIVEL 1 

matrix = np.zeros((7, 6))

for i in range(0,6):
    matrix[6,i] = 3
    
matrix[6,3] = 2

matrix[1,1] = 1

pared1 = Pared(0,5,1,5)
pared2 = Pared(1,4,1,5)
pared3 = Pared(5,5,5,4)
pared4 = Pared(0,3,1,3)
pared5 = Pared(1,1,2,1)

paredes = [pared1, pared2, pared3, pared4, pared5]

personaje = Personaje(1,3)

monstruo = Monstruo(1,5)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 2 

matrix = np.zeros((7, 6))

for i in range(0,6):
    matrix[6,i] = 3
    
matrix[6,1] = 2

matrix[1,2] = 1

pared1 = Pared(1,0,2,0)
pared2 = Pared(4,0,5,0)
pared3 = Pared(4,1,5,1)
pared4 = Pared(3,3,4,3)
pared5 = Pared(4,4,5,4)

paredes = [pared1, pared2, pared3, pared4, pared5]

personaje = Personaje(4,4)

monstruo = Monstruo(5,5)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 3 

matrix = np.zeros((7, 6))

for i in range(0,6):
    matrix[6,i] = 3
    
matrix[6,2] = 2

matrix[4,3] = 1
matrix[3,5] = 1

pared1 = Pared(0,2,1,2)
pared2 = Pared(0,4,1,4)
pared3 = Pared(1,3,1,4)
pared4 = Pared(2,0,2,1)
pared5 = Pared(2,2,3,2)
pared6 = Pared(2,3,3,3)
pared7 = Pared(3,3,4,3)
pared8 = Pared(5,0,5,1)
pared9 = Pared(5,1,5,2)
pared10 = Pared(4,3,5,3)
pared11 = Pared(5,3,5,4)
pared12 = Pared(4,4,5,4)


paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8, pared9, pared10, pared11, pared12]

personaje = Personaje(5,5)

monstruo = Monstruo(2,3)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 4 

matrix = np.zeros((6,7))

for i in range(0,6):
    matrix[i,6] = 3
    
matrix[3,6] = 2

matrix[4,2] = 1

pared1 = Pared(0,1,0,2)
pared2 = Pared(0,2,0,3)
pared3 = Pared(1,1,2,1)
pared4 = Pared(2,1,2,2)
pared5 = Pared(1,4,2,4)
pared6 = Pared(2,4,2,5)
pared7 = Pared(3,0,4,0)
pared8 = Pared(4,0,5,0)
pared9 = Pared(5,3,5,4)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8, pared9]

personaje = Personaje(4,0)

monstruo = Monstruo(0,0)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 5 

matrix = np.zeros((7,6))

for i in range(0,6):
    matrix[0,i] = 3
    
matrix[0,5] = 2

matrix[2,0] = 1

pared1 = Pared(2,0,3,0)
pared2 = Pared(2,2,3,2)
pared3 = Pared(4,1,4,2)
pared4 = Pared(5,1,5,2)
pared5 = Pared(5,1,6,1)
pared6 = Pared(2,4,3,4)
pared7 = Pared(1,4,1,5)
pared8 = Pared(4,4,5,4)
pared9 = Pared(4,5,5,5)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8, pared9]

personaje = Personaje(1,1)

monstruo = Monstruo(2,2)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 6 

matrix = np.zeros((7,6))

for i in range(0,6):
    matrix[0,i] = 3
    
matrix[0,5] = 2

matrix[6,1] = 1
matrix[5,5] = 1

pared1 = Pared(2,1,3,1)
pared2 = Pared(3,0,3,1)
pared3 = Pared(4,0,4,1)
pared4 = Pared(4,1,5,1)
pared5 = Pared(5,2,5,3)
pared6 = Pared(2,4,3,4)
pared7 = Pared(3,4,3,5)
pared8 = Pared(3,5,4,5)
pared9 = Pared(4,5,5,5)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8, pared9]

personaje = Personaje(5,3)

monstruo = Monstruo(4,5)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 7 

matrix = np.zeros((7,6))

for i in range(0,6):
    matrix[6,i] = 3
    
matrix[6,1] = 2

matrix[1,2] = 1
matrix[0,4] = 1

pared1 = Pared(0,0,1,0)
pared2 = Pared(0,1,1,1)
pared3 = Pared(1,0,1,1)
pared4 = Pared(5,0,5,1)
pared5 = Pared(4,1,4,2)
pared6 = Pared(4,2,5,2)
pared7 = Pared(2,3,3,3)
pared8 = Pared(1,5,2,5)
pared9 = Pared(4,4,5,4)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8, pared9]

personaje = Personaje(3,5)

monstruo = Monstruo(5,4)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 8 

matrix = np.zeros((7,6))

for i in range(0,6):
    matrix[0,i] = 3
    
matrix[0,0] = 2

matrix[2,4] = 1
matrix[5,5] = 1

pared1 = Pared(1,0,1,1)
pared2 = Pared(2,1,2,2)
pared3 = Pared(3,2,3,3)
pared4 = Pared(3,0,3,1)
pared5 = Pared(3,1,4,1)
pared6 = Pared(4,1,4,2)
pared7 = Pared(4,3,5,3)
pared8 = Pared(5,2,6,2)
pared9 = Pared(5,3,6,3)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8, pared9]

personaje = Personaje(6,3)

monstruo = Monstruo(3,2)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 9 

matrix = np.zeros((7,6))

for i in range(0,6):
    matrix[0,i] = 3
    
matrix[0,0] = 2

matrix[5,1] = 1

pared1 = Pared(4,0,5,0)
pared2 = Pared(4,1,5,1)
pared3 = Pared(4,1,4,2)
pared4 = Pared(3,3,3,4)
pared5 = Pared(4,3,5,3)
pared6 = Pared(4,4,5,4)
pared7 = Pared(5,3,6,3)
pared8 = Pared(6,4,6,5)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8]

personaje = Personaje(5,4)

monstruo = Monstruo(4,1)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 10 

matrix = np.zeros((6,7))

for i in range(0,6):
    matrix[i,0] = 3
    
matrix[3,0] = 2

matrix[4,3] = 1

pared1 = Pared(1,1,1,2)
pared2 = Pared(1,2,2,2)
pared3 = Pared(2,3,3,3)
pared4 = Pared(1,4,1,5)
pared5 = Pared(1,4,2,4)
pared6 = Pared(0,5,1,5)
pared7 = Pared(5,2,5,3)
pared8 = Pared(4,6,5,6)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8]

personaje = Personaje(5,3)

monstruo = Monstruo(1,2)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 11 

matrix = np.zeros((7,6))

for i in range(0,6):
    matrix[6,i] = 3
    
matrix[6,3] = 2

matrix[1,5] = 1

pared1 = Pared(0,1,0,2)
pared2 = Pared(1,1,2,1)
pared3 = Pared(1,2,2,2)
pared4 = Pared(1,2,1,3)
pared5 = Pared(0,3,1,3)
pared6 = Pared(2,3,3,3)
pared7 = Pared(3,2,3,3)
pared8 = Pared(2,4,2,5)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8]

personaje = Personaje(2,2)

monstruo = Monstruo(5,2)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 13 

matrix = np.zeros((7,6))

for i in range(0,6):
    matrix[0,i] = 3
    
matrix[0,3] = 2
matrix[5,1] = 1

pared1 = Pared(2,2,3,2)
pared2 = Pared(5,1,6,1)
pared3 = Pared(4,2,4,3)
pared4 = Pared(5,2,5,3)
pared5 = Pared(1,4,2,4)
pared6 = Pared(2,4,2,5)
pared7 = Pared(4,4,5,4)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7]

personaje = Personaje(3, 5)

monstruo = Monstruo(1, 1)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL 14 

matrix = np.zeros((7, 6))

for i in range(0,6):
    matrix[6,i] = 3
    
matrix[6,4] = 2

matrix[1,5] = 1

pared1 = Pared(1,1,2,1)
pared2 = Pared(4,1,5,1)
pared3 = Pared(3,3,4,3)
pared4 = Pared(4,3,5,3)
pared5 = Pared(4,4,5,4)
pared6 = Pared(4,4,4,5)
pared7 = Pared(2,4,2,5)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7]

personaje = Personaje(4, 1)

monstruo = Monstruo(5, 3)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL PRUEBA 0 
    
matrix = np.zeros((4, 6))

matrix[1,5] = 2

paredes = [Pared(1,3,1,4), Pared(2,3,2,4)]

matrix[1,1] = 1

personaje = Personaje(1, 2)

monstruo = Monstruo(1, 0)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL PRUEBA 1 
    
matrix = np.zeros((6, 6))

matrix[3,5] = 2

paredes = [Pared(1,1,1,2), Pared(2,1,2,2), Pared(3,1,3,2), Pared(2,3,3,3), Pared(2,4,3,4), Pared(2,4,2,5), Pared(1,4,1,5)]

personaje = Personaje(2, 4)

monstruo = Monstruo(1, 1)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL PRUEBA 2 
    
matrix = np.zeros((4, 3))

matrix[2,1] = 2

paredes = [Pared(0,0,0,1), Pared(0,0,1,0), Pared(1,1,2,1), Pared(1,1,1,2)]

personaje = Personaje(1, 1)

monstruo = Monstruo(0, 0)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" NIVEL PRUEBA 3

matrix = np.zeros((50, 6))

for i in range(0,6):
    matrix[49,i] = 3
    
matrix[49,3] = 2

matrix[1,1] = 1

pared1 = Pared(0,5,1,5)
pared2 = Pared(1,4,1,5)
pared3 = Pared(48,5,48,4)
pared4 = Pared(0,3,1,3)
pared5 = Pared(1,1,2,1)

paredes = [pared1, pared2, pared3, pared4, pared5]

personaje = Personaje(1,3)

monstruo = Monstruo(1,5)

mapa = Mapa(matrix, paredes, monstruo, personaje)

"""

""" SELECCION DE HEURISTICA """

""" HEURISTICA 1 """

def h(nodo):
    mapa = nodo.estado
    personaje = mapa.personaje
    
    listaObjetivo = []
    for i in range(0,mapa.tamaño_ver()):
        for j in range(0,mapa.tamaño_hor()):
            if(mapa.celdas[i, j] == 2):
                listaObjetivo.append(CeldaGenerica(i,j))
                break
    objetivo = listaObjetivo[0]
    
    return abs(objetivo.icelda - personaje.icelda) + abs(objetivo.jcelda - personaje.jcelda)
    


""" HEURISTICA 2

def h(nodo):
    mapa = nodo.estado
    monstruo = mapa.monstruo
    personaje = mapa.personaje
    
    listaObjetivo = []
    for i in range(0,mapa.tamaño_ver()):
        for j in range(0,mapa.tamaño_hor()):
            if(mapa.celdas[i, j] == 2):
                listaObjetivo.append(CeldaGenerica(i,j))
                break
    objetivo = listaObjetivo[0]
    long = [mapa.tamaño_ver(), mapa.tamaño_hor()]
    maxlong = max(long)
    
    distanciaPersonajeObjetivo = abs(objetivo.icelda - personaje.icelda) + abs(objetivo.jcelda - personaje.jcelda)
    distanciaMonstruoObjetivo = abs(objetivo.icelda - monstruo.icelda) + abs(objetivo.jcelda - monstruo.jcelda)
    distanciaPersonajeMonstruo = abs(monstruo.icelda - personaje.icelda) + abs(monstruo.jcelda - personaje.jcelda)
    
    # IMPORTANCIA SELECCION CASILLA ARDIENTE
    ardientes = []
    distanciaMonstruoArdientes = 0
    distanciaPersonajeArdientes = 0
    for i in range(0,mapa.tamaño_ver()):
        for j in range(0,mapa.tamaño_hor()):
            if(mapa.celdas[i, j] == 1):
                ardientes.append(CeldaGenerica(i,j))
                dist = abs(personaje.icelda - i) + abs(personaje.jcelda - j)
                if(dist < distanciaPersonajeArdientes or distanciaPersonajeArdientes == 0):
                    distanciaPersonajeArdientes = abs(personaje.icelda - i) + abs(personaje.jcelda - j)
                    distanciaMonstruoArdientes = abs(monstruo.icelda - i) + abs(monstruo.jcelda - j)
                
    # INICIO CALCULO HEURISTICA
    
    heuristica = 0
    if(len(ardientes) > 0 and distanciaPersonajeArdientes <= distanciaMonstruoArdientes and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo)):
        heuristica = 4*distanciaMonstruoArdientes
    elif(distanciaMonstruoObjetivo <= distanciaPersonajeObjetivo and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo)):
        heuristica = 2*maxlong - distanciaPersonajeObjetivo - distanciaPersonajeMonstruo
    else:
        heuristica = distanciaPersonajeObjetivo

    mov_i = objetivo.icelda - personaje.icelda
    mov_j = objetivo.jcelda - personaje.jcelda
    
    if(mov_j > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda + 1)):
        heuristica = heuristica + 1
    elif(mov_j < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda - 1)):
        heuristica = heuristica + 1
    elif(mov_i > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda + 1, personaje.jcelda)):
        heuristica = heuristica + 1
    elif(mov_i < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda - 1, personaje.jcelda)):
        heuristica = heuristica + 1
    
    return heuristica

"""

""" HEURISTICA 3

def h(nodo):
    mapa = nodo.estado
    monstruo = mapa.monstruo
    personaje = mapa.personaje
    
    listaObjetivo = []
    for i in range(0,mapa.tamaño_ver()):
        for j in range(0,mapa.tamaño_hor()):
            if(mapa.celdas[i, j] == 2):
                listaObjetivo.append(CeldaGenerica(i,j))
                break
    objetivo = listaObjetivo[0]
    long = [mapa.tamaño_ver(), mapa.tamaño_hor()]
    maxlong = max(long)
    
    distanciaPersonajeObjetivo = abs(objetivo.icelda - personaje.icelda) + abs(objetivo.jcelda - personaje.jcelda)
    distanciaMonstruoObjetivo = abs(objetivo.icelda - monstruo.icelda) + abs(objetivo.jcelda - monstruo.jcelda)
    distanciaPersonajeMonstruo = abs(monstruo.icelda - personaje.icelda) + abs(monstruo.jcelda - personaje.jcelda)
    
    # IMPORTANCIA SELECCION CASILLA ARDIENTE
    ardientes = []
    distanciaMonstruoArdientes = 0
    distanciaPersonajeArdientes = 0
    for i in range(0,mapa.tamaño_ver()):
        for j in range(0,mapa.tamaño_hor()):
            if(mapa.celdas[i, j] == 1):
                ardientes.append(CeldaGenerica(i,j))
                dist = abs(personaje.icelda - i) + abs(personaje.jcelda - j)
                if(dist > distanciaPersonajeArdientes or distanciaPersonajeArdientes == 0):
                    distanciaPersonajeArdientes = abs(personaje.icelda - i) + abs(personaje.jcelda - j)
                    distanciaMonstruoArdientes = abs(monstruo.icelda - i) + abs(monstruo.jcelda - j)
                
    # INICIO CALCULO HEURISTICA
    
    heuristica = 0
    if(len(ardientes) > 0 and distanciaPersonajeArdientes <= distanciaMonstruoArdientes and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo)):
        heuristica = 4*distanciaMonstruoArdientes
    elif(distanciaMonstruoObjetivo <= distanciaPersonajeObjetivo and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo)):
        heuristica = 2*maxlong - distanciaPersonajeObjetivo - distanciaPersonajeMonstruo
    else:
        heuristica = distanciaPersonajeObjetivo

    mov_i = objetivo.icelda - personaje.icelda
    mov_j = objetivo.jcelda - personaje.jcelda
    
    if(mov_j > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda + 1)):
        heuristica = heuristica + 1
    elif(mov_j < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda - 1)):
        heuristica = heuristica + 1
    elif(mov_i > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda + 1, personaje.jcelda)):
        heuristica = heuristica + 1
    elif(mov_i < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda - 1, personaje.jcelda)):
        heuristica = heuristica + 1
    
    return heuristica

"""

""" HEURISTICA 4

def h(nodo):
    mapa = nodo.estado
    monstruo = mapa.monstruo
    personaje = mapa.personaje
    
    listaObjetivo = []
    for i in range(0,mapa.tamaño_ver()):
        for j in range(0,mapa.tamaño_hor()):
            if(mapa.celdas[i, j] == 2):
                listaObjetivo.append(CeldaGenerica(i,j))
                break
    objetivo = listaObjetivo[0]
    long = [mapa.tamaño_ver(), mapa.tamaño_hor()]
    maxlong = max(long)
    
    distanciaPersonajeObjetivo = abs(objetivo.icelda - personaje.icelda) + abs(objetivo.jcelda - personaje.jcelda)
    distanciaMonstruoObjetivo = abs(objetivo.icelda - monstruo.icelda) + abs(objetivo.jcelda - monstruo.jcelda)
    distanciaPersonajeMonstruo = abs(monstruo.icelda - personaje.icelda) + abs(monstruo.jcelda - personaje.jcelda)
    
    # IMPORTANCIA SELECCION CASILLA ARDIENTE
    ardientes = []
    distanciaMonstruoArdientes = 0
    distanciaPersonajeArdientes = 0
    for i in range(0,mapa.tamaño_ver()):
        for j in range(0,mapa.tamaño_hor()):
            if(mapa.celdas[i, j] == 1):
                ardientes.append(CeldaGenerica(i,j))
    
    if(len(ardientes) > 0):
        ardiente = rndm.choice(ardientes)
        distanciaPersonajeArdientes = abs(personaje.icelda - ardiente.icelda) + abs(personaje.jcelda - ardiente.jcelda)
        distanciaMonstruoArdientes = abs(monstruo.icelda - ardiente.icelda) + abs(monstruo.jcelda - ardiente.jcelda)
    
    # INICIO CALCULO HEURISTICA
    
    heuristica = 0
    if(len(ardientes) > 0 and distanciaPersonajeArdientes <= distanciaMonstruoArdientes and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo)):
        heuristica = 4*distanciaMonstruoArdientes
    elif(distanciaMonstruoObjetivo <= distanciaPersonajeObjetivo and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo)):
        heuristica = 2*maxlong - distanciaPersonajeObjetivo - distanciaPersonajeMonstruo
    else:
        heuristica = distanciaPersonajeObjetivo

    mov_i = objetivo.icelda - personaje.icelda
    mov_j = objetivo.jcelda - personaje.jcelda
    
    if(mov_j > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda + 1)):
        heuristica = heuristica + 1
    elif(mov_j < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda - 1)):
        heuristica = heuristica + 1
    elif(mov_i > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda + 1, personaje.jcelda)):
        heuristica = heuristica + 1
    elif(mov_i < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda - 1, personaje.jcelda)):
        heuristica = heuristica + 1
    
    return heuristica
    
"""

""" HEURISTICA 5

def h(nodo):
	mapa = nodo.estado
	monstruo = mapa.monstruo
	personaje = mapa.personaje
	
	listaObjetivo = []
	for i in range(0,mapa.tamaño_ver()):
		for j in range(0,mapa.tamaño_hor()):
			if(mapa.celdas[i, j] == 2):
				listaObjetivo.append(CeldaGenerica(i,j))
				break
	objetivo = listaObjetivo[0]
	long = [mapa.tamaño_ver(), mapa.tamaño_hor()]
	maxlong = max(long)
	
	distanciaPersonajeObjetivo = abs(objetivo.icelda - personaje.icelda) + abs(objetivo.jcelda - personaje.jcelda)
	distanciaMonstruoObjetivo = abs(objetivo.icelda - monstruo.icelda) + abs(objetivo.jcelda - monstruo.jcelda)
	distanciaPersonajeMonstruo = abs(monstruo.icelda - personaje.icelda) + abs(monstruo.jcelda - personaje.jcelda)
	
	# IMPORTANCIA SELECCION CASILLA ARDIENTE
	ardientes = []
	distanciaMonstruoArdientes = 0
	distanciaPersonajeArdientes = 0
	for i in range(0,mapa.tamaño_ver()):
		for j in range(0,mapa.tamaño_hor()):
			if(mapa.celdas[i, j] == 1):
				ardientes.append(CeldaGenerica(i,j))
	
	if(len(ardientes) > 0):
		ardiente = rndm.choice(ardientes)
		distanciaPersonajeArdientes = abs(personaje.icelda - ardiente.icelda) + abs(personaje.jcelda - ardiente.jcelda)
		distanciaMonstruoArdientes = abs(monstruo.icelda - ardiente.icelda) + abs(monstruo.jcelda - ardiente.jcelda)
	
	dosParedesContiguasMonstruo = False
	if(dosParedesContiguasMonstruo == False):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda - 1, monstruo.jcelda) and mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda, monstruo.jcelda - 1)):
			dosParedesContiguasMonstruo == True
	if(dosParedesContiguasMonstruo == False):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda, monstruo.jcelda - 1) and mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda + 1, monstruo.jcelda)):
			dosParedesContiguasMonstruo == True
	if(dosParedesContiguasMonstruo == False):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda + 1, monstruo.jcelda) and mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda, monstruo.jcelda + 1)):
			dosParedesContiguasMonstruo == True
	if(dosParedesContiguasMonstruo == False):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda + 1, monstruo.icelda, monstruo.jcelda) and mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda - 1, monstruo.jcelda)):
			dosParedesContiguasMonstruo == True
		
	mov_i = personaje.icelda - monstruo.icelda
	mov_j = personaje.jcelda - monstruo.jcelda
	
	personajeLibre = True
	if(mov_i < 0):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda - 1, monstruo.jcelda) and personaje.icelda < monstruo.icelda):
			personajeLibre = personajeLibre and True
		else:
			personajeLibre = personajeLibre and False
	personajeLibre = True
	if(mov_i > 0):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda + 1, monstruo.jcelda) and personaje.icelda > monstruo.icelda):
			personajeLibre = personajeLibre and True
		else:
			personajeLibre = personajeLibre and False
	if(mov_j < 0):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda, monstruo.jcelda - 1) and personaje.jcelda < monstruo.jcelda):
			personajeLibre = personajeLibre and True
		else:
			personajeLibre = personajeLibre and False
	if(mov_j > 0):
		if(mapa.hay_pared(monstruo.icelda, monstruo.jcelda, monstruo.icelda, monstruo.jcelda + 1) and personaje.jcelda > monstruo.jcelda):
			personajeLibre = personajeLibre and True
		else:
			personajeLibre = personajeLibre and False
	
	# INICIO CALCULO HEURISTICA
	
	heuristica = 0
	if(len(ardientes) > 0 and distanciaPersonajeArdientes <= distanciaMonstruoArdientes and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo) and not(dosParedesContiguasMonstruo >= 2 and personajeLibre)):
		heuristica = 4*distanciaMonstruoArdientes
	elif(distanciaMonstruoObjetivo <= distanciaPersonajeObjetivo and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo) and not(dosParedesContiguasMonstruo and personajeLibre)):
		heuristica = 2*maxlong - distanciaPersonajeObjetivo - distanciaPersonajeMonstruo
	elif(dosParedesContiguasMonstruo and personajeLibre and not(monstruo.stun > 0) and not (distanciaMonstruoObjetivo >= 2*distanciaPersonajeObjetivo)):
		heuristica = 2*distanciaPersonajeObjetivo - distanciaPersonajeMonstruo
	else:
		heuristica = distanciaPersonajeObjetivo

	mov_i = objetivo.icelda - personaje.icelda
	mov_j = objetivo.jcelda - personaje.jcelda
	
	if(mov_j > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda + 1)):
		heuristica = heuristica + 1
	elif(mov_j < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda, personaje.jcelda - 1)):
		heuristica = heuristica + 1
	elif(mov_i > 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda + 1, personaje.jcelda)):
		heuristica = heuristica + 1
	elif(mov_i < 0 and mapa.hay_pared(personaje.icelda, personaje.jcelda, personaje.icelda - 1, personaje.jcelda)):
		heuristica = heuristica + 1
	
	return heuristica

"""

""" SELECCION DE COSTE """

""" COSTE 1 """

def coste(nodo):
    return 0



""" COSTE 2

def coste(nodo):
    return 1
    
"""

""" EJECUTAMOS """

estado_inicial = mapa
acciones = [MoverPersonaje(i, coste) for i in ["arriba", "abajo", "derecha", "izquierda"]]
Problema_Wappo = ProblemaWappo(acciones, estado_inicial)

print("- Calculando solucion... Si tarda demasiado es que el algoritmo no encuentra la solucion.")

t_inicial = time()

busq = busqee.BusquedaAEstrella(h, detallado=False)
# busq = busqee.BusquedaEnAnchura(detallado=False)
# busq = busqee.BusquedaEnProfundidad(detallado=False)

solucion = busq.buscar(Problema_Wappo)

t_final = time()

""" REPRESENTACION POR CONSOLA """

print("\n-- MAPA INICIAL --")
print(representation.graphicRepresentation(estado_inicial))
print("Solucion ({} movimientos): {}".format(len(solucion[0]), solucion[0]))
print('Tiempo de ejecución: {} segundos'.format(t_final - t_inicial))
print("Nodos explorados: {}".format(len(busq.explorados)))



""" REPRESENTACION EN FICHERO

archivo = open("resolucion_wappo.txt","w")

archivo.write('Solucion: {} movimientos\n'.format(len(solucion[0])))
archivo.write('Tiempo de ejecución: {} segundos\n'.format(t_final - t_inicial))
archivo.write('Nodos explorados: {}\n\n'.format(len(busq.explorados)))

archivo.write("-- MAPA INICIAL --\n\n")
archivo.write(representation.graphicRepresentation(estado_inicial))
archivo.write("\n")

archivo.write("-- ACCIONES --\n\n")

for i in range(0, len(solucion[0])):
    acciones_solucion = solucion[0]
    nodos_solucion = solucion[1]
    contador = i+1
    
    archivo.write("{}) ".format(contador) + acciones_solucion[i])
    archivo.write("\n")
    archivo.write(representation.graphicRepresentation(nodos_solucion[i]))
    archivo.write("\n")
    
archivo.close()

print("- Solucion generada en el fichero 'resolucion_wappo.txt'")

"""