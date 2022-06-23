def merge_sort(arr, n):
    tmp_arr = [0] * n  # temporary array
    return rec_merge_sort(arr, tmp_arr, 0, n - 1)  # recursive way


def rec_merge_sort(arr, tmp_arr, left, right):
    # more than one element in array -> recursive call
    if left < right:
        mid = (left + right) // 2
        rec_merge_sort(arr, tmp_arr, left, mid)  # left subarray
        rec_merge_sort(arr, tmp_arr, mid + 1, right)  # right subarray
        merge(arr, tmp_arr, left, mid, right)  # merge subarrays


def merge(arr, tmp_arr, left, mid, right):
    # starting indexes: left subarray, right subarray, temporary array
    i, j, k = left,  mid + 1, left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp_arr[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp_arr[k] = arr[j]
            j, k = j + 1, k + 1

    # copy remaining elements
    while i <= mid:
        tmp_arr[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= right:
        tmp_arr[k] = arr[j]
        j, k = j + 1, k + 1

    # copy to origin array
    for ind in range(left, right + 1):
        arr[ind] = tmp_arr[ind]


arr_len = int(input())
array = list(map(int, input().split()))
merge_sort(array, arr_len)  # in-place
print(*array)
