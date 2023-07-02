import math


def biseccion(fx, interval, min_error, max_iterations):
    relative_error = 100
    actual_iteration = 0
    actual_m = 0
    previous_m = 0

    assert fx(interval[0]) * fx(interval[1]) < 0, "La función no cumple con el Teorema de Bolzano en el intervalo dado."

    while((actual_iteration < max_iterations) and (relative_error > min_error)):
        previous_m = actual_m
        actual_m = (interval[0] + interval[1])/2

        if(fx(actual_m) * fx(interval[1]) < 0):
            interval[0] = actual_m
        else:
            interval[1] = actual_m

        if(actual_iteration >= 1):
            relative_error = abs((actual_m - previous_m)/actual_m)

        actual_iteration+= 1

    if __name__ == "__main__":
        print("Numero de iteraciones:" + str(actual_iteration))
        print("Error relativo: " + str(relative_error))
        print("Valor mas aproximado a P: " + str(actual_m))

    return actual_m



# Data.

if __name__ == "__main__":
    fx = lambda x: math.e ** x - 3 * x ** 2
    interval = [0,1]
    error = 0.03
    max_iterations = 50

    print(biseccion(fx, interval, error, max_iterations))

