from math import log2
 
 
def obj_func(x):  # objective function
    return x ** 2 + x ** 0.5
 
 
def get_func_arg(val, left, right, eps):
    mid = (left + right) / 2
    for _ in range(int(log2((right - left) / eps)) + 1):
        mid = (left + right) / 2
        if obj_func(mid) < val:  # x**2 + sqrt(x) <= c
            left = mid
        else:
            right = mid
    return round(mid, 6)
 
 
c = float(input())
print(get_func_arg(c, 1.0, 1e10, 1e-6))
