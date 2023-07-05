import math


def sum_riemann(f, interval, n):
    h = (interval[1] - interval[0]) / n
    acum = 0

    for i in range(n + 1):
        x = interval[0] + i * h
        acum += h * f(x)

    return acum

def trapezoid_method(f, interval, n):
    h = (interval[1] - interval[0]) / n
    acum = 0

    for i in range(n):
        x = interval[0] + i * h
        x2 = interval[0] + (i + 1) * h
        acum += (h * (f(x) + f(x2))) / 2

    return acum


# Data.

if __name__ == "__main__":
    fx = lambda x: math.cos(x**2)
    interval = [0,1]
    n = 10000

    print(trapezoid_method(fx, interval, n))
