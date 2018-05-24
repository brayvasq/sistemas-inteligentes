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

def values_of_bin(x):
    matrix = []
    for i in range(num_particulas):
        matrix.append([])
        for j in range(dimesiones):
            matrix[i].append(int(x[i][j],2))
    return matrix

x = init_matrix()
xp = copiar(x)
f = init_fitness(x)
print_matrix(x,"X:")
fapt = [0 for i in range(num_particulas)]
iteraciones = 0
while iteraciones < max_num_iteraciones:
    iteraciones += 1

    prom = fitness(x)
    for i in range(num_particulas):
        fapt[i] = f[i] / prom
    
    print(fapt)
    iterador = 0
    val = 0
    directo = []
    for i in range(num_particulas):
        if(fapt[i] > 1):
            it = math.floor(fapt[i])
            xp[iterador] = x[i]
            iterador += 1
            directo.append(xp[iterador])
        else:
            val += math.modf(fapt[i])[0]
    
    print(" VAL : ",val)

    num_disp = num_particulas-iterador
    print(directo)
    ## Ruleta
    for k in range(num_disp):
        for i in range(num_particulas): 
            rand = random.randrange(0,math.floor(val)*10)/10
            #print(rand)
            if fapt[i] > rand:
                if(not x[i] in directo):
                    xp[iterador] = x[i]
                    iterador += 1
                    break

    ## Combinacion
    print(random.shuffle(xp))
    for i in range(num_particulas):
        rps = random.randrange(0,num_particulas)
        #print(rps)
        val = xp[rps]
        aux = xp[i]
        xp[rps] = aux
        xp[i] = val


    for i in range(0,num_particulas,2):
        pr = random.randrange(0,10)/10
        if pr > 0.6:
            print("helos")
            rand = random.randrange(0,8)
            print(rand)
            for j in range(dimesiones):
                #print("tamaño",len(x[i][j]))
                #print(x[i][j])
                val1 = x[i][j][0:rand]
                val2 = x[i][j][rand:8]
                valf = val1+val2
                print(valf)
                x[i][j] = valf
                x[i+1][j] = valf
        
    # Mutación
    pmut = 0.0001
    for i in range(num_particulas):
        for j in range(dimesiones):
            ran = random.randrange(0,1000)/1000
            if ran < pmut:
                randp = random.randrange(0,8)
                if x[i][j][randp] == "1":
                    x[i][j][randp] == "0"
                elif x[i][j][randp] == "0":
                    x[i][j][randp] == "1"


print_matrix(xp," XP : ")
xpv = values_of_bin(xp)
print_matrix(xpv," XPV : ")


