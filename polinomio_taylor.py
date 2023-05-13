import sympy as sp
import math

#Function without intregations
def taylor_polynomial(fx, grade, x0, test_value):
    fx_sym = sp.sympify(fx(x))
    functions = [fx_sym]
    actual_iteration = 0
    result = 0
    relative_error = 100
    real_value = fx_sym.evalf(subs = {x : test_value})

    while(actual_iteration < grade):
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
    relative_error = (real_value - result) / real_value

    return result, relative_error


#Function with integrations
def taylor_polynomial_integrating(fx, grade, interval):
    pass


x = sp.Symbol('x')
if __name__ == "__main__":
    #data
    fx = lambda x: x * sp.ln(x)
    grade = 3
    x0 = 1
    test_value = 1.3
    result, relative_error = taylor_polynomial(fx, grade, x0, test_value)
    print("valor aproximado: " + str(result))
    print("Error relativo: " + str(relative_error))

    fx = lambda x: x * sp.cos(x**2)
    grade = 2
    interval = [0,2]
    taylor_polynomial_integrating(fx, grade, interval)

