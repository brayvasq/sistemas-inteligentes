import random

def funcion(x,y):
    #return (x**4) - 14 * (x**3) + 60 * (x**2) - 70 * x 
    return (3 * ((x**2) + (y**2))) + (4*x*y) + (5*x) + (6*y) + 7

def hill_climbing(axo,bxo,ayo,byo,tasa,max_iter=1000):
    x = random.randint(axo,bxo)
    y = random.randint(ayo,byo)

    item = 0
    for i in range(max_iter):

        if item==0:
            xnuevo = x + tasa * random.gauss(0,1)
            if funcion(x,y) > funcion(xnuevo,y):
                x = xnuevo
            item = 1
        else:
            ynuevo = y + tasa * random.gauss(0,1)
            if(funcion(x,y) > funcion(x,ynuevo)):
                y = ynuevo
            item = 0

    print("X : ",x," Y : ",y," EVAL : ",funcion(x,y))

    #print(x)
    return funcion(x,y)
    
#hill_climbing(-2,2,-2,2,0.1)
def run():
    local = 0
    global_v = 0 
    for i in range(0,1000):
        x = hill_climbing(-2,2,-2,2,0.1)
        if(round(x,2) == 3.85):
            local+=1
        elif(round(x,2) != 3.85):
            global_v += 1

    print(local)
    print(global_v)

run()