import math

def funcion(x):
    """
        :param: x -> punto o valor para evaluar en la funcion. Está dado en el intervalo de [2 3]

        :return: retorna x evaluado en la funcion -> f(x) = 8*e^(2-x) + 7*ln(x-1)
    """
    return 8*math.exp(2-x) + 7*math.log(x-1)
    #return (x**4) - 14 * (x**3) + 60 * (x**2) - 70 * x

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

def busqueda_fibonacci(ao,bo,tol):
    """
        Algoritmo de busqueda fibonacci para el calculo del valor minimo
        para la función descrita en el metodo eval()

        :param: ao -> punto inicial del intervalo a evaluar
        :param: bo -> punto final del intervalo a evaluar
        :param: tol -> tolerancia de diferencia entre el resultado y el valor minimo
    """

    limit = round((bo - ao)/tol)
    j = 0
    c = fibonacci(j)
    while c < limit:
        j += 1
        c = fibonacci(j)

    n = j

    a1 = ao + fibonacci(n-2)/fibonacci(n) * (bo - ao)
    b1 = ao + fibonacci(n-1)/fibonacci(n) * (bo - ao)

    evala = funcion(a1)
    evalb = funcion(b1)

    iteraciones = 0
    while(tol > (1/fibonacci(n+1))):

        iteraciones += 1

        if evala > evalb:
            ao = a1
            a1 = b1
            b1 = ao + (fibonacci(n-1)/fibonacci(n)) * (bo-ao)
            evala = evalb
            evalb = funcion(b1)
        else:
            bo = b1
            b1 = a1
            evalb = evala
            a1 = ao + (fibonacci(n-2)/fibonacci(n)) * (bo-ao)
            evala = funcion(a1)

        n -= 1
        
    #print("evala : ",funcion(ao)," evalb : ",funcion(bo))
    #print("ao : ",ao," bo : ",bo)
    #print("Media eval : ", (funcion(ao)+funcion(bo))/2)
    #print("Media point : ",(ao+bo)/2, " Iteraciones : ",iteraciones)
    if funcion(ao) < funcion(bo):
        print(funcion(ao)," - ao : ",ao," - Iteraciones : ",iteraciones)
    else:
        print(funcion(bo)," - bo : ",bo," - Iteraciones : ",iteraciones)




if __name__ == "__main__":
    busqueda_fibonacci(2,3,0.0001)
    #busqueda_fibonacci(0,2,0.0001)