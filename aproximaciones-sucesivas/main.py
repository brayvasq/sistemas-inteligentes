import math

def funcion(x):
    """
        :param: x -> punto o valor para funcionuar en la funcion. Está dado en el intervalo de [2 3]

        :return: retorna x funcionuado en la funcion -> f(x) = 8*e^(2-x) + 7*ln(x-1)
    """
    #return 8*math.exp(2-x) + 7*math.log(x-1)
    return (x**4) - 14 * (x**3) + 60 * (x**2) - 70 * x

def aproximaciones_susecivas(ao,bo,tol,tasa):
    """
        Algoritmo de aproximaciones sucesivas para el calculo del valor minimo
        para la función descrita en el metodo funcion()

        :param: ao -> punto inicial del intervalo a funcionuar
        :param: bo -> punto final del intervalo a funcionuar
        :param: tol -> tolerancia de diferencia entre el resultado y el valor minimo
        :param: tasa -> tasa de aprendizaje. Cada cuanto se va a mover por la función.
    """
    iteraciones = 0
    while( ( bo - ao ) > tol ):
        iteraciones += 1
        a1 = ao + tasa * ( bo - ao ) 
        b1 = bo - tasa * ( bo - ao )

        if funcion(a1) < funcion(b1):
            bo = b1
        else:
            ao = a1

    if funcion(ao) < funcion(bo):
        print(funcion(ao)," - ao : ",ao," - Iteraciones : ",iteraciones)
    else:
        print(funcion(bo)," - bo : ",bo," - Iteraciones : ",iteraciones)

if __name__ == "__main__":
    aproximaciones_susecivas(0,2,0.01,0.01)
    #aproximaciones_susecivas(2,3,0.1,0.1)