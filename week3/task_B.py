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
 
 
n = int(sys.stdin.readline()) # numbers
nums = sorted(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline()) # requests
result = []
for _ in range(k):
    l, r = map(int, sys.stdin.readline().split())
    min_ind = get_min_ind(nums, n, l)
    max_ind = get_max_ind(nums, n, r)
    result.append(max_ind - min_ind + 1)
print(*result)
