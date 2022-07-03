import math

def get_func_val(arg, precision):
    left = 0
    right, val = arg, 1

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == arg:
            val = mid
            break
        if mid * mid < arg:
            left = mid + 1
        else:
            right = mid - 1

    increment = 0.1
    for i in range(0, precision):
        while val * val <= arg:
            val += increment
        val -= increment
        increment /= 10

    return val**4 + val  # x**2 + sqrt(x)


from math import log2


def obj_func(x):  # objective function
    return x ** 2 + x ** 0.5


def get_func_arg(val, left, right, eps):
    mid = (left + right) / 2
    # while right - left > eps:
    for _ in range(int(log2((right - left) / eps)) + 1):
        mid = (left + right) / 2
        if obj_func(mid) < val:  # x**2 + sqrt(x) <= c
            left = mid
        else:
            right = mid
    return round(mid, 6)


c = float(input())
print(get_func_arg(c, 1.0, 1e10, 1e-6))

#c = float(18)  # input()
#print(get_func_arg(c, 1.0, 1e10, 1e-6))
#print(f"{get_func_val(x, 6):.10f}")
