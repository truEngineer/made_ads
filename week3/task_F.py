import math


def get_len(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_coordinate(a, v_p, v_f, eps):
    left, right = 0, 1
    for _ in range(int(math.log2((right - left) / eps)) + 1):
        mid = (left + right) / 2
        len1 = get_len(0, 1, mid, a) / v_p + get_len(1, 0, mid, a) / v_f
        len2 = get_len(0, 1, mid - eps, a) / v_p + get_len(1, 0, mid - eps, a) / v_f
        if len1 > len2:
            right = mid
        else:
            left = mid
    return right


vp, vf = map(int, input().split())
a = float(input())
print(round(get_coordinate(a, vp, vf, 1e-9), 9))
