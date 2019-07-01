class representation:
    def graphicRepresentation(mapa):
        paredes = mapa.paredes
        matrix = mapa.celdas
        c1 = '.-----.'
        c2 = '|     |'
        c3 = '|     |'
        c4 = '.-----.'
        
        Casillas = ''
        for i in range(0, len(matrix)):
            c1s = ''
            c2s = ''
            c3s = ''
            c4s = ''
            for j in range(0, len(matrix[0])):
                if(mapa.celdas[i][j]==1):
                    c1 = '.-----.'
                    c2 = '|A   A|'
                    c3 = '|A   A|'
                    c4 = '.-----.'
                if(mapa.celdas[i][j]==2):
                    c1 = '.-----.'
                    c2 = '|O O O|'
                    c3 = '|O O O|'
                    c4 = '.-----.'
                if(mapa.celdas[i][j]==3):
                    c1 = '#######'
                    c2 = '#######'
                    c3 = '#######'
                    c4 = '#######'
                if(mapa.celdas[i][j]==4):
                    c1 = '.-----.'
                    c2 = '|T   T|'
                    c3 = '|T   T|'
                    c4 = '.-----.'
                if(mapa.celdas[i][j]==5):
                    c1 = '.-----.'
                    c2 = '|F   F|'
                    c3 = '|F   F|'
                    c4 = '.-----.'
                if(mapa.personaje.icelda==i and mapa.personaje.jcelda==j):
                    c1 = '.-----.'
                    c2 = '|P   P|'
                    c3 = '|P   P|'
                    c4 = '.-----.'
                if hasattr(mapa, 'monstruo'):
                    if(mapa.monstruo.icelda==i and mapa.monstruo.jcelda==j):
                        c1 = '.-----.'
                        c2 = '|M   M|'
                        c3 = '|M   M|'
                        c4 = '.-----.'
                else:
                    if((mapa.monstruo1.icelda==i and mapa.monstruo1.jcelda==j) or (mapa.monstruo2.icelda==i and mapa.monstruo2.jcelda==j)):
                        c1 = '.-----.'
                        c2 = '|M   M|'
                        c3 = '|M   M|'
                        c4 = '.-----.'
                for k in range(0, len(paredes)):
                    if((paredes[k].icelda1==i and paredes[k].jcelda1==j)):
                        if(paredes[k].jcelda2==j-1):
                            c4 = c4.replace('.','#', 1)
                            c1= c1.replace('.','#', 1)
                            c2 = c2.replace('|','#', 1)
                            c3 = c3.replace('|','#', 1)
                        if(paredes[k].jcelda2==j+1):
                            c2 = c2.replace('|','#', 1)
                            c3 = c3.replace('|','#', 1)
                            c4 = c4.replace('.','#', 1)
                            c1= c1.replace('.','#', 1)
                            c2 = representation.reverse(c2)
                            c3 = representation.reverse(c3)
                            c1 = representation.reverse(c1)
                            c4 = representation.reverse(c4)
                        if(paredes[k].icelda2==i-1):
                            c1 = c1.replace('-','#')
                            c1 = c1.replace('.','#')
                        if(paredes[k].icelda2==i+1):
                            c4 = c4.replace('-','#')
                            c4 = c4.replace('.','#')
                    elif((paredes[k].icelda2==i and paredes[k].jcelda2==j)):
                        if(paredes[k].jcelda1==j-1):
                            c2 = c2.replace('|','#', 1)
                            c3 = c3.replace('|','#', 1)
                            c4 = c4.replace('.','#', 1)
                            c1= c1.replace('.','#', 1)
                        if(paredes[k].jcelda1==j+1):
                            c2 = c2.replace('|','#', 1)
                            c3 = c3.replace('|','#', 1)
                            c4 = c4.replace('.','#', 1)
                            c1= c1.replace('.','#', 1)
                            c2 = representation.reverse(c2)
                            c3 = representation.reverse(c3)
                            c1 = representation.reverse(c1)
                            c4 = representation.reverse(c4)
                        if(paredes[k].icelda1==i-1):
                            c1 = c1.replace('-','#')
                            c1 = c1.replace('.','#')
                        if(paredes[k].icelda1==i+1):
                            c4 = c4.replace('-','#')
                            c4 = c4.replace('.','#')
                c1s += c1
                c2s += c2
                c3s += c3
                c4s += c4 
                c1 = '.-----.'
                c2 = '|     |'
                c3 = '|     |'
                c4 = '.-----.'
            Casillas += c1s + '\n' + c2s+ '\n'  + c3s + '\n'  + c4s + '\n'
            
        return Casillas
        
    def reverse(s): 
      str = "" 
      for i in s: 
        str = i + str
      return str