### Sección Nodo ###

class Nodo:
    def __init__(self):
        self.utilidad = 0
        self.estado = [
            ['-','-','-'],
            ['-','-','-'],
            ['-','-','-']
        ]

    def llena(self):
        llena = True
        for i in range(0,3):
            if(nodo.estado[i].__contains__('-')):
                llena = False
        return llena

    def gano(self):
        return self.ver_horizontal() or self.ver_vertical() or self.ver_diagonal()

    def ver_horizontal(self):
        fila_1 = (self.estado[0][0] != '-') and (self.estado[0][1] != '-') and (self.estado[0][2] != '-')
        if(fila_1):
            fila_1 = self.estado[0][0] == self.estado[0][1] ==  self.estado[0][2]
        
        fila_2 = (self.estado[1][0] != '-') and (self.estado[1][1] != '-') and (self.estado[1][2] != '-')
        if(fila_2):
            fila_2 = self.estado[1][0] == self.estado[1][1] ==  self.estado[1][2]
        
        fila_3 = (self.estado[2][0] != '-') and (self.estado[2][1] != '-') and (self.estado[2][2] != '-')
        if(fila_3):
            fila_3 = self.estado[2][0] == self.estado[2][1] ==  self.estado[2][2]

        return fila_1 or fila_2 or fila_3

    def ver_vertical(self):
        col_1 = (self.estado[0][0] != '-') and (self.estado[1][0] != '-') and (self.estado[2][0] != '-')
        if(col_1):
            col_1 = self.estado[0][0] == self.estado[1][0] == self.estado[2][0]
        
        col_2 = (self.estado[0][1] != '-') and (self.estado[1][1] != '-') and (self.estado[2][1] != '-')
        if(col_2):
            col_2 = self.estado[0][1] == self.estado[1][1] == self.estado[2][1]

        col_3 = (self.estado[0][2] != '-') and (self.estado[1][2] != '-') and (self.estado[2][2] != '-')
        if(col_3):
            col_3 = self.estado[0][2] == self.estado[1][2] == self.estado[2][2]

        return col_1 or col_2 or col_3

    def ver_diagonal(self):
        diag_1 = (self.estado[0][0] != '-') and (self.estado[1][1] != '-') and (self.estado[2][2] != '-')
        if(diag_1):
            diag_1 = self.estado[0][0] == self.estado[1][1] == self.estado[2][2]
        
        diag_2 = (self.estado[0][2] != '-') and (self.estado[1][1] != '-') and (self.estado[2][0] != '-')
        if(diag_2):
            diag_2 = self.estado[0][2] == self.estado[1][1] == self.estado[2][0]

        return diag_1 or diag_2

### Fin sección nodo ###

def copiar(matrix):
    copia = []
    for fila in matrix:
        aux = fila.copy()
        copia.append(aux)
    return copia



def generar(nodo,val):
    lista_estados = []
    if not nodo.gano():
        if nodo.llena():
            nodito.utilidad = 0
        else:
            for i in range(0,3):
                for j in range(0,3):
                    estado = copiar(nodo.estado)
                    nuevo = Nodo()
                    nuevo.estado = estado
                    if nuevo.estado[i][j] == '-':
                        nuevo.estado[i][j] = val
                        lista_estados.append(nuevo)
    else:
        if val == 'o':
            nodo.utilidad = -1
        elif val == 'x':
            nodo.utilidad = 1
    return lista_estados

def es_hoja(nodito,val):
    if(nodito != None):
        hijos = generar(nodito,val)
        return len(hijos) == 0
    return False

def maximo(lista_nodos):
    max = -1
    for i in lista_nodos:
        if i.utilidad > max:
            max = i.utilidad
    return max

def minimo(lista_nodos):
    min = 1
    for i in lista_nodos:
        if i.utilidad > min:
            min = i.utilidad
    return min

def print_matrix(nodo):
    estados = nodo.estado
    print('-------------------------')
    for i in estados:
        print(i)
    print('-------------------------')    
    #print(nodo.estado)

pasos = 0
def min_max(nodito,val='x',turno='x'):
    global pasos
    pasos += 1 
    print("Paso : ",pasos)
    print_matrix(nodito)
    if es_hoja(nodito,turno):
        return nodito.utilidad
    else:
        if turno == val:
            hijos = generar(nodito,turno)
            for i in hijos:
                nodito.utilidad = min_max(i,val='x',turno='o')
            return maximo(hijos)
        else:
            hijos = generar(nodito,turno)
            for i in hijos:
                nodito.utilidad = min_max(i,val='x',turno='x')
            return nodito.utilidad

nodo = Nodo()
nodo.estado = [
        ['x','o','x'],
        ['-','-','-'],
        ['-','-','-']
    ]

valor = min_max(nodo,val='x',turno='x')
print(valor)
