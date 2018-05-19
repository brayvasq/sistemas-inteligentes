import math

def eval(x):
    """
        :param: x -> punto o valor para evaluar en la funcion. Está dado en el intervalo de [2 3]

        :return: retorna x evaluado en la funcion -> f(x) = 8*e^(2-x) + 7*ln(x-1)
    """
    return 8*math.exp(2-x) + 7*math.log(x-1)

def aproximaciones_susecivas(ao,bo,tol,tasa):
    """
        Algoritmo de aproximaciones sucesivas para el calculo del valor minimo
        para la función descrita en el metodo eval()

        :param: ao -> punto inicial del intervalo a evaluar
        :param: bo -> punto final del intervalo a evaluar
        :param: tol -> tolerancia de diferencia entre el resultado y el valor minimo
        :param: tasa -> tasa de aprendizaje. Cada cuanto se va a mover por la función.
    """
    iteraciones = 0
    while( ( bo - ao ) > tol ):
        iteraciones += 1
        a1 = ao + tasa * ( bo - ao ) 
        b1 = bo - tasa * ( bo - ao )

        if eval(a1) < eval(b1):
            bo = b1
        else:
            ao = a1

    if eval(ao) < eval(bo):
        print(eval(ao)," - ao : ",ao," - Iteraciones : ",iteraciones)
    else:
        print(eval(bo)," - bo : ",bo," - Iteraciones : ",iteraciones)

if __name__ == "__main__":
    aproximaciones_susecivas(2,3,0.01,0.01)