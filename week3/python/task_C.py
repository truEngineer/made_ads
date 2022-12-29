import math
 
 
def f_squared_square(x):
    return x**2 + x**(1 / 2)
 
 
def real_binary_search(f, left, right, val, acc):
    # solving equation 'f(x) = val' with accuracy 'acc'
    RATIO = 2
    BASE = 10
    n_ans_digits = int(-round(math.log(acc, BASE)))  # number of digits after comma
    n_iterations = int(math.log((right - left), RATIO) - math.log(acc / BASE, RATIO))
    for iter_i in range(n_iterations + 1):
        ans = (left + right) / RATIO
        f_val = f(ans)  # calculate the function
        if math.isclose(f_val, val, abs_tol=acc):
            return round(ans, n_ans_digits)
        if f_val > val:
            right = ans
        else:
            left = ans
    return round(ans, n_ans_digits)
 
 
# function x**2 + sqrt(x) = f(x) is monotonic from 0 to inf
# f(x) = C: where 1 < C < 10**10
# hence, x is not larger than 10^5
C_MAX = 10**10
C_MIN = 1
ACCURACY = 1e-6  # necessary accuracy for the answer
f_value = float(input())
print(real_binary_search(f_squared_square, C_MIN, C_MAX, f_value, ACCURACY))
