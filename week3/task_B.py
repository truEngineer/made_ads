import sys


def get_min_ind(arr, arlen, key):
    left = 0
    right = arlen - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= key:
            right = mid - 1
        else:
            left = mid + 1
    return left  # first index >= key


def get_max_ind(arr, arlen, key):
    left = 0
    right = arlen - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= key:
            left = mid + 1
        else:
            right = mid - 1
    return right  # last index <= key


def get_min_max_ind(arr, arlen, key_min, key_max):
    left_min, left_max = 0, 0
    right_min, right_max = arlen - 1, arlen - 1
    while left_min <= right_min or left_max <= right_max:
        mid_min = left_min + (right_min - left_min) // 2
        mid_max = left_max + (right_max - left_max) // 2
        if arr[mid_min] >= key_min:
            right_min = mid_min - 1
        else:
            left_min = mid_min + 1
        if arr[mid_max] <= key_max:
            left_max = mid_max + 1
        else:
            right_max = mid_max - 1
    return left_min, right_max  # first index >= key, last index <= key


def lower_bound(arr, arlen, key):
    left = 0
    right = arlen - 1
    while right >= left:
        mid = left + (left + right) // 2
        if arr[mid] >= key:
            right = mid - 1
        else:
            left = mid + 1
    return left


# numbers
n = int(sys.stdin.readline())  # int(input())  # 5
nums = sorted(map(int, sys.stdin.readline().split()))  # list(map(int, input().split()))  # [10, 1, 10, 3, 4]
# requests
k = int(sys.stdin.readline())  # int(input())  # 4
result = []
for i in range(k):  # _
    # l, r = [(1, 10), (2, 9), (3, 4), (2, 2)][i]  # l, r = map(int, input().split()) # [(1, 10), (2, 9), (3, 4), (2, 2)]
    l, r = map(int, sys.stdin.readline().split())
    min_ind = get_min_ind(nums, n, l)
    max_ind = get_max_ind(nums, n, r)
    result.append(max_ind - min_ind + 1)

    # min_ind, max_ind = get_min_max_ind(nums, n, l, r)
    # result.append(max_ind - min_ind + 1)
print(*result)  # 5 2 2 0

"""n = int(input())  # array
nums = sorted(map(int, input().split()))
k = int(input())  # requests
result = []
for _ in range(k):
    l, r = map(int, input().split())
    min_ind, max_ind = get_min_max_ind(nums, n, l, r)
    result.append(max_ind - min_ind + 1)
print(*result)"""
