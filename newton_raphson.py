import sympy as sp
import math

def newton_raphson(fx, start, min_error, max_iterations):
    message = "El algoritmo no converge en la funcion dada"
    relative_error = 100
    previous_error = 0
    actual_iteration = 0
    actual_m = start
    previous_m = 0
    fx_sym = sp.sympify(fx(x))
    fx_derivative = fx_sym.diff(x)

    while((actual_iteration < max_iterations) and (relative_error > min_error)):
        previous_m = actual_m
        try:
            actual_m = actual_m - ((fx(actual_m))/(fx_derivative.evalf(subs={x: actual_m})))
        except ZeroDivisionError:
            return "No se puede hacer una division entre 0"

        if(actual_iteration >= 1):
            previous_error = relative_error
            relative_error = abs((actual_m - previous_m) / actual_m)
            if(math.isnan(relative_error)):
                return message

            if(actual_iteration >= 2):
                if (relative_error > (2 * previous_error)):
                    return message

        actual_iteration+= 1
    if __name__ == "__main__":
        print("Numero de iteraciones:" + str(actual_iteration))
        print("Error relativo: " + str(relative_error))
        print("Valor mas aproximado a P: " + str(actual_m))
    return actual_m


x = sp.Symbol('x')
if __name__ == "__main__":
    #Data
    max_iterations = 50
    fx = lambda x: x**2 - 2*x + 1
    start_point = 0.5
    error = 0
    print(newton_raphson(fx, start_point, error, max_iterations))






