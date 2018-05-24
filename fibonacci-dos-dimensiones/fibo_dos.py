import math
import random
import decimal

def funcion(x,y):
    return (3 * ((x**2) + (y**2))) + (4*x*y) + (5*x) + (6*y) + 7
    #return 8*math.exp(2-x) + 7*math.log(x-1)

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

def busqueda_fibonacci(ao,bo,co,val,tol):
    """
        Algoritmo de busqueda fibonacci para el calculo del valor minimo
        para la función descrita en el metodo eval()

        :param: ao -> punto inicial del intervalo a evaluar
        :param: bo -> punto final del intervalo a evaluar
        :param: tol -> tolerancia de diferencia entre el resultado y el valor minimo
    """

    limit = round((bo - ao)/tol)
    print(limit)
    j = 0
    c = fibonacci(j)
    while c < limit:
        j += 1
        c = fibonacci(j)

    n = j

    a1 = ao + fibonacci(n-2)/fibonacci(n) * (bo - ao)
    b1 = ao + fibonacci(n-1)/fibonacci(n) * (bo - ao)
    print(a1)
    print(b1)
 
    evala = 0
    evalb = 0
    if(val):
        evala = funcion(a1,co)
        evalb = funcion(b1,co)
    else:
        evala = funcion(co,a1)
        evalb = funcion(co,b1)

    iteraciones = 0
    while(tol > (1/fibonacci(n+1))):

        iteraciones += 1

        if evala > evalb:
            ao = a1
            a1 = b1
            b1 = ao + (fibonacci(n-1)/fibonacci(n)) * (bo-ao)
            evala = evalb
            if(val):
                evalb = funcion(b1,co)
            else:
                evalb = funcion(co,b1)
        else:
            bo = b1
            b1 = a1
            evalb = evala
            a1 = ao + (fibonacci(n-2)/fibonacci(n)) * (bo-ao)
            if(val):
                evalb = funcion(a1,co)
            else:
                evalb = funcion(co,a1)

        n -= 1
        
    #print("evala : ",evala," evalb : ",evala)
        print("ao : ",ao," bo : ",bo, " co : ",co)
    #print("Media eval : ", (evala+evalb)/2)
    #print("Media point : ",(ao+bo)/2, " Iteraciones : ",iteraciones)
    return (ao+bo)/2

def fibo_dos(axo,bxo,ayo,byo,tol,max_iter=10000):
    converged = False
    num = 0
    y = random.randrange(ayo,byo)/10
    while(not converged):
        num += 1
        print("NUM : ",num)
        axo = busqueda_fibonacci(axo,bxo,y,True,tol)
        ayo = busqueda_fibonacci(ayo,byo,axo,False,tol)
        
        print("AX : ",axo)
        print("BX : ",bxo)
        print(funcion(axo,bxo))

        if round(axo,6) == round(ayo,6):
            converged = True

        if max_iter == num:
            converged = True


fibo_dos(-20,20,-20,20,0.1,max_iter = 1000)
#fibo_dos(2,3,2,3,0.1,max_iter = 1000)
