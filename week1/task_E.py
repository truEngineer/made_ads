from random import randint


def quick_sort(arr, first, last):

    if last <= first:
        return

    # len(arr) > 1
    left, right = first, last
    pivot = arr[randint(first, last)]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quick_sort(arr, first, right)
    quick_sort(arr, left, last)


# https://geekbrains.ru/posts/python_sort
arr_len = int(input())
array = list(map(int, input().split()))
quick_sort(array, 0, arr_len - 1)  # in-place
print(*array)
