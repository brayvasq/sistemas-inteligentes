import random
import sys
import math

num_particulas = 6
dimensiones = 2
max_num_iteraciones = 10000
probabilida_comb = 0.6
prob_mut = 0.0001

def funcion(x):
    #                 x -            y + 7
    #return positions[0] - positions[1] + 7
    d = len(x)
    suma = 0
    for i in range(d):
        suma += x[i] * math.sin(math.sqrt(abs(x[i])))
    return 418.9829 * d - suma

get_bin = lambda x, n: format(x, 'b').zfill(n)

def get_binary():
    num = random.randrange(0,1024)
    #num = 420
    #print(num)
    numbin = get_bin(num,10);
    cad = numbin
    return cad

def toBinary(n):
    #cad = ''.join(str(1 & int(n) >> i) for i in range(9)[::-1])
    return cad
    

def toNum(n):
    val = int(n,2) - 512
    if val > 500:
        val = 500
    elif val < -500:
        val = -500
    return val

def fitness_array(x):
    valor = 0
    for i in x:
        #print(i.posx)
        valor += i.fitness
    valor = valor/num_particulas
    return valor

def print_matrix(matrix):
    print("-> START")
    for i in matrix:
        if i != None:
            print("POSX : ",i.posx," POS Y : ",i.posy,"VAL X : ",i.valx," VAL Y : ",i.valy," FITNESS : ",i.fitness," FACT : ",i.factibilidad)
    print("-> END")

class Cromosoma:
    def __init__(self,dimensiones):
        self.posx = get_binary()
        self.posy = get_binary()
        #print(self.posx)
        #print(self.posy)
        self.valx = toNum(self.posx) 
        self.valy = toNum(self.posy) 
        #print(self.valx)
        #print(self.valy)
        
        self.fitness = funcion([self.valx,self.valy])
        self.factibilidad = 0
        #print(self.fitness)
    def update(self,val_x,val_y):
        self.posx = val_x
        self.posy = val_x
        self.valx = toNum(val_x)
        self.valy = toNum(val_y)
        self.fitness = funcion([self.valx,self.valy])

def conve(x):
    val = 0
    for i in x:
        #print("Factibi  : ",i.factibilidad)
        if i.fitness < 1:
            val+=1
    #print("Val percent ,", val)
    perc = ((val*100)/num_particulas)
    print("Porcemtaje : ",perc)
    return (perc >= 90)

    

x = Cromosoma(dimensiones)
swarm = [Cromosoma(dimensiones) for __x in range(num_particulas)]
swarm_better = []#[None for __x in range(num_particulas)]
#conve(swarm)
fapt = [0 for i in range(num_particulas)]

iteraciones = 0
converge = False
#print_matrix(swarm)
#print(funcion([-356, -356]))
while not converge:
    iteraciones += 1
    prom = fitness_array(swarm)
    
    #print(prom)

    ################ SELECCIÓN #######################

    # Factibilidad: indica la probabilidad de pasar a la siguiente etapa.
    # También para identificar el numero de copias directas.
    for i in swarm:
        print("FITNESS : ",i.fitness)
        print("PROM : ",prom)
        i.factibilidad = abs(i.fitness) / prom
        print("FACTIBILIDAD : ",i.factibilidad)
    print("-----------------------MATRIX X----------------------")
    print_matrix(swarm)
    # Pasar directamente en los que la factibilidad es mayor o igual a 1
    iterador = 0 #para indicar el numero de plazas disponibles
    pos_ruleta = 0 # indica las posiciones de la ruleta
    swarm_better = []
    for i in swarm:
        if i.factibilidad > 1:
            num_directas = math.floor(i.factibilidad)
            for j in range(num_directas):
                #print("-------------->",j)
                swarm_better.append(Cromosoma(dimensiones))
                swarm_better[iterador].posx = i.posx
                swarm_better[iterador].posy = i.posy
                swarm_better[iterador].valx = i.valx
                swarm_better[iterador].valy = i.valy
                swarm_better[iterador].fitness = i.fitness
                swarm_better[iterador].factibilidad = i.factibilidad
                iterador += 1
        pos_ruleta += math.floor(math.modf(i.factibilidad)[0] * 10)

    #print("####----------------------------->",pos_ruleta)
    #print_matrix(swarm)
    #print_matrix(swarm_better)

    # Ruleta: para identificar 
    #print(")))))))))))))))))))))))))))))))))))))))))))))) iteraciones ",iteraciones)
    num_disp = num_particulas - iterador
    #print(")))))))))))))))))))))))))))))))))))))))))))))) ",num_disp)
    vector = []
    for i in swarm:
        fact = math.floor(math.modf(i.factibilidad)[0] * 10)
        #print("============================================  ",fact)
        for j in range(fact):
            vector.append(i)

    for i in range(num_disp):
        if pos_ruleta>0:
            ramd = math.floor(random.randrange(0,math.floor(pos_ruleta)))
            swarm_better.append(vector[ramd])

    ##################### COMBINACIÓN #######################
    random.shuffle(swarm_better)

    for i in range(0,num_particulas,2):
        #print("Iterando en  I : ",i)
        pr = random.randrange(0,10)/10
        #print("Probabilidad : ",pr)
        if pr >= probabilida_comb:
            if len(swarm_better) == num_particulas:
                #print("Longitud arr : ",len(swarm_better[i].posx))
                rand = random.randrange(0,8)
                val_x = swarm_better[i].posx[0:rand] + swarm_better[i+1].posx[rand:]
                #print(val_x)
                val_y = swarm_better[i].posy[0:rand] + swarm_better[i+1].posy[rand:]
                #print(val_y)
                crom = Cromosoma(dimensiones)
                crom.update(val_x,val_y)

                swarm_better[i] = crom
                swarm_better[i+1] = crom

                #print("Longitud new arr : ",len(val_x)) 

    ##################### MUTACION ###########################
    for i in swarm_better:
        ran = random.randrange(0,10)/10000
        #print("Valor rand : ",ran)
        if ran <= prob_mut:
            #print("Mutando")
            pos = random.randrange(0,10)
            #print("Pos Mut : ",pos)
            val_x = list(i.posx)
            val_x[pos] = '1' if val_x[pos] == '0' else '0'
            i.posx = "".join(val_x)
            val_y = list(i.posy)
            val_y[pos] = '1' if val_y[pos] == '0' else '0'
            i.posy = "".join(val_y)
            #i.posx = i.posx[0:pos-2]+"1"+i.posx[pos:] if i.posx[pos] == "0" else i.posx[0:pos-2]+"0"+i.posx[pos:]
            #i.posy = i.posy[0:pos-2]+"1"+i.posy[pos:] if i.posy[pos] == "0" else i.posy[0:pos-2]+"0"+i.posy[pos:]
             
            #print("POS X LEN : ",len(i.posx))
            #print("POS Y LEN : ",len(i.posy))
            
    swarm = swarm_better
    #swarm_better = []
    #print(swarm_better)
    #print("-----------------------MATRIX XP----------------------")
    #print_matrix(swarm)
    #print_matrix(swarm_better)
    converge = conve(swarm)
    #print("LEN ",len(swarm))
    if len(swarm) == 0:
        converge = True
    if iteraciones == 10:
        converge = True

print_matrix(swarm)




    



