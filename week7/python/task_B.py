import math
 
BASE = 2
A_LIN = 23
A_CONST = 21563
A_DIV = 16714589
INF = A_DIV
ANS_PREV = None  # for previous answer
 
 
def a_generator(a_term, n_elements):
    yield a_term  # yield a[i]
    for _ in range(n_elements - 1):
        a_term = (A_LIN * a_term + A_CONST) % A_DIV
        yield a_term
 
        
def requests_generator(u, v, n_requests):
    yield u, v  # first request
    for ind in range(2, n_requests + 1):
        # too much constants to create CONSTANTS...
        u = ((17 * u + 751 + ANS_PREV + 2 * (ind - 1)) % n) + 1
        v = ((13 * v + 593 + ANS_PREV + 5 * (ind - 1)) % n) + 1
        yield u, v  # request #ind
 
 
def rmq(left, right, min_arr):
    max_power = int(math.log(right - left + 1, BASE))
    return min(min_arr[left][max_power],
               min_arr[right - BASE ** max_power + 1][max_power])
    
 
 
# n - number of elements
# m - number of requests
# a_1 - first element
n, m, a_1 = map(int, input().split())
# first request
u_1, v_1 = map(int, input().split())
# generate array of a's
a_arr = [a_i for a_i in a_generator(a_1, n)]
 
# array for min's
min_a = [[INF for _ in range(int(math.log(n - left, BASE)) + 1)] for left in range(n)]
max_power = int(math.log(n, BASE)) + 1
# initialization of min_a[left][0] for DP
for ind in range(n):
    min_a[ind][0] = a_arr[ind]
# fill the min_a array with DP
for power in range(1, max_power):
    for left in range(n):
        if power <= len(min_a[left]) - 1:
            min_a[left][power] = min(min_a[left][power - 1], 
                                     min_a[left + BASE ** (power - 1)][power - 1])
 
# requests
for u, v in requests_generator(u_1, v_1, m):
    if u < v:
        left, right = u, v
    else:
        left, right = v, u
    # u and v >= 1
    ANS_PREV = rmq(left - 1, right - 1, min_a)
print(u, v, ANS_PREV)
