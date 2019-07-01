import numpy as np
from mapa import Pared
from mapa import Mapa
from mapa import Mapa2
from mapa import Monstruo
from mapa import Personaje
from mapa import MoverPersonaje
from mapa import MoverPersonaje2
from mapa import CeldaGenerica
from problema_espacio_estados import ProblemaWappo
import busqueda_espacio_estados as busqee
import random as rndm
from representacion_grafica import representation
from time import time

class Script():
    def __init__(self):
        self.celdas = np.zeros((1,1))
        self.paredes = []
        self.monstruo = Monstruo(0,0)
        self.monstruo1 = Monstruo(0,0)
        self.monstruo2 = Monstruo(0,0)
        self.personaje = Personaje(0,0)
        self.filas = 1
        self.columnas = 1
        
        # OTRA INFORMACION
        self.precargado = False
        self.detallado = False
        self.heuristica = 1
        self.coste = 1
        self.algoritmo = 1
        self.enFichero = False
        self.numMonstruos = 0
        
    def limpiar(self):
        self.celdas = np.zeros((1,1))
        self.paredes = []
        self.monstruo = Monstruo(0,0)
        self.monstruo1 = Monstruo(0,0)
        self.monstruo2 = Monstruo(0,0)
        self.personaje = Personaje(0,0)
        self.filas = 1
        self.columnas = 1
        
        # OTRA INFORMACION
        self.precargado = False
        self.detallado = False
        self.heuristica = 1
        self.coste = 1
        self.algoritmo = 1
        self.enFichero = False
        self.numMonstruos = 0
    
    def ejecutar(self):
        print( "- Wappo Game", chr(1))
        print("¿Quieres usar un nivel precargado (1) o definir uno desde cero (2)?")
        res = input("Responda con uno de los números indicados entre paréntesis: ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                self.precargado = True
                self.preguntaNivel()
            elif(res == 2):
                self.precargado = False
                self.preguntarFilas()
                self.preguntarColumnas()
                self.celdas = np.zeros((self.filas, self.columnas))
                self.preguntarFilaColumnaInaccesible()
                self.preguntarObjetivo()
                self.preguntarPersonaje()
                self.preguntarMonstruo()
                self.preguntarAñadirOtroMonstruo()
                self.preguntarArdiente()
                self.preguntarTeletransporte()
                self.preguntarPared()
            else:
                print("Valor incorrecto.\n")
                self.ejecutar()
                
            self.representarYVerificar()
            self.preguntarAlgoritmo()
            self.preguntarDetallado()
            self.preguntarEnFichero()
            
            # RESOLUCIÓN
            if(self.numMonstruos == 1):
                estado_inicial = Mapa(self.celdas, self.paredes, self.monstruo, self.personaje)
            if(self.numMonstruos == 2):
                estado_inicial = Mapa2(self.celdas, self.paredes, self.monstruo1, self.monstruo2, self.personaje)
            
            if(self.coste == 2):
                
                def coste(nodo):
                    return 1
                
            else:
                
                def coste(nodo):
                    return 0
            
            if(self.numMonstruos == 1):
                acciones = [MoverPersonaje(i, coste) for i in ["arriba", "abajo", "derecha", "izquierda"]]
            if(self.numMonstruos == 2):
                acciones = [MoverPersonaje2(i, coste) for i in ["arriba", "abajo", "derecha", "izquierda"]]
            
            Problema_Wappo = ProblemaWappo(acciones, estado_inicial)
            
            if(self.algoritmo == 1):
                t_inicial = time()
                busq = busqee.BusquedaEnAnchura(detallado = self.detallado)
            elif(self.algoritmo == 2):
                t_inicial = time()
                busq = busqee.BusquedaEnProfundidad(detallado = self.detallado)
            elif(self.heuristica == 1):
                
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
                
                t_inicial = time()
                busq = busqee.BusquedaAEstrella(h, detallado = self.detallado)
            elif(self.heuristica == 2):
                
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
                
                t_inicial = time()
                busq = busqee.BusquedaAEstrella(h, detallado = self.detallado)
            elif(self.heuristica == 3):
                
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
                
                t_inicial = time()
                busq = busqee.BusquedaAEstrella(h, detallado = self.detallado)
            elif(self.heuristica == 4):
                
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
                
                t_inicial = time()
                busq = busqee.BusquedaAEstrella(h, detallado = self.detallado)
            else:
                
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
                
                t_inicial = time()
                busq = busqee.BusquedaAEstrella(h, detallado = self.detallado)
                
            print("- Calculando solucion... Si tarda demasiado es que el algoritmo no encuentra la solucion.")
            solucion = busq.buscar(Problema_Wappo)
            t_final = time()
            
            if(self.enFichero):
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
            else:
                print("\n-- MAPA INICIAL --")
                print(representation.graphicRepresentation(estado_inicial))
                print("Solucion ({} movimientos): {}".format(len(solucion[0]), solucion[0]))
                print('Tiempo de ejecución: {} segundos'.format(t_final - t_inicial))
                print("Nodos explorados: {}".format(len(busq.explorados)))

            print("\n==== FIN ====\n")            
                
        except ValueError:
            print("Entrada incorrecta.\n")
            self.ejecutar()
            
    def preguntaNivel(self):
        print("¿Qué nivel quieres cargar? Estos son los niveles disponibles:")
        print("- Nivel 0 del juego (1)")
        print("- Nivel 1 del juego (2)")
        print("- Nivel 2 del juego (3)")
        print("- Nivel 3 del juego (4)")
        print("- Nivel 4 del juego (5)")
        print("- Nivel 5 del juego (6)")
        print("- Nivel 6 del juego (7)")
        print("- Nivel 7 del juego (8)")
        print("- Nivel 8 del juego (9)")
        print("- Nivel 9 del juego (10)")
        print("- Nivel 10 del juego (11)")
        print("- Nivel 11 del juego (12)")
        print("- Nivel 12 del juego, DOS MONSTRUOS (13)")
        print("- Nivel 13 del juego (14)")
        print("- Nivel 14 del juego (15)")
        print("-- Otros niveles:")
        print("- Nivel 0 de prueba (16)")
        print("- Nivel 1 de prueba (17)")
        print("- Nivel 2 de prueba (18)")
        print("- Nivel 3 de prueba (19)")
        res = input("Responda con uno de los números indicados entre paréntesis: ")
        print("\n---\n")
        
        try:
            res = int(res)
            self.paredes = []
            
            if(res == 1):
                # NIVEL 0
                self.numMonstruos = 1
                
                self.celdas = np.zeros((6, 7))
                

                for i in range(0,6):
                    self.celdas[i,6] = 3
                
                self.celdas[2,6] = 2
                
                self.paredes.append(Pared(0,0,1,0))
                self.paredes.append(Pared(1,0,1,1))
                self.paredes.append(Pared(2,0,2,1))
                self.paredes.append(Pared(3,0,3,1))
                
                self.personaje = Personaje(4, 2)
                
                self.monstruo = Monstruo(1, 0)
            elif(res == 2):
                # NIVEL 1
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7, 6))

                for i in range(0,6):
                    self.celdas[6,i] = 3
                
                self.celdas[6,3] = 2
                self.celdas[1,1] = 1
                
                self.paredes.append(Pared(0,5,1,5))
                self.paredes.append(Pared(1,4,1,5))
                self.paredes.append(Pared(5,5,5,4))
                self.paredes.append(Pared(0,3,1,3))
                self.paredes.append(Pared(1,1,2,1))
                
                self.personaje = Personaje(1,3)
                
                self.monstruo = Monstruo(1, 5)
            elif(res == 3):
                # NIVEL 2
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7, 6))

                for i in range(0,6):
                    self.celdas[6,i] = 3
                
                self.celdas[6,1] = 2
                self.celdas[1,2] = 1
                
                self.paredes.append(Pared(1,0,2,0))
                self.paredes.append(Pared(4,0,5,0))
                self.paredes.append(Pared(4,1,5,1))
                self.paredes.append(Pared(3,3,4,3))
                self.paredes.append(Pared(4,4,5,4))
                
                self.personaje = Personaje(4, 4)
                
                self.monstruo = Monstruo(5, 5)
            elif(res == 4):
                # NIVEL 3
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7, 6))

                for i in range(0,6):
                    self.celdas[6,i] = 3
                
                self.celdas[6,2] = 2
                self.celdas[4,3] = 1
                self.celdas[3,5] = 1
                
                self.paredes.append(Pared(0,2,1,2))
                self.paredes.append(Pared(0,4,1,4))
                self.paredes.append(Pared(1,3,1,4))
                self.paredes.append(Pared(2,0,2,1))
                self.paredes.append(Pared(2,2,3,2))
                self.paredes.append(Pared(2,3,3,3))
                self.paredes.append(Pared(3,3,4,3))
                self.paredes.append(Pared(5,0,5,1))
                self.paredes.append(Pared(5,1,5,2))
                self.paredes.append(Pared(4,3,5,3))
                self.paredes.append(Pared(5,3,5,4))
                self.paredes.append(Pared(4,4,5,4))
                
                self.personaje = Personaje(5, 5)
                
                self.monstruo = Monstruo(2, 3)
            elif(res == 5):
                # NIVEL 4
                self.numMonstruos = 1
                
                self.celdas = np.zeros((6,7))

                for i in range(0,6):
                    self.celdas[i,6] = 3
                
                self.celdas[3,6] = 2
                self.celdas[4,2] = 1
                
                self.paredes.append(Pared(0,1,0,2))
                self.paredes.append(Pared(0,2,0,3))
                self.paredes.append(Pared(1,1,2,1))
                self.paredes.append(Pared(2,1,2,2))
                self.paredes.append(Pared(1,4,2,4))
                self.paredes.append(Pared(2,4,2,5))
                self.paredes.append(Pared(3,0,4,0))
                self.paredes.append(Pared(4,0,5,0))
                self.paredes.append(Pared(5,3,5,4))
                
                self.personaje = Personaje(4, 0)
                
                self.monstruo = Monstruo(0, 0)
            elif(res == 6):
                # NIVEL 5
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7,6))

                for i in range(0,6):
                    self.celdas[0,i] = 3
                
                self.celdas[0,5] = 2
                self.celdas[2,0] = 1
                
                self.paredes.append(Pared(2,0,3,0))
                self.paredes.append(Pared(2,2,3,2))
                self.paredes.append(Pared(4,1,4,2))
                self.paredes.append(Pared(5,1,5,2))
                self.paredes.append(Pared(5,1,6,1))
                self.paredes.append(Pared(2,4,3,4))
                self.paredes.append(Pared(1,4,1,5))
                self.paredes.append(Pared(4,4,5,4))
                self.paredes.append(Pared(4,5,5,5))
                
                self.personaje = Personaje(1, 1)
                
                self.monstruo = Monstruo(2, 2)
            elif(res == 7):
                # NIVEL 6
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7,6))

                for i in range(0,6):
                    self.celdas[0,i] = 3
                
                self.celdas[0,5] = 2
                self.celdas[6,1] = 1
                self.celdas[5,5] = 1
                
                self.paredes.append(Pared(2,1,3,1))
                self.paredes.append(Pared(3,0,3,1))
                self.paredes.append(Pared(4,0,4,1))
                self.paredes.append(Pared(4,1,5,1))
                self.paredes.append(Pared(5,2,5,3))
                self.paredes.append(Pared(2,4,3,4))
                self.paredes.append(Pared(3,4,3,5))
                self.paredes.append(Pared(3,5,4,5))
                self.paredes.append(Pared(4,5,5,5))
                
                self.personaje = Personaje(5, 3)
                
                self.monstruo = Monstruo(4, 5)
            elif(res == 8):
                # NIVEL 7
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7,6))

                for i in range(0,6):
                    self.celdas[6,i] = 3
                
                self.celdas[6,1] = 2
                self.celdas[1,2] = 1
                self.celdas[0,4] = 1
                
                self.paredes.append(Pared(0,0,1,0))
                self.paredes.append(Pared(0,1,1,1))
                self.paredes.append(Pared(1,0,1,1))
                self.paredes.append(Pared(5,0,5,1))
                self.paredes.append(Pared(4,1,4,2))
                self.paredes.append(Pared(4,2,5,2))
                self.paredes.append(Pared(2,3,3,3))
                self.paredes.append(Pared(1,5,2,5))
                self.paredes.append(Pared(4,4,5,4))
                
                self.personaje = Personaje(3, 5)
                
                self.monstruo = Monstruo(5, 4)
            elif(res == 9):
                # NIVEL 8
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7,6))

                for i in range(0,6):
                    self.celdas[0,i] = 3
                
                self.celdas[0,0] = 2
                self.celdas[2,4] = 1
                self.celdas[5,5] = 1
                
                self.paredes.append(Pared(1,0,1,1))
                self.paredes.append(Pared(2,1,2,2))
                self.paredes.append(Pared(3,2,3,3))
                self.paredes.append(Pared(3,0,3,1))
                self.paredes.append(Pared(3,1,4,1))
                self.paredes.append(Pared(4,1,4,2))
                self.paredes.append(Pared(4,3,5,3))
                self.paredes.append(Pared(5,2,6,2))
                self.paredes.append(Pared(5,3,6,3))
                
                self.personaje = Personaje(6, 3)
                
                self.monstruo = Monstruo(3, 2)
            elif(res == 10):
                # NIVEL 9
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7,6))

                for i in range(0,6):
                    self.celdas[0,i] = 3
                
                self.celdas[0,0] = 2
                self.celdas[5,1] = 1
                
                self.paredes.append(Pared(4,0,5,0))
                self.paredes.append(Pared(4,1,5,1))
                self.paredes.append(Pared(4,1,4,2))
                self.paredes.append(Pared(3,3,3,4))
                self.paredes.append(Pared(4,3,5,3))
                self.paredes.append(Pared(4,4,5,4))
                self.paredes.append(Pared(5,3,6,3))
                self.paredes.append(Pared(6,4,6,5))
                
                self.personaje = Personaje(5, 4)
                
                self.monstruo = Monstruo(4, 1)
            elif(res == 11):
                # NIVEL 10
                self.numMonstruos = 1
                
                self.celdas = np.zeros((6,7))

                for i in range(0,6):
                    self.celdas[i,0] = 3
                
                self.celdas[3,0] = 2
                self.celdas[4,3] = 1
                
                self.paredes.append(Pared(1,1,1,2))
                self.paredes.append(Pared(1,2,2,2))
                self.paredes.append(Pared(2,3,3,3))
                self.paredes.append(Pared(1,4,1,5))
                self.paredes.append(Pared(1,4,2,4))
                self.paredes.append(Pared(0,5,1,5))
                self.paredes.append(Pared(5,2,5,3))
                self.paredes.append(Pared(4,6,5,6))
                
                self.personaje = Personaje(5, 3)
                
                self.monstruo = Monstruo(1, 2)
            elif(res == 12):
                # NIVEL 11
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7,6))

                for i in range(0,6):
                    self.celdas[6,i] = 3
                
                self.celdas[6,3] = 2
                self.celdas[1,5] = 1
                
                self.paredes.append(Pared(0,1,0,2))
                self.paredes.append(Pared(1,1,2,1))
                self.paredes.append(Pared(1,2,2,2))
                self.paredes.append(Pared(1,2,1,3))
                self.paredes.append(Pared(0,3,1,3))
                self.paredes.append(Pared(2,3,3,3))
                self.paredes.append(Pared(3,2,3,3))
                self.paredes.append(Pared(2,4,2,5))
                
                self.personaje = Personaje(2, 2)
                
                self.monstruo = Monstruo(5, 2)
            elif(res == 13):
                # NIVEL 12
                self.numMonstruos = 2
                
                self.celdas = np.zeros((6, 7))
                
                for i in range(0,6):
                    self.celdas[i,0] = 3
                    
                self.celdas[3,0] = 2
                self.celdas[2,4] = 1
                
                self.paredes.append(Pared(0,3,0,4))
                self.paredes.append(Pared(1,2,1,3))
                self.paredes.append(Pared(5,2,5,3))
                self.paredes.append(Pared(1,4,1,5))
                self.paredes.append(Pared(4,4,5,4))
                self.paredes.append(Pared(2,5,3,5))
                self.paredes.append(Pared(0,6,1,6))
                self.paredes.append(Pared(1,5,1,6))
                
                self.personaje = Personaje(1, 3)
                
                self.monstruo1 = Monstruo(1, 1)
                self.monstruo2 = Monstruo(5, 5)
            elif(res == 14):
                # NIVEL 13
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7,6))

                for i in range(0,6):
                    self.celdas[0,i] = 3
                
                self.celdas[0,3] = 2
                self.celdas[5,1] = 1
                
                self.paredes.append(Pared(2,2,3,2))
                self.paredes.append(Pared(5,1,6,1))
                self.paredes.append(Pared(4,2,4,3))
                self.paredes.append(Pared(5,2,5,3))
                self.paredes.append(Pared(1,4,2,4))
                self.paredes.append(Pared(2,4,2,5))
                self.paredes.append(Pared(4,4,5,4))
                
                self.personaje = Personaje(3, 5)
                
                self.monstruo = Monstruo(1, 1)
            elif(res == 15):
                # NIVEL 14
                self.numMonstruos = 1
                
                self.celdas = np.zeros((7, 6))
                
                for i in range(0,6):
                    self.celdas[6,i] = 3

                self.celdas[6,4] = 2
                self.celdas[1,5] = 1
                
                self.paredes.append(Pared(1,1,2,1))
                self.paredes.append(Pared(4,1,5,1))
                self.paredes.append(Pared(3,3,4,3))
                self.paredes.append(Pared(4,3,5,3))
                self.paredes.append(Pared(4,4,5,4))
                self.paredes.append(Pared(4,4,4,5))
                self.paredes.append(Pared(2,4,2,5))
                
                self.personaje = Personaje(4, 1)
                
                self.monstruo = Monstruo(5, 3)
            elif(res == 16):
                # PRUEBA 0
                self.numMonstruos = 1
                
                self.celdas = np.zeros((4, 6))

                self.celdas[1,5] = 2
                self.celdas[1,1] = 1
                
                self.paredes.append(Pared(1,3,1,4))
                self.paredes.append(Pared(2,3,2,4))
                
                self.personaje = Personaje(1, 2)
                
                self.monstruo = Monstruo(1, 0)
            elif(res == 17):
                # PRUEBA 1
                self.numMonstruos = 1
                
                self.celdas = np.zeros((6, 6))

                self.celdas[3,5] = 2
                
                self.paredes.append(Pared(1,1,1,2))
                self.paredes.append(Pared(2,1,2,2))
                self.paredes.append(Pared(3,1,3,2))
                self.paredes.append(Pared(2,3,3,3))
                self.paredes.append(Pared(2,4,3,4))
                self.paredes.append(Pared(2,4,2,5))
                self.paredes.append(Pared(1,4,1,5))
                
                self.personaje = Personaje(2, 4)
                
                self.monstruo = Monstruo(1, 1)
            elif(res == 18):
                # PRUEBA 2
                self.numMonstruos = 1
                
                self.celdas = np.zeros((4, 3))

                self.celdas[2,1] = 2
                
                self.paredes.append(Pared(0,0,0,1))
                self.paredes.append(Pared(0,0,1,0))
                self.paredes.append(Pared(1,1,2,1))
                self.paredes.append(Pared(1,1,1,2))
                
                self.personaje = Personaje(1, 1)
                
                self.monstruo = Monstruo(0, 0)
            elif(res == 19):
                # PRUEBA 3
                self.numMonstruos = 1
                
                self.celdas = np.zeros((50, 6))

                for i in range(0,6):
                    self.celdas[49,i] = 3
                
                self.celdas[49,3] = 2
                self.celdas[1,1] = 1
                
                self.paredes.append(Pared(0,5,1,5))
                self.paredes.append(Pared(1,4,1,5))
                self.paredes.append(Pared(48,5,48,4))
                self.paredes.append(Pared(0,3,1,3))
                self.paredes.append(Pared(1,1,2,1))
                
                self.personaje = Personaje(1,3)
                
                self.monstruo = Monstruo(1, 5)
            else:
                print("Valor incorrecto.\n")
                self.preguntaNivel()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntaNivel()
            
    def representarYVerificar(self):
        print("¿Este es el nivel que deseas cargar?\n")
        if(self.numMonstruos == 1):
            mapa = Mapa(self.celdas, self.paredes, self.monstruo, self.personaje)
        if(self.numMonstruos == 2):
            mapa = Mapa2(self.celdas, self.paredes, self.monstruo1, self.monstruo2, self.personaje)
        print(representation.graphicRepresentation(mapa))
        res = input("Responda SI (1) o NO (2): ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                print("Mapa cargado correctamente.\n")
            elif(res == 2):
                print("Seleccione de nuevo el mapa.\n")
                self.limpiar()
                self.ejecutar()
            else:
                print("Valor incorrecto.\n")
                self.representarYVerificar()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.representarYVerificar()
            
    def preguntarFilas(self):
        print("¿Cuantas filas tiene el mapa?")
        res = input("Responda con un número: ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res >= 3):
                self.filas = res
            else:
                print("Tienen que haber mínimo 3 filas.\n")
                self.preguntarFilas()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarFilas()
    
    def preguntarColumnas(self):
        print("¿Cuantas columnas tiene el mapa?")
        res = input("Responda con un número: ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res >= 3):
                self.columnas = res
            else:
                print("Tienen que haber mínimo 3 columnas.\n")
                self.preguntarColumnas()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarColumnas()
            
    def preguntarFilaColumnaInaccesible(self):
        print("¿Existe una fila o columna inexistente?")
        res = input("Responda con 1 para especificar una fila, 2 para especificar una columna o 3 para continuar: ")
        print("\n---")
        
        try:
            res = int(res)
            
            if(res == 1):
                res = input("Indique la fila inexistente: ")
                print("\n---\n")
                res = int(res)
                if(res < self.filas):
                    for i in range(0,self.columnas):
                        self.celdas[res,i] = 3
                else:
                    print("No existe la fila indicada.\n")
                    self.preguntarFilaColumnaInaccesible()
            elif(res == 2):
                res = input("Indique la columna inexistente: ")
                print("\n---\n")
                res = int(res)
                if(res < self.columnas):
                    for i in range(0,self.filas):
                        self.celdas[i,res] = 3
                else:
                    print("No existe la columna indicada.\n")
                    self.preguntarFilaColumnaInaccesible()
            elif(res == 3):
                print("\nNo existe ninguna fila o columna inexistente.\n")
            else:
                print("\nValor incorrecto.\n")
                self.preguntarFilaColumnaInaccesible()
        except ValueError:
            print("\nEntrada incorrecta.\n")
            self.preguntarFilaColumnaInaccesible()
            
    def preguntarObjetivo(self):
        print("¿Cual es la fila de la celda objetivo?")
        res = input("Responda con un número: ")
        print("\n---")
        
        try:
            res = int(res)
            
            if(res >= 0 and res < self.filas):
                fila = res
                print("\n¿Y la columna?")
                res = input("Responda con un número: ")
                print("\n---\n")
                
                res = int(res)
                
                if(res >= 0 and res < self.columnas):
                    columna = res
                    self.celdas[fila, columna] = 2
                else:
                    print("\nLa celda objetivo no puede estar fuera del mapa.\n")
                    self.preguntarObjetivo()
            else:
                print("\nLa celda objetivo no puede estar fuera del mapa.\n")
                self.preguntarObjetivo()
        except ValueError:
            print("\nEntrada incorrecta.\n")
            self.preguntarObjetivo()
            
    def preguntarPersonaje(self):
        print("¿Cual es la fila del personaje?")
        res = input("Responda con un número: ")
        print("\n---")
        
        try:
            res = int(res)
            
            if(res >= 0 and res < self.filas):
                fila = res
                print("\n¿Y la columna?")
                res = input("Responda con un número: ")
                print("\n---\n")
                
                res = int(res)
                
                if(res >= 0 and res < self.columnas):
                    columna = res
                    
                    if(not self.celdas[fila, columna] == 1 and not self.celdas[fila, columna] == 2 and not self.celdas[fila, columna] == 3):
                        self.personaje = Personaje(fila, columna)
                    else:
                        print("\nEl personaje no puede estar sobre una celda ardiente, sobre una celda inexistente o sobre la celda objetivo.\n")
                        self.preguntarPersonaje()
                else:
                    print("\nEl personaje no puede estar fuera del mapa.\n")
                    self.preguntarPersonaje()
            else:
                print("\nEl personaje no puede estar fuera del mapa.\n")
                self.preguntarPersonaje()
        except ValueError:
            print("\nEntrada incorrecta.\n")
            self.preguntarPersonaje()
            
    def preguntarMonstruo(self):
        print("¿Cual es la fila del monstruo?")
        res = input("Responda con un número: ")
        print("\n---")
        
        try:
            res = int(res)
            
            if(res >= 0 and res < self.filas):
                fila = res
                print("\n¿Y la columna?")
                res = input("Responda con un número: ")
                print("\n---\n")
                
                res = int(res)
                
                if(res >= 0 and res < self.columnas):
                    columna = res
                    
                    if(not self.celdas[fila, columna] == 1 and not self.celdas[fila, columna] == 2 and not self.celdas[fila, columna] == 3 and not (fila == self.personaje.icelda and columna == self.personaje.jcelda)):
                        if(self.numMonstruos == 0):
                            self.monstruo = Monstruo(fila, columna)
                            self.monstruo1 = Monstruo(fila, columna)
                            self.numMonstruos = 1
                        elif(self.numMonstruos == 1):
                            self.monstruo2 = Monstruo(fila, columna)
                            self.numMonstruos = 2
                    else:
                        print("\nEl monstruo no puede estar sobre una celda ardiente, sobre una celda inexistente, sobre la celda objetivo ni en la misma celda que el personaje.\n")
                        self.preguntarMonstruo()
                else:
                    print("\nEl monstruo no puede estar fuera del mapa.\n")
                    self.preguntarMonstruo()
            else:
                print("\nEl monstruo no puede estar fuera del mapa.\n")
                self.preguntarMonstruo()
        except ValueError:
            print("\nEntrada incorrecta.\n")
            self.preguntarMonstruo()
            
    def preguntarAñadirOtroMonstruo(self):
        print("¿Quieres añadir un segundo monstruo?")
        res = input("Responda SI (1) o NO (2): ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                self.preguntarMonstruo()
            elif(res == 2):
                print("No se ha añadido otro monstruo.\n")
            else:
                print("Valor incorrecto.\n")
                self.preguntarAñadirOtroMonstruo()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarAñadirOtroMonstruo()
            
    def preguntarArdiente(self):
        print("¿Quieres añadir una casilla ardiente?")
        res = input("Responda 1 para añadir una o 2 para continuar: ")
        print("\n---")
        
        try:
            res = int(res)
            
            if(res == 1):
                
                print("\n¿Cual es la fila de la casilla ardiente?")
                res = input("Responda con un número: ")
                print("\n---")
                res = int(res)
                
                if(res >= 0 and res < self.filas):
                    fila = res
                    print("\n¿Y la columna?")
                    res = input("Responda con un número: ")
                    print("\n---\n")
                    
                    res = int(res)
                    
                    if(res >= 0 and res < self.columnas):
                        columna = res
                        
                        if(not self.celdas[fila, columna] == 1 and not self.celdas[fila, columna] == 2 and not self.celdas[fila, columna] == 3 and not (fila == self.personaje.icelda and columna == self.personaje.jcelda) and not (fila == self.monstruo.icelda and columna == self.monstruo.jcelda)):
                            self.celdas[fila, columna] = 1
                            print("A continuación podrás añadir otra casilla ardiente.\n")
                            self.preguntarArdiente()
                        else:
                            print("\nLa casilla ardiente no puede estar sobre otra casilla ardiente, sobre una celda inexistente, sobre la celda objetivo ni en la misma celda que el personaje o el monstruo.\n")
                            self.preguntarArdiente()
                    else:
                        print("\nLa casilla ardiente no puede estar fuera del mapa.\n")
                        self.preguntarArdiente()
                else:
                    print("\nLa casilla ardiente no puede estar fuera del mapa.\n")
                    self.preguntarArdiente()
            elif(res == 2):
                print("\nNo se ha añadido la casilla ardiente.\n")
            else:
                print("\nValor incorrecto.\n")
        except ValueError:
            print("\nEntrada incorrecta.\n")
            self.preguntarArdiente()
            
    def preguntarPared(self):
        print("¿Quieres añadir una pared?")
        res = input("Responda 1 para añadir una o 2 para continuar: ")
        print("\n---")
        
        try:
            res = int(res)
            
            if(res == 1):
                
                print("\n¿Cual es la fila de la primera celda que compone la pared?")
                res = input("Responda con un número: ")
                print("\n---")
                res = int(res)
                
                if(res >= 0 and res < self.filas):
                    fila1 = res
                    print("\n¿Y la columna?")
                    res = input("Responda con un número: ")
                    print("\n---")
                    
                    res = int(res)
                    
                    if(res >= 0 and res < self.columnas):
                        columna1 = res
                        
                        print("\n¿Cual es la fila de la segunda celda que compone la pared?")
                        res = input("Responda con un número: ")
                        print("\n---")
                        res = int(res)
                        
                        if(res >= 0 and res < self.filas):
                            fila2 = res
                            print("\n¿Y la columna?")
                            res = input("Responda con un número: ")
                            print("\n---")
                            
                            res = int(res)
                            
                            if(res >= 0 and res < self.columnas):
                                columna2 = res
                                
                                self.paredes.append(Pared(fila1, columna1, fila2, columna2))
                                print("\nA continuación podrás añadir otra pared.\n")
                                self.preguntarPared()
                            else:
                                print("\nLa pared no puede estar fuera del mapa.\n")
                                self.preguntarPared()
                        else:
                            print("\nLa pared no puede estar fuera del mapa.\n")
                            self.preguntarPared()
                    else:
                        print("\nLa pared no puede estar fuera del mapa.\n")
                        self.preguntarPared()
                else:
                    print("\nLa pared no puede estar fuera del mapa.\n")
                    self.preguntarPared()
            elif(res == 2):
                print("\nNo se ha añadido la pared.\n")
            else:
                print("\nValor incorrecto.\n")
                self.preguntarPared()
        except ValueError:
            print("\nEntrada incorrecta.\n")
            self.preguntarPared()
            
    def preguntarTeletransporte(self):
        print("¿Quieres añadir un par de teletransportes?")
        res = input("Responda 1 para añadir una o 2 para continuar: ")
        print("\n---")
        
        try:
            res = int(res)
            
            if(res == 1):
                
                print("\n¿Cual es la fila del primer teletransporte?")
                res = input("Responda con un número: ")
                print("\n---")
                res = int(res)
                
                if(res >= 0 and res < self.filas):
                    fila1 = res
                    print("\n¿Y la columna?")
                    res = input("Responda con un número: ")
                    print("\n---")
                    
                    res = int(res)
                    
                    if(res >= 0 and res < self.columnas):
                        columna1 = res
                        
                        print("\n¿Cual es la fila del segundo teletransporte?")
                        res = input("Responda con un número: ")
                        print("\n---")
                        res = int(res)
                        
                        if(res >= 0 and res < self.filas):
                            fila2 = res
                            print("\n¿Y la columna?")
                            res = input("Responda con un número: ")
                            print("\n---")
                            
                            res = int(res)
                            
                            if(res >= 0 and res < self.columnas):
                                columna2 = res
                                
                                self.celdas[fila1, columna1] = 4
                                self.celdas[fila2, columna2] = 4
                            else:
                                print("\nEl teletransporte no puede estar fuera del mapa.\n")
                                self.preguntarTeletransporte()
                        else:
                            print("\nEl teletransporte no puede estar fuera del mapa.\n")
                            self.preguntarTeletransporte()
                    else:
                        print("\nEl teletransporte no puede estar fuera del mapa.\n")
                        self.preguntarTeletransporte()
                else:
                    print("\nEl teletransporte no puede estar fuera del mapa.\n")
                    self.preguntarTeletransporte()
            elif(res == 2):
                print("\nNo se ha añadido el teletransporte.\n")
            else:
                print("\nValor incorrecto.\n")
                self.preguntarTeletransporte()
        except ValueError:
            print("\nEntrada incorrecta.\n")
            self.preguntarTeletransporte()
            
    def preguntarAlgoritmo(self):
        explicacion = ""
        if(self.numMonstruos == 2):
            explicacion = "usando como heurística la distancia de Manhattan (Personaje - Objetivo) "
        
        print("¿Con qué algoritmo de búsqueda quieres intentar resolver el mapa?")
        print("- Búsqueda en anchura (1)")
        print("- Búsqueda en profundidad (2)")
        print("- Búsqueda con A* {}(3)".format(explicacion))
        res = input("Responda con uno de los números indicados entre paréntesis: ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                self.algoritmo = 1
            elif(res == 2):
                self.algoritmo = 2
            elif(res == 3):
                self.algoritmo = 3
                
                self.preguntarCoste()
                if(self.numMonstruos == 1):
                    self.preguntarHeuristica()
            else:
                print("Valor incorrecto.\n")
                self.preguntarAlgoritmo()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarAlgoritmo()
            
    def preguntarCoste(self):
        print("¿Qué función de coste quieres usar?")
        print("- Coste 0 para cada nodo (1)")
        print("- Coste 1 para cada nodo (2)")
        res = input("Responda con uno de los números indicados entre paréntesis: ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                self.coste = 1
            elif(res == 2):
                self.coste = 2
            else:
                print("Valor incorrecto.\n")
                self.preguntarCoste()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarCoste()
            
    def preguntarHeuristica(self):
        print("¿Qué función de heurística quieres usar?")
        print("- Distancia Manhattan (Personaje - Objetivo) (1)")
        print("- Heurística contemplando diferentes situaciones, con preferencia a la casilla ardiente más cercana al personaje (2)")
        print("- Heurística contemplando diferentes situaciones, con preferencia a la casilla ardiente más lejana al personaje (3)")
        print("- Heurística contemplando diferentes situaciones, con preferencia a una casilla ardiente aleatoria (4)")
        print("- Heurística contemplando diferentes situaciones, con preferencia a una casilla ardiente aleatoria y teniendo en cuenta situaciones en las que el monstruo queda encajado en dos paredes contiguas (5)")
        res = input("Responda con uno de los números indicados entre paréntesis: ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                self.heuristica = 1
            elif(res == 2):
                self.heuristica = 2
            elif(res == 3):
                self.heuristica = 3
            elif(res == 4):
                self.heuristica = 4
            elif(res == 5):
                self.heuristica = 5
            else:
                print("Valor incorrecto.\n")
                self.preguntarHeuristica()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarHeuristica()
            
    def preguntarDetallado(self):
        print("¿Quieres que el algoritmo muestre los nodos que va explorando durante la resolución del mapa a tiempo real?")
        res = input("Responda SÍ (1) o NO (2): ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                self.detallado = True
            elif(res == 2):
                self.detallado = False
            else:
                print("Valor incorrecto.\n")
                self.preguntarDetallado()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarDetallado()
            
    def preguntarEnFichero(self):
        print("¿Quieres que la resolución se escriba en un fichero 'resolucion_wappo.txt' en la carpeta raíz del proyecto (1) o que se muestre por pantalla con menos información (2)?")
        res = input("Responda con uno de los números indicados entre paréntesis: ")
        print("\n---\n")
        
        try:
            res = int(res)
            
            if(res == 1):
                self.enFichero = True
            elif(res == 2):
                self.enFichero = False
            else:
                print("Valor incorrecto.\n")
                self.preguntarEnFichero()
        except ValueError:
            print("Entrada incorrecta.\n")
            self.preguntarEnFichero()