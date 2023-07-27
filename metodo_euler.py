import math

def euler_method(f, interval, n, yi):
    h = (interval[1] - interval[0]) / n
    result ={}
    actual_y = yi

    for i in range(n + 1):
        result[i] = round(actual_y + h * f(actual_y, interval[0] + (h * i)), 4)
        actual_y = result[i]

    return result

if __name__ == "__main__":
    f = lambda y, t: ((t - y) ** 2) +1
    interval = [2, 3]
    n = 4
    yi = 1

    print(euler_method(f, interval, n, yi))