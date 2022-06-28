def count_sort(arr, arlen, maxnum):
    count = [0] * (maxnum + 1)
    # count of each number in array
    for j in range(arlen):
        count[arr[j]] += 1

    # count of numbers in array <= current number (i)
    for i in range(1, maxnum + 1):
        count[i] += count[i - 1]

    # from right to left for stability
    res = [0] * arlen
    for j in range(arlen - 1, -1, -1):
        ind = arr[j]
        res[count[ind] - 1] = ind
        count[ind] -= 1

    return res


array = list(map(int, input().split()))
print(*count_sort(array, len(array), 100))
