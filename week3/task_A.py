def binary_search(arr, arlen, key):
    left, right = 0, arlen - 1
    closest = left
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            closest = mid
            break
        if abs(arr[mid] - key) < abs(arr[closest] - key):
            closest = mid
        if closest > 0 and abs(arr[closest - 1] - key) == abs(arr[closest] - key):
            closest -= 1
    return arr[closest]
 
 
n, k = map(int, input().split())
arr = list(map(int, input().split()))
keys = list(map(int, input().split()))
for key in keys:
    print(binary_search(arr, n, key))
