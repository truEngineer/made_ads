def count_invs(arr, n):
    tmp_arr = [0] * n  # temporary array
    return rec_merge_sort(arr, tmp_arr, 0, n - 1)  # recursive way


def rec_merge_sort(arr, tmp_arr, left, right):
    inv_count = 0
    # more than one element in array -> recursive call
    if left < right:
        mid = (left + right) // 2
        inv_count += rec_merge_sort(arr, tmp_arr, left, mid)  # left subarray
        inv_count += rec_merge_sort(arr, tmp_arr, mid + 1, right)  # right subarray
        inv_count += merge(arr, tmp_arr, left, mid, right)  # merge subarrays
    return inv_count


def merge(arr, tmp_arr, left, mid, right):
    inv_count = 0
    # starting indexes: left subarray, right subarray, temporary array
    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            # no inversions
            tmp_arr[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            # inversions occurs
            tmp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j, k = j + 1, k + 1
    # copy the remaining elements of left subarray into temporary array
    while i <= mid:
        tmp_arr[k] = arr[i]
        i, k = i + 1, k + 1
    # copy the remaining elements of right subarray into temporary array
    while j <= right:
        tmp_arr[k] = arr[j]
        j, k = j + 1, k + 1

    # copy to origin array
    for ind in range(left, right + 1):
        arr[ind] = tmp_arr[ind]

    return inv_count


arr_len = int(input())
array = list(map(int, input().split()))
print(count_invs(array, arr_len))
