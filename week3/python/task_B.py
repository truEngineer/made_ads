def lower_bound(arr, val):
    # arr is sorted
    # returns element's index i: element arr[i] <= val
    len_arr = len(arr)
    left = -1  # left boundary
    right = len_arr  # right boundary
    if val > arr[-1]:
        return right
    if val < arr[0]:
        return left + 1  # there is no lower bound (it's at infinity)
    while right - left > 1:
        # separates arr[left..right] in two equal parts
        middle = (left + right) // 2
        if val > arr[middle]:  # arr[left] < val < arr[right]
            left = middle
        else:
            right = middle
    if (arr[left] < val) or (left == -1):
        left += 1  # if there is no element in arr, return the first which is larger
    return left
 
 
len_arr = int(input())
init_arr = list(map(int, input().split()))  # input unsorted list
sorted_arr = sorted(init_arr)  # sorting
sorted_arr_neg = sorted([-elem for elem in sorted_arr])  # sorted arr of elements*(-1)
requests_n = int(input())  # number of requests
count_arr = []  # list of requests answers
for req in range(requests_n):
    left, right = map(int, input().split())
    lower_bound_req = lower_bound(sorted_arr, left)
    # calculate upper bound via lower bound of the negative array!
    upper_bound_req = len(init_arr) - 1 - (lower_bound(sorted_arr_neg, -right) - 1)
    count_arr.append(upper_bound_req - lower_bound_req)
print(*count_arr)
