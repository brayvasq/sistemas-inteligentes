import math
import random
import decimal

def funcion(x,y):
    #return (x**4) - 14 * (x**3) + 60 * (x**2) - 70 * x 
    return (3 * ((x**2) + (y**2))) + (4*x*y) + (5*x) + (6*y) + 7

def derivada_x(x,y,h):
    return (funcion(x+h,y) - funcion(x,y))/h

def derivada_y(x,y,h):
    return (funcion(x,y+h) - funcion(x,y))/h

def gradiente(axo,bxo,ayo,byo,tolerancia,tasa,max_iter = 10000):
    converged = False

    iteraciones = 0

    x1 = random.randrange(axo,bxo)/10
    y1 = random.randrange(ayo,byo)/10

    h = 0.0005

    k1 = derivada_x(x1,y1,h)
    k2 = derivada_y(x1,y1,h)

    num = 0

    item = 0
    print("\n--------------------- Iteracion : "+str(num)+"----------------------------")
    print("Itero : ","X1" if item==0 else "X2")
    print("X1 : ",x1," Y1 ",y1," - X1' : ",k1," Y1' : ",k2)
    print(" Eval fun : ",funcion(x1,y1))

    while not converged or abs(k1) > tolerancia or abs(k2) > tolerancia:
        num += 1
        
        if item == 0:
            x1 = x1 - tasa * k1
            k1 = derivada_x(x1,y1,h)

            if(x1<axo):
                x1 = axo
            if(x1>(bxo/10)):
                x1 = bxo
            item = 1
        else:
            y1 = y1 - tasa * k2
            k2 = derivada_y(x1,y1,h)

            if(y1<ayo):
                y1 = ayo
            if(y1>(byo/10)):
                y1 = byo
            item = 0

        if x1 == y1:
            converged = True
            #print("Iguales")

        if num == max_iter:
            print("Num max iter")
            #converged = True

        if k1 == 0 and k2==0:
            converged = True
            #print("Derivate = 0")

        if round(abs(k1),6) == round(abs(k2),6):
        #if abs(k1) == abs(k2):        
            converged = True
            #print("Derivate equals")

    print("\n--------------------- Iteracion : "+str(num)+"----------------------------")
    print("Itero : ","X1" if item==0 else "X2")
    print("X1 : ",x1," Y1 ",y1," - X1' : ",k1," Y1' : ",k2)
    print(" Eval fun : ",funcion(x1,y1))

gradiente(-2,2,-2,2,0.1,0.1,max_iter = 10000)