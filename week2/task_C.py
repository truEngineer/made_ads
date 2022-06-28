from itertools import zip_longest, islice


def radix_sort(arr, radix, phases):
    maxnum = max(arr)

    loc = 1
    while loc < maxnum:
        bins = [[] for _ in range(radix)]
        for x in arr:
            i = int((x / loc) % radix)
            bins[i].append(x)
        j = 0
        for i in range(phases):  # phases range(radix):
            for b in bins[i]:
                arr[j] = b
                j += 1
        loc *= radix

    return arr


def count_sort_letters(arr, arr_size, ind):
    count = [0] * 27  # One addition cell to account for dummy letter
    min_base = ord('a') - 1  # subtract one too allow for dummy character

    for item in arr:  # generate Counts
        # get column letter if within string, else use dummy position of 0
        letter = ord(item[ind]) - min_base  #if ind < item_size else 0  # len(item)
        count[letter] += 1

    for i in range(1, 27):  # Accumulate counts
        count[i] += count[i - 1]

    output = [0] * arr_size
    for item in reversed(arr):
        # Get index of current letter of item at index col in count array
        letter = ord(item[ind]) - min_base  #if ind < item_size else 0
        output[count[letter] - 1] = item
        count[letter] -= 1

    return output


# Цифровая сортировка работает за k фаз, где
# k — число цифр в сортируемых числах.
# Фазы нумеруются от одного до k.
# На i-ой фазе производится устойчивая сортировка
# массива по i-ой с конца цифре.
# Таким образом верно: после i-ой фазы если от
# каждого числа оставить последние i цифр,
# получится корректный отсортированный массив.


def radix_sort_letters(array, arr_size, item_size, p_num):
    # p_num: number of sort phases
    for p in range(p_num):
        # range(item_size - 1, -1, item_size - p_num - 1)
        # max_len-1, max_len-2, ... 0  (max_ind - 1, -1, -1)
        array = count_sort_letters(array, arr_size, item_size - 1 - p)
        # LSD (Least Significant Digit) radix sort !!!
    return array
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%A6%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0

#user_input = input("Input numbers separated by a comma:\n").strip()
#nums = [int(item) for item in user_input.split(',')]
n, m, k = map(int, input().split())
#n, m, k = [int(x) for x in input("Enter three value: ").split()]
data = []
for _ in range(n):
    data.append(input())
res = radix_sort_letters(data, n, m, k)
for item in res:
    print(item)
