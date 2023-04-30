import sympy as sp

def newton_raphson(fx, start, min_error, max_iterations):
    relative_error = 100
    previous_error = 0
    actual_iteration = 0
    actual_m = start
    previous_m = 0
    fx_sym = sp.sympify(fx(x))
    fx_derivative = fx_sym.diff(x)

    while((actual_iteration < max_iterations) and (relative_error > min_error)):
        previous_m = actual_m
        actual_m = actual_m - ((fx(actual_m))/(fx_derivative.evalf(subs={x: actual_m})))

        if(actual_iteration >= 1):
            previous_error = relative_error
            relative_error = abs((actual_m - previous_m) / actual_m)
            if(actual_iteration >= 2):
                if (relative_error > (3 * previous_error)):
                    return "El algoritmo no converge en la funcion dada"

        actual_iteration+= 1
    print("Numero de iteraciones:" + str(actual_iteration))
    print("Error relativo: " + str(relative_error))
    print("Valor mas aproximado a P: " + str(actual_m))
    return actual_m


#Data
x = sp.Symbol('x')
max_iterations = 50
fx = lambda x: x**3 - x + 1
start_point = 0.5
error = 0.000006

print(newton_raphson(fx, start_point, error, max_iterations))



