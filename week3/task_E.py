def obj_func(m, t_x, t_y, n_c):  # objective function
    return m // t_x + m // t_y - n_c + 1
 
 
def calc_time(num_copy, time_x, time_y):
    if num_copy == 1:
        return min(time_x, time_y)
    else:
        left = 0
        right = (num_copy - 1) * max(x, y)
 
        while right - left > 1:
            mid = (right + left) // 2
            if obj_func(mid, time_x, time_y, num_copy) >= 0:
                right = mid
            else:
                left = mid
        return min(x, y) + left + 1
 
 
n, x, y = map(int, input().split())
print(calc_time(n, x, y))
