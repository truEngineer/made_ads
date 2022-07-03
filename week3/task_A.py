def binary_search2(arr, arlen, key):
    left = 0
    right = arlen - 1

    while left <= right:
        mid = left + (right - left) // 2
        current_item = arr[mid]
        if current_item == key:
            print(arr[mid + 1])
            break
            # return mid
        elif current_item > key:
            right = mid - 1
        else:
            left = mid + 1

    if key - arr[left] <= arr[right]:
        print(arr[right])
    else:
        print(arr[left])
    #return None


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
        # check if arr[mid] is closer to 'key' than arr[closest]
        if abs(arr[mid] - key) < abs(arr[closest] - key):
            closest = mid
        if closest > 0 and abs(arr[closest - 1] - key) == abs(arr[closest] - key):
            closest -= 1
    return arr[closest]


n, k = 5, 5  # map(int, input().split())
arr = [1, 3, 5, 7, 9]  # list(map(int, input().split()))
keys = [2, 4, 8, 1, 6]  # list(map(int, input().split()))
for key in keys:
    print(binary_search(arr, n, key))
# 5 5    1 3 5 7 9    2 4 8 1 6    (1 3 7 1 5)
