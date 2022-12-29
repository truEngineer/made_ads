import math
 
 
START = (0, 1)  # home coordinate
END = (1, 0)  # glade coordinate
N_DIGITS_MIN = 4
 
 
def dist(pnt_1, pnt_2):
    return math.sqrt((pnt_1[0] - pnt_2[0]) ** 2 + (pnt_1[1] - pnt_2[1]) ** 2)
 
 
def walk_time(pnt_mid, v_field, v_forest):
    return dist(START, pnt_mid) / v_field + dist(pnt_mid, END) / v_forest
 
 
def forest_input_point(bound, v_field, v_forest, acc=1e-6):
    left = START[0]
    right = END[0]
    RATIO = 3 / 2
    n_iterations = int(math.log((right - left), RATIO) - math.log(acc, RATIO))
    for _ in range(n_iterations): # right - left > eps:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        time1 = walk_time((mid1, bound), v_field, v_forest);
        time2 = walk_time((mid2, bound), v_field, v_forest)
        if time1 > time2:
            left = mid1
        else:
            right = mid2
    return round(left, N_DIGITS_MIN + 1)
 
 
vp, vf = map(int, input().split())
a = float(input())
print(forest_input_point(a, vp, vf))
