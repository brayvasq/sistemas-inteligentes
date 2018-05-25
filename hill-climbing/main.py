import random
import time

def funcion(x,y):
    #return (x**4) - 14 * (x**3) + 60 * (x**2) - 70 * x 
    #return (3 * ((x**2) + (y**2))) + (4*x*y) + (5*x) + (6*y) + 7
	#return (1.5-x +(x*y))*(1.5-x +(x*y)) + (2.25-x+(x*y))*(2.25-x+(x*y)) + (2.625-x+(x*y))*(2.625-x+(x*y))    
    return (1.5 - x + (x*y))**2 + (2.25-x + (x*(y**2)))**2 + (2.625-x + (x*(y**3)))**2
    #return ((1.5 - x + (x*y))**2) + ((2.25 - x + ((x*y)**2))**2) + ((2.625 - x + ((x*y)**3))**2)

def hill_climbing(axo,bxo,ayo,byo,tasa,max_iter=1000):
    start_time = time.time()
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
    #print("Time : ", time.time() - start_time)

    #print(x)
    return funcion(x,y)
    
#hill_climbing(-20,20,-20,20,0.01)

#print(funcion(-3/10,-4/5))

def run():
    for i in range(0,10):
        hill_climbing(-2,2,-2,2,0.3819)


run()
