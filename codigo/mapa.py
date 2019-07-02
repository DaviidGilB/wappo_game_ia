import problema_espacio_estados as probee
import copy

class Mapa:
    def __init__(self, celdas, paredes, monstruo, personaje):
        self.celdas = celdas
        self.paredes = paredes
        self.monstruo = monstruo
        self.personaje = personaje
    
    def tamaño_hor(self):
        return len(self.celdas[0])
    
    def tamaño_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, i, j):
        tipo = self.celdas[i][j]
        out = "La casilla es: "
        
        if(tipo==0):
            out+= "Normal"
        if(tipo==1):
            out+= "Ardiente"
        if(tipo==2):
            out+= "La salida"
        if(tipo==3):
            out+= "Incaccesible"
            
        return out
    
    def hay_pared(self, icelda1, jcelda1, icelda2, jcelda2):
        res = False
        
        paredes = self.paredes;
        for i in range(0, len(self.paredes)):
            check1 = paredes[i].icelda1 == icelda1 and paredes[i].jcelda1 == jcelda1 and paredes[i].icelda2 == icelda2 and paredes[i].jcelda2 == jcelda2
            check2 = paredes[i].icelda1 == icelda2 and paredes[i].jcelda1 == jcelda2 and paredes[i].icelda2 == icelda1 and paredes[i].jcelda2 == jcelda1
            if(check1 or check2):
                res = True
                break
        return res
    
    def __str__(self):
        return 'Personaje en fila {} y columna {}, y monstruo en fila {} y columna {}'.format(self.personaje.icelda, self.personaje.jcelda, self.monstruo.icelda, self.monstruo.jcelda)
    
    def __eq__(self, other):
        p = self.personaje.icelda == other.personaje.icelda and self.personaje.jcelda == other.personaje.jcelda
        m = self.monstruo.icelda == other.monstruo.icelda and self.monstruo.jcelda == other.monstruo.jcelda
        s = self.monstruo.stun == other.monstruo.stun
        return p and m and s
    
class Mapa2:
    def __init__(self, celdas, paredes, monstruo1, monstruo2, personaje):
        self.celdas = celdas
        self.paredes = paredes
        self.monstruo1 = monstruo1
        self.monstruo2 = monstruo2
        self.personaje = personaje
    
    def tamaño_hor(self):
        return len(self.celdas[0])
    
    def tamaño_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, i, j):
        tipo = self.celdas[i][j]
        out = "La casilla es: "
        
        if(tipo==0):
            out+= "Normal"
        if(tipo==1):
            out+= "Ardiente"
        if(tipo==2):
            out+= "La salida"
        if(tipo==3):
            out+= "Incaccesible"
            
        return out
    
    def hay_pared(self, icelda1, jcelda1, icelda2, jcelda2):
        res = False
        
        paredes = self.paredes;
        for i in range(0, len(self.paredes)):
            check1 = paredes[i].icelda1 == icelda1 and paredes[i].jcelda1 == jcelda1 and paredes[i].icelda2 == icelda2 and paredes[i].jcelda2 == jcelda2
            check2 = paredes[i].icelda1 == icelda2 and paredes[i].jcelda1 == jcelda2 and paredes[i].icelda2 == icelda1 and paredes[i].jcelda2 == jcelda1
            if(check1 or check2):
                res = True
                break
        return res
    
    def __str__(self):
        return 'Personaje en fila {} y columna {}, primer monstruo en fila {} y columna {} y segundo monstruo en fila {} y columna {}'.format(self.personaje.icelda, self.personaje.jcelda, self.monstruo1.icelda, self.monstruo1.jcelda, self.monstruo2.icelda, self.monstruo2.jcelda)
    
    def __eq__(self, other):
        p = self.personaje.icelda == other.personaje.icelda and self.personaje.jcelda == other.personaje.jcelda
        m1 = self.monstruo1.icelda == other.monstruo1.icelda and self.monstruo1.jcelda == other.monstruo1.jcelda
        s1 = self.monstruo1.stun == other.monstruo1.stun
        mov1 = self.monstruo1.movimiento == other.monstruo1.movimiento
        m2 = self.monstruo2.icelda == other.monstruo2.icelda and self.monstruo2.jcelda == other.monstruo2.jcelda
        s2 = self.monstruo2.stun == other.monstruo2.stun
        mov2 = self.monstruo2.movimiento == other.monstruo2.movimiento
        return p and m1 and s1 and mov1 and m2 and s2 and mov2
    
class Pared:
    def __init__(self, icelda1, jcelda1, icelda2, jcelda2):
        self.icelda1 = icelda1
        self.jcelda1 = jcelda1
        self.icelda2 = icelda2
        self.jcelda2 = jcelda2 
        
class CeldaGenerica:
    def __init__(self, icelda, jcelda):
        self.icelda = icelda
        self.jcelda = jcelda
        
class Monstruo:
    def __init__(self, i, j):
        self.icelda = i
        self.jcelda = j
        self.vivo = True
        self.stun = 0
        self.movimiento = 2
        
    def stuneado(self):
        self.stun = 3
        
class Personaje:
    def __init__(self, i, j):
        self.icelda = i
        self.jcelda = j
        
class MoverPersonaje(probee.Accion):
    def __init__(self, direccion, coste = None):
        nombre = 'Mover: {}'.format(direccion)
        super().__init__(nombre)
        self.direccion = direccion
        self.coste = coste
        
    def es_aplicable(self, estado):
        res = False
        mapa = estado
        celdas = mapa.celdas
        p = mapa.personaje
        m = mapa.monstruo
        
        if(self.direccion=="arriba" and not p.icelda == 0):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda - 1, p.jcelda) and not (celdas[p.icelda-1, p.jcelda]) == 1 and not (celdas[p.icelda-1, p.jcelda]) == 3
        if(self.direccion=="abajo" and not p.icelda == mapa.tamaño_ver()-1):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda + 1, p.jcelda) and not (celdas[p.icelda+1, p.jcelda]) == 1 and not (celdas[p.icelda+1, p.jcelda]) == 3
        if(self.direccion=="derecha" and not p.jcelda == mapa.tamaño_hor()-1):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda, p.jcelda + 1) and not (celdas[p.icelda, p.jcelda+1]) == 1 and not (celdas[p.icelda, p.jcelda+1]) == 3
        if(self.direccion=="izquierda" and not p.jcelda == 0):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda, p.jcelda - 1) and not (celdas[p.icelda, p.jcelda-1]) == 1 and not (celdas[p.icelda, p.jcelda-1]) == 3
        
        # MONSTRUO EN EL PROXIMO MOVIMIENTO
        if(res):
            next_mapa = copy.deepcopy(estado)
            next_monstruo = copy.deepcopy(m)
            next_personaje = copy.deepcopy(p)
            
            i_actual_monstruo = m.icelda
            j_actual_monstruo = m.jcelda
            
            if(self.direccion == "arriba"):
                next_personaje.icelda = p.icelda - 1
            if(self.direccion == "abajo"):
                next_personaje.icelda = p.icelda + 1
            if(self.direccion == "izquierda"):
                next_personaje.jcelda = p.jcelda - 1
            if(self.direccion == "derecha"):
                next_personaje.jcelda = p.jcelda + 1
                
            # TELETRANSPORTE
            if(mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 4):
                for i in range(0,mapa.tamaño_ver()):
                    for j in range(0,mapa.tamaño_hor()):
                        if(mapa.celdas[i, j] == 4 and not (i == next_personaje.icelda and j == next_personaje.jcelda)):
                            if(next_personaje.icelda == next_monstruo.icelda and next_personaje.jcelda == next_monstruo.jcelda):
                                res = False
                            else:
                                next_personaje.icelda = i
                                next_personaje.jcelda = j
                            break
                
        if(res):
            for i in range(0,m.movimiento):
                if(next_monstruo.stun > 0):
                    break
                else:
                    mov_i = next_personaje.icelda - next_monstruo.icelda
                    mov_j = next_personaje.jcelda - next_monstruo.jcelda
                    
                    if(mov_j > 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda, next_monstruo.jcelda + 1) or (mapa.celdas[next_monstruo.icelda, next_monstruo.jcelda + 1]) == 3)):
                        next_monstruo.jcelda = next_monstruo.jcelda + 1
                    else:
                        if(mov_j < 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda, next_monstruo.jcelda - 1) or (mapa.celdas[next_monstruo.icelda, next_monstruo.jcelda - 1]) == 3)):
                            next_monstruo.jcelda = next_monstruo.jcelda - 1
                        else:
                            if(mov_i > 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda + 1, next_monstruo.jcelda) or (mapa.celdas[next_monstruo.icelda + 1, next_monstruo.jcelda]) == 3)):
                                next_monstruo.icelda = next_monstruo.icelda + 1
                            else:
                                if(mov_i < 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda - 1, next_monstruo.jcelda) or (mapa.celdas[next_monstruo.icelda - 1, next_monstruo.jcelda]) == 3)):
                                   next_monstruo.icelda = next_monstruo.icelda - 1
                                   
                    if(mapa.celdas[next_monstruo.icelda, next_monstruo.jcelda] == 1 and not (i_actual_monstruo == next_monstruo.icelda and j_actual_monstruo == next_monstruo.jcelda)):
                        break
                                
            next_mapa.personaje = next_personaje
            next_mapa.monstruo = next_monstruo
            
            if(next_personaje.icelda == next_monstruo.icelda and next_personaje.jcelda == next_monstruo.jcelda and not (mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 2)):
                res = False
        
        return res
    
    def aplicar(self, estado):
        mapa = estado
        next_mapa = copy.deepcopy(estado)
        
        monstruo = mapa.monstruo
        next_monstruo = copy.deepcopy(mapa.monstruo)
        
        personaje = mapa.personaje
        next_personaje = copy.deepcopy(mapa.personaje)
        
        i_actual_monstruo = monstruo.icelda
        j_actual_monstruo = monstruo.jcelda
        
        if(self.direccion == "arriba"):
            next_personaje.icelda = personaje.icelda - 1
        if(self.direccion == "abajo"):
            next_personaje.icelda = personaje.icelda + 1
        if(self.direccion == "izquierda"):
            next_personaje.jcelda = personaje.jcelda - 1
        if(self.direccion == "derecha"):
            next_personaje.jcelda = personaje.jcelda + 1
            
        # TELETRANSPORTE
        if(mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 4):
            for i in range(0,mapa.tamaño_ver()):
                for j in range(0,mapa.tamaño_hor()):
                    if(mapa.celdas[i, j] == 4 and not (i == next_personaje.icelda and j == next_personaje.jcelda)):
                        next_personaje.icelda = i
                        next_personaje.jcelda = j
                        break
            
        if(not (mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 2)):
            for i in range(0,monstruo.movimiento):
                if(next_monstruo.stun > 0):
                    next_monstruo.stun = next_monstruo.stun - 1
                    break
                else:
                    mov_i = next_personaje.icelda - next_monstruo.icelda
                    mov_j = next_personaje.jcelda - next_monstruo.jcelda
                    
                    if(mov_j > 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda, next_monstruo.jcelda + 1) or (mapa.celdas[next_monstruo.icelda, next_monstruo.jcelda + 1]) == 3)):
                        next_monstruo.jcelda = next_monstruo.jcelda + 1
                    else:
                        if(mov_j < 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda, next_monstruo.jcelda - 1) or (mapa.celdas[next_monstruo.icelda, next_monstruo.jcelda - 1]) == 3)):
                            next_monstruo.jcelda = next_monstruo.jcelda - 1
                        else:
                            if(mov_i > 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda + 1, next_monstruo.jcelda) or (mapa.celdas[next_monstruo.icelda + 1, next_monstruo.jcelda]) == 3)):
                                next_monstruo.icelda = next_monstruo.icelda + 1
                            else:
                                if(mov_i < 0 and not (mapa.hay_pared(next_monstruo.icelda, next_monstruo.jcelda, next_monstruo.icelda - 1, next_monstruo.jcelda) or (mapa.celdas[next_monstruo.icelda - 1, next_monstruo.jcelda]) == 3)):
                                   next_monstruo.icelda = next_monstruo.icelda - 1
                                   
                    if(mapa.celdas[next_monstruo.icelda, next_monstruo.jcelda] == 1 and not (i_actual_monstruo == next_monstruo.icelda and j_actual_monstruo == next_monstruo.jcelda)):
                        next_monstruo.stuneado()
                        break
                            
        next_mapa.personaje = next_personaje
        next_mapa.monstruo = next_monstruo
        return next_mapa
    
