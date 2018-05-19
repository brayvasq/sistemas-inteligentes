

import math

def eval(x):
    """
        :param: x -> punto o valor para evaluar en la funcion. Está dado en el intervalo de [2 3]

        :return: retorna x evaluado en la funcion -> f(x) = 8*e^(2-x) + 7*ln(x-1)
    """
    return 8*math.exp(2-x) + 7*math.log(x-1)
    #return (x**4) - 14 * (x**3) + 60 * (x**2) - 70 * x

def seccion_dorada(ao,bo,tol):
    """
        Algoritmo de seccion dorada para el calculo del valor minimo
        para la función descrita en el metodo eval()

        :param: ao -> punto inicial del intervalo a evaluar
        :param: bo -> punto final del intervalo a evaluar
        :param: tol -> tolerancia de diferencia entre el resultado y el valor minimo
    """
    iteraciones = 0
    
    #numero_aureo = 2 - (1 + (math.sqrt(5))/2)
    #numero_aureo = 0.68;
    numero_aureo = 2 - ((1 + math.sqrt(5)) / 2)
    print("phi : ",numero_aureo)

    a1 = ao + numero_aureo * ( bo - ao ) 
    b1 = bo - numero_aureo * ( bo - ao )
    
    evala = eval(a1)
    evalb = eval(b1)

    while( ( bo - ao ) > tol):
        iteraciones += 1
        
        if evala < evalb:
            bo = b1
            b1 = a1
            a1 = ao + ( bo - ao ) * numero_aureo
            evalb = evala
            evala = eval(a1)
        else:
            ao = a1
            a1 = b1
            b1 = bo - ( bo - ao ) * numero_aureo
            evala = evalb
            evalb = eval(b1)

    print( (evala + evalb)/2 ," - pos : ",(ao+bo)/2,"  - Iteraciones : ",iteraciones)

if __name__ == "__main__":
    #seccion_dorada(0,2,0.01)
    seccion_dorada(2,3,0.1)