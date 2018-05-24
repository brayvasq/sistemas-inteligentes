import math,random

num_particulas = 6
dimesiones = 2
max_num_iteraciones = 10000

def funcion(x):
    #                 x -            y + 7
    #return positions[0] - positions[1] + 7
    d = len(x)
    suma = 0
    for i in range(d):
        suma += x[i] * math.sin(math.sqrt(abs(x[i])))
    return 418.9829 * d - suma

def num_to_bin(num):
    return bin(num)

def print_matrix(matrix,name):
    print("\n",name)
    for i in matrix:
        print(i)

def init_matrix():
    matrix = []
    for i in range(num_particulas):
        matrix.append([])
        for j in range(dimesiones):
            num = random.randrange(-500,500)
            cad =  "{:09b}".format(num) #num_to_bin(num)
            matrix[i].append(cad)
    return matrix

def copiar(matrix):
    copia = []
    for fila in matrix:
        aux = fila.copy()
        copia.append(aux)
    return copia

def fitness(x):
    valor = 0
    for i in range(num_particulas):
        vector = []
        for j in range(dimesiones):
            vector.append(int(x[i][j],2))

        valor += funcion(vector)
    valor = valor/num_particulas
    return valor

def init_fitness(x):
    f = []
    for i in range(num_particulas):
        v = []
        for j in range(dimesiones):
            v.append(int(x[i][j],2))

        fit = funcion(v)
        f.append(fit)
    return f

x = init_matrix()
xp = copiar(x)
f = init_fitness(x)
print_matrix(x,"X:")
fapt = [0 for i in range(num_particulas)]
iteraciones = 0
while iteraciones < 10:
    iteraciones += 1

    prom = fitness(x)
    for i in range(num_particulas):
        fapt[i] = f[i] / prom
    
    print(fapt)
    iterador = 0
    for i in range(num_particulas):
        if(fapt[i] > 1):
            it = math.floor(fapt[i])
            xp[iterador] = x[i]
            iterador += 1
    
    #for i in range(num_particulas-iterador):


    print_matrix(xp," XP : ")