class MoverPersonaje2(probee.Accion):
    def __init__(self, direccion, coste = None):
        nombre = 'Mover: {}'.format(direccion)
        super().__init__(nombre)
        self.direccion = direccion
        self.coste = coste
        
    def es_aplicable(self, estado):
        res = False
        mapa = estado
        celdas = mapa.celdas
        p = mapa.personaje
        m1 = mapa.monstruo1
        m2 = mapa.monstruo2
        
        if(self.direccion=="arriba" and not p.icelda == 0):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda - 1, p.jcelda) and not (celdas[p.icelda-1, p.jcelda]) == 1 and not (celdas[p.icelda-1, p.jcelda]) == 3
        if(self.direccion=="abajo" and not p.icelda == mapa.tamaño_ver()-1):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda + 1, p.jcelda) and not (celdas[p.icelda+1, p.jcelda]) == 1 and not (celdas[p.icelda+1, p.jcelda]) == 3
        if(self.direccion=="derecha" and not p.jcelda == mapa.tamaño_hor()-1):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda, p.jcelda + 1) and not (celdas[p.icelda, p.jcelda+1]) == 1 and not (celdas[p.icelda, p.jcelda+1]) == 3
        if(self.direccion=="izquierda" and not p.jcelda == 0):
            res = not mapa.hay_pared(p.icelda, p.jcelda, p.icelda, p.jcelda - 1) and not (celdas[p.icelda, p.jcelda-1]) == 1 and not (celdas[p.icelda, p.jcelda-1]) == 3
        
        next_monstruo1 = copy.deepcopy(m1)
        next_monstruo2 = copy.deepcopy(m2)
        next_personaje = copy.deepcopy(p)
        
        if(self.direccion == "arriba"):
            next_personaje.icelda = next_personaje.icelda - 1
        if(self.direccion == "abajo"):
            next_personaje.icelda = next_personaje.icelda + 1
        if(self.direccion == "izquierda"):
            next_personaje.jcelda = next_personaje.jcelda - 1
        if(self.direccion == "derecha"):
            next_personaje.jcelda = next_personaje.jcelda + 1
        
        if(res and not mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 2):
            # TELETRANSPORTE
            if(mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 4):
                for i in range(0,mapa.tamaño_ver()):
                    for j in range(0,mapa.tamaño_hor()):
                        if(mapa.celdas[i, j] == 4 and not (i == next_personaje.icelda and j == next_personaje.jcelda)):
                            if((next_personaje.icelda == next_monstruo1.icelda and next_personaje.jcelda == next_monstruo1.jcelda) or (next_personaje.icelda == next_monstruo2.icelda and next_personaje.jcelda == next_monstruo2.jcelda)):
                                res = False
                            else:
                                next_personaje.icelda = i
                                next_personaje.jcelda = j
                            break           
            
        if(res and not mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 2):
            # MONSTRUO 1 Y 2 EN EL PROXIMO MOVIMIENTO
            i_actual_monstruo1 = m1.icelda
            j_actual_monstruo1 = m1.jcelda
            
            i_actual_monstruo2 = m2.icelda
            j_actual_monstruo2 = m2.jcelda
            
            for i in range(0,next_monstruo1.movimiento):
                if(next_monstruo1.stun == 0 or next_monstruo1.movimiento == 3):
                    mov_i = next_personaje.icelda - next_monstruo1.icelda
                    mov_j = next_personaje.jcelda - next_monstruo1.jcelda
                    
                    if(mov_j > 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda, next_monstruo1.jcelda + 1) or (mapa.celdas[next_monstruo1.icelda, next_monstruo1.jcelda + 1]) == 3)):
                        next_monstruo1.jcelda = next_monstruo1.jcelda + 1
                    else:
                        if(mov_j < 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda, next_monstruo1.jcelda - 1) or (mapa.celdas[next_monstruo1.icelda, next_monstruo1.jcelda - 1]) == 3)):
                            next_monstruo1.jcelda = next_monstruo1.jcelda - 1
                        else:
                            if(mov_i > 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda + 1, next_monstruo1.jcelda) or (mapa.celdas[next_monstruo1.icelda + 1, next_monstruo1.jcelda]) == 3)):
                                next_monstruo1.icelda = next_monstruo1.icelda + 1
                            else:
                                if(mov_i < 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda - 1, next_monstruo1.jcelda) or (mapa.celdas[next_monstruo1.icelda - 1, next_monstruo1.jcelda]) == 3)):
                                   next_monstruo1.icelda = next_monstruo1.icelda - 1
                                   
                    if(mapa.celdas[next_monstruo1.icelda, next_monstruo1.jcelda] == 1 and not (i_actual_monstruo1 == next_monstruo1.icelda and j_actual_monstruo1 == next_monstruo1.jcelda) and not next_monstruo1.movimiento == 3):
                        next_monstruo1.stuneado()
                
                if(next_monstruo2.stun == 0 or next_monstruo2.movimiento == 3):
                    mov_i = next_personaje.icelda - next_monstruo2.icelda
                    mov_j = next_personaje.jcelda - next_monstruo2.jcelda
                    
                    if(mov_j > 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda, next_monstruo2.jcelda + 1) or (mapa.celdas[next_monstruo2.icelda, next_monstruo2.jcelda + 1]) == 3)):
                        next_monstruo2.jcelda = next_monstruo2.jcelda + 1
                    else:
                        if(mov_j < 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda, next_monstruo2.jcelda - 1) or (mapa.celdas[next_monstruo2.icelda, next_monstruo2.jcelda - 1]) == 3)):
                            next_monstruo2.jcelda = next_monstruo2.jcelda - 1
                        else:
                            if(mov_i > 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda + 1, next_monstruo2.jcelda) or (mapa.celdas[next_monstruo2.icelda + 1, next_monstruo2.jcelda]) == 3)):
                                next_monstruo2.icelda = next_monstruo2.icelda + 1
                            else:
                                if(mov_i < 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda - 1, next_monstruo2.jcelda) or (mapa.celdas[next_monstruo2.icelda - 1, next_monstruo2.jcelda]) == 3)):
                                   next_monstruo2.icelda = next_monstruo2.icelda - 1
                                   
                    if(mapa.celdas[next_monstruo2.icelda, next_monstruo2.jcelda] == 1 and not (i_actual_monstruo2 == next_monstruo2.icelda and j_actual_monstruo2 == next_monstruo2.jcelda) and not next_monstruo2.movimiento == 3):
                        next_monstruo2.stuneado()
                            
                if(next_monstruo1.icelda == next_monstruo2.icelda and next_monstruo1.jcelda == next_monstruo2.jcelda and not next_monstruo1.movimiento == 3 and not next_monstruo2.movimiento == 3):
                    break
            
            personajePilladoPor1 = next_monstruo1.icelda == next_personaje.icelda and next_monstruo1.jcelda == next_personaje.jcelda
            personajePilladoPor2 = next_monstruo2.icelda == next_personaje.icelda and next_monstruo2.jcelda == next_personaje.jcelda
            
            if(personajePilladoPor1 or personajePilladoPor2):
                res = False
        
        return res
    
    def aplicar(self, estado):
        mapa = estado
        next_mapa = copy.deepcopy(estado)
        
        monstruo1 = mapa.monstruo1
        next_monstruo1 = copy.deepcopy(mapa.monstruo1)
        
        monstruo2 = mapa.monstruo2
        next_monstruo2 = copy.deepcopy(mapa.monstruo2)
        
        personaje = mapa.personaje
        next_personaje = copy.deepcopy(mapa.personaje)
        
        if(self.direccion == "arriba"):
            next_personaje.icelda = personaje.icelda - 1
        if(self.direccion == "abajo"):
            next_personaje.icelda = personaje.icelda + 1
        if(self.direccion == "izquierda"):
            next_personaje.jcelda = personaje.jcelda - 1
        if(self.direccion == "derecha"):
            next_personaje.jcelda = personaje.jcelda + 1
            
        # TELETRANSPORTE
        if(mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 4):
            for i in range(0,mapa.tamaño_ver()):
                for j in range(0,mapa.tamaño_hor()):
                    if(mapa.celdas[i, j] == 4 and not (i == next_personaje.icelda and j == next_personaje.jcelda)):
                        next_personaje.icelda = i
                        next_personaje.jcelda = j
                        break
            
        if(not (mapa.celdas[next_personaje.icelda, next_personaje.jcelda] == 2)):
            # MONSTRUO 1 Y 2 EN EL PROXIMO MOVIMIENTO
            i_actual_monstruo1 = monstruo1.icelda
            j_actual_monstruo1 = monstruo1.jcelda
            
            i_actual_monstruo2 = monstruo2.icelda
            j_actual_monstruo2 = monstruo2.jcelda
            
            stuneadoAlInicio1 = monstruo1.stun > 0
            stuneadoAlInicio2 = monstruo2.stun > 0
            
            for i in range(0,monstruo1.movimiento):
                if(next_monstruo1.stun > 0 and not next_monstruo1.movimiento == 3):
                    if(i == monstruo1.movimiento - 1 and stuneadoAlInicio1):
                        next_monstruo1.stun = next_monstruo1.stun - 1
                else:
                    mov_i = next_personaje.icelda - next_monstruo1.icelda
                    mov_j = next_personaje.jcelda - next_monstruo1.jcelda
                    
                    if(mov_j > 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda, next_monstruo1.jcelda + 1) or (mapa.celdas[next_monstruo1.icelda, next_monstruo1.jcelda + 1]) == 3)):
                        next_monstruo1.jcelda = next_monstruo1.jcelda + 1
                    else:
                        if(mov_j < 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda, next_monstruo1.jcelda - 1) or (mapa.celdas[next_monstruo1.icelda, next_monstruo1.jcelda - 1]) == 3)):
                            next_monstruo1.jcelda = next_monstruo1.jcelda - 1
                        else:
                            if(mov_i > 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda + 1, next_monstruo1.jcelda) or (mapa.celdas[next_monstruo1.icelda + 1, next_monstruo1.jcelda]) == 3)):
                                next_monstruo1.icelda = next_monstruo1.icelda + 1
                            else:
                                if(mov_i < 0 and not (mapa.hay_pared(next_monstruo1.icelda, next_monstruo1.jcelda, next_monstruo1.icelda - 1, next_monstruo1.jcelda) or (mapa.celdas[next_monstruo1.icelda - 1, next_monstruo1.jcelda]) == 3)):
                                   next_monstruo1.icelda = next_monstruo1.icelda - 1
                                   
                    if(mapa.celdas[next_monstruo1.icelda, next_monstruo1.jcelda] == 1 and not (i_actual_monstruo1 == next_monstruo1.icelda and j_actual_monstruo1 == next_monstruo1.jcelda) and not next_monstruo1.movimiento == 3):
                        next_monstruo1.stuneado()
                
                if(next_monstruo2.stun > 0 and not next_monstruo2.movimiento == 3):
                    if(i == monstruo1.movimiento - 1 and stuneadoAlInicio2):
                        next_monstruo2.stun = next_monstruo2.stun - 1
                else:
                    mov_i = next_personaje.icelda - next_monstruo2.icelda
                    mov_j = next_personaje.jcelda - next_monstruo2.jcelda
                    
                    if(mov_j > 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda, next_monstruo2.jcelda + 1) or (mapa.celdas[next_monstruo2.icelda, next_monstruo2.jcelda + 1]) == 3)):
                        next_monstruo2.jcelda = next_monstruo2.jcelda + 1
                    else:
                        if(mov_j < 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda, next_monstruo2.jcelda - 1) or (mapa.celdas[next_monstruo2.icelda, next_monstruo2.jcelda - 1]) == 3)):
                            next_monstruo2.jcelda = next_monstruo2.jcelda - 1
                        else:
                            if(mov_i > 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda + 1, next_monstruo2.jcelda) or (mapa.celdas[next_monstruo2.icelda + 1, next_monstruo2.jcelda]) == 3)):
                                next_monstruo2.icelda = next_monstruo2.icelda + 1
                            else:
                                if(mov_i < 0 and not (mapa.hay_pared(next_monstruo2.icelda, next_monstruo2.jcelda, next_monstruo2.icelda - 1, next_monstruo2.jcelda) or (mapa.celdas[next_monstruo2.icelda - 1, next_monstruo2.jcelda]) == 3)):
                                   next_monstruo2.icelda = next_monstruo2.icelda - 1
                                   
                    if(mapa.celdas[next_monstruo2.icelda, next_monstruo2.jcelda] == 1 and not (i_actual_monstruo2 == next_monstruo2.icelda and j_actual_monstruo2 == next_monstruo2.jcelda) and not next_monstruo2.movimiento == 3):
                        next_monstruo2.stuneado()
                            
                if(next_monstruo1.icelda == next_monstruo2.icelda and next_monstruo1.jcelda == next_monstruo2.jcelda and not next_monstruo1.movimiento == 3 and not next_monstruo2.movimiento == 3):
                    next_monstruo1.movimiento = 3
                    next_monstruo1.stun = 0
                    next_monstruo2.movimiento = 3
                    next_monstruo2.stun = 0
                    break
                            
        next_mapa.personaje = next_personaje
        next_mapa.monstruo1 = next_monstruo1
        next_mapa.monstruo2 = next_monstruo2
        
        return next_mapa