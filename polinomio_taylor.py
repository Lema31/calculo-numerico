import sympy as sp


#Function without intregations
def taylor_polynomial(fx, degree, x0, test_value):
    fx_sym = sp.sympify(fx(x))
    functions = [fx_sym]
    actual_iteration = 0
    result = 0
    relative_error = 100
    real_value = fx_sym.evalf(subs = {x : test_value})

    while(actual_iteration < degree):
        functions.append(functions[actual_iteration].diff())
        actual_iteration += 1

    actual_iteration = 0

    for function in functions:
        if(actual_iteration == 0):
            result += function.evalf(subs = {x : x0})
        if(actual_iteration == 1):
            result += function.evalf(subs = {x : x0}) * (test_value - 1)
        if(actual_iteration >= 2):
            result += (function.evalf(subs={x: x0}) * (test_value - 1) ** actual_iteration) / sp.factorial(actual_iteration)

        actual_iteration += 1
    relative_error = abs((real_value - result) / real_value)

    return result, relative_error


#Function with integrations
def taylor_polynomial_integrating(fx, degree, interval):
    fx_sym = sp.sympify(fx(x))
    functions = [fx_sym]
    actual_iteration = 0
    result = 0
    relative_error = 100
    test_value = (interval[0] + interval[1]) / 2
    real_value = sp.integrate(fx_sym, (x, interval[0], interval[1])).evalf()

    while (actual_iteration < degree):
        functions.append(functions[actual_iteration].diff())
        actual_iteration += 1

    actual_iteration = 0

    for function in functions:
        if(actual_iteration == 0):
            result += sp.integrate(function.evalf(subs = {x : test_value}),(x,interval[0],interval[1])).evalf()
        if(actual_iteration == 1):
            func = function.evalf(subs = {x : test_value}) * (x - test_value)
            result += sp.integrate(func, (x,interval[0],interval[1])).evalf()
        if(actual_iteration >= 2):
            func = (function.evalf(subs={x: test_value})) * ((x - test_value) ** actual_iteration) / sp.factorial(actual_iteration)
            result += sp.integrate(func, (x,interval[0],interval[1])).evalf()

        actual_iteration += 1
    if(result != real_value):
        relative_error = abs((real_value - result) / real_value)
    else:
        relative_error = 0

    return result, relative_error


x = sp.Symbol('x')
if __name__ == "__main__":
    #data
    fx = lambda x: x * sp.ln(x)
    degree = 3
    x0 = 1
    test_value = 1.3
    result, relative_error = taylor_polynomial(fx, degree, x0, test_value)
    print("valor aproximado: " + str(result))
    print("Error relativo: " + str(relative_error))

    #fx = lambda x: x * sp.cos(x**2)
    fx = lambda x: sp.exp(x)
    degree = 5
    interval = [0, 1]
    result, relative_error = taylor_polynomial_integrating(fx, degree, interval)
    print("valor aproximado: " + str(result))
    print("Error relativo: " + str(relative_error))

