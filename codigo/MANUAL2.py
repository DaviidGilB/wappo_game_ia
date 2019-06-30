import numpy as np
from mapa import Pared
from mapa import Mapa2
from mapa import Monstruo
from mapa import Personaje
from mapa import MoverPersonaje2
from mapa import CeldaGenerica
from problema_espacio_estados import ProblemaWappo
import busqueda_espacio_estados as busqee
from representacion_grafica import representation
from time import time

# Tipos de casillas:
# 0 -> Normal
# 1 -> Ardiente
# 2 -> Objetivo
# 3 -> Inaccesible

""" MAPAS """

""" NIVEL 12 """
    
matrix = np.zeros((6, 7))

for i in range(0,6):
    matrix[i,0] = 3

matrix[3,0] = 2
matrix[2,4] = 1

pared1 = Pared(0,3,0,4)
pared2 = Pared(1,2,1,3)
pared3 = Pared(5,2,5,3)
pared4 = Pared(1,4,1,5)
pared5 = Pared(4,4,5,4)
pared6 = Pared(2,5,3,5)
pared7 = Pared(0,6,1,6)
pared8 = Pared(1,5,1,6)

paredes = [pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8]

personaje = Personaje(1, 3)

monstruo1 = Monstruo(1, 1)

monstruo2 = Monstruo(5, 5)

mapa = Mapa2(matrix, paredes, monstruo1, monstruo2, personaje)



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
acciones = [MoverPersonaje2(i, coste) for i in ["arriba", "abajo", "derecha", "izquierda"]]
Problema_Wappo = ProblemaWappo(acciones, estado_inicial)

print("- Calculando solucion... Si tarda demasiado es que el algoritmo no encuentra la solucion.")

t_inicial = time()

busq = busqee.BusquedaAEstrella(h, detallado=False)
# busq = busqee.BusquedaEnAnchura(detallado=False)
# busq = busqee.BusquedaEnProfundidad(detallado=False)

solucion = busq.buscar(Problema_Wappo)

t_final = time()

""" REPRESENTACION POR CONSOLA 

print("\n-- MAPA INICIAL --")
print(representation.graphicRepresentation(estado_inicial))
print("Solucion ({} movimientos): {}".format(len(solucion[0]), solucion[0]))
print('Tiempo de ejecución: {} segundos'.format(t_final - t_inicial))
print("Nodos explorados: {}".format(len(busq.explorados)))

"""

""" REPRESENTACION EN FICHERO """

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

