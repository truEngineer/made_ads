def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr_len = int(input())
array = list(map(int, input().split()))
print(*bubble_sort(array, arr_len))
