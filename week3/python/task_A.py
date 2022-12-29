
def lower_bound(arr, val):
    # arr is sorted
    # returns element's index i: element arr[i] <= val
    arr_len = len(arr)
    left = -1  # left boundary
    right = arr_len  # right boundary
    while right - left > 1:
        # separates arr[left..right] in two equal parts
        middle = (left + right) // 2
        if val >= arr[middle]:  # arr[left] <= val < arr[right]
            left = middle
        else:  # val is out of arr range (at right)
            right = middle
    
    if left == arr_len:  # out of range index
        return left - 1
    if left == arr_len - 1:  # already the last element
        return left
    # check if arr[left + 1] is closer to val
    if (left == -1) or (abs(arr[left] - val) > abs(arr[left + 1] - val)):
        return left + 1
    return left
 
 
k, n = map(int, input().split())
sorted_arr = list(map(int, input().split()))
requests = list(map(int, input().split()))
for request in requests:
    print(sorted_arr[lower_bound(sorted_arr, request)])
