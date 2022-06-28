import random


def quick_sort(arr, first, last):
    if last <= first:
        return

    # len(arr) > 1
    left, right = first, last
    pivot = arr[random.randint(first, last)]

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

    return arr


def dummy_median(arr, arlen):  # nlog(n)
    quick_sort(arr, 0, arlen - 1)
    if arlen % 2 == 1:
        return arr[arlen / 2]
    else:
        return 0.5 * (arr[arlen / 2 - 1] + arr[arlen / 2])


def quickselect_median(arr, arlen, pivot_fn=random.choice):
    if arlen % 2 == 1:
        return quick_select(arr, arlen / 2, pivot_fn)
    else:
        return 0.5 * (quick_select(arr, arlen / 2 - 1, pivot_fn) +
                      quick_select(arr, arlen / 2, pivot_fn))


def quick_select(arr, k, pivot_fun=random.choice):
    """
    Выбираем k-тый элемент в списке arr (с нулевой базой)
    :param arr: список числовых данных
    :param k: индекс
    :param pivot_fun: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент arr
    """
    if len(arr) == 1:
        assert k == 0
        return arr[0]

    pivot = pivot_fun(arr)

    part_low = [x for x in arr if x < pivot]
    part_high = [x for x in arr if x > pivot]
    part_piv = [x for x in arr if x == pivot]

    len_low, len_piv = len(part_low), len(part_piv)

    if k < len_low:
        return quick_select(part_low, k, pivot_fun)
    elif k < len_low + len_piv:
        # Нам повезло и мы угадали медиану
        return part_piv[0]
    else:
        return quick_select(part_high, k - len_low - len_piv, pivot_fun)


def pick_pivot(arr):
    """
    Выбираем хорошй pivot в списке чисел l
    Этот алгоритм выполняется за время O(n).
    """
    arlen = len(arr)
    assert arlen > 0

    # Если элементов < 5, просто возвращаем медиану
    if arlen < 5:
        # В этом случае мы возвращаемся к первой написанной нами функции медианы.
        # Поскольку мы выполняем её только для списка из пяти или менее элементов, она не
        # зависит от длины входных данных и может считаться постоянным
        # временем.
        return dummy_median(arr, arlen)

    # Сначала разделим l на группы по 5 элементов. O(n)
    chunks = get_chunks(arr, arlen, 5)

    # Для простоты мы можем отбросить все группы, которые не являются полными. O(n)
    all_chunks = [chunk for chunk in chunks if len(chunk) == 5]

    # Затем мы сортируем каждый фрагмент. Каждая группа имеет фиксированную длину, поэтому каждая сортировка
    # занимает постоянное время. Поскольку у нас есть n/5 фрагментов, эта операция
    # тоже O(n)
    sorted_groups = [quick_sort(chunk, 0, 5 - 1) for chunk in all_chunks]

    # Медиана каждого фрагмента имеет индекс 2
    medians = [chunk[2] for chunk in sorted_groups]

    # Возможно, я немного повторюсь, но я собираюсь доказать, что нахождение
    # медианы списка можно произвести за доказуемое O(n).
    # Мы находим медиану списка длиной n/5, поэтому эта операция также O(n)
    # Мы передаём нашу текущую функцию pick_pivot в качестве создателя pivot алгоритму
    # quickselect. O(n)
    median_of_medians = quickselect_median(medians, len(medians), pick_pivot)
    return median_of_medians


def get_chunks(arr, arlen, chunk_size):
    """Разделяем список `l` на фрагменты размером `chunk_size`."""
    return [arr[i : i + chunk_size] for i in range(0, arlen, chunk_size)]





def partition(arr, p, q):
    pivot = arr[p]  # first element as pivot
    # element whose index less than r is less than or equal to pivot
    r = p  #
    # element whose index between r and i is larger than pivot
    # O(n)
    for i in range(r + 1, q):
        if arr[i] <= pivot:
            r += 1
            # do exchange
            arr[r], arr[i] = arr[i], arr[r]
    # exchange pivot and arr[r]
    arr[p], arr[r] = arr[r], pivot
    return r


def random_partition(arr, p, q):
    # generate a random index
    rand_ind = random.randint(p, q - 1)
    # swap first element with random number
    arr[p], arr[rand_ind] = arr[rand_ind], arr[p]
    # tmp = arr[p] # arr[p] = arr[random_index] # arr[random_index] = tmp

    pivot = arr[p]  # first element as pivot
    # element whose index less than r is less than or equal to pivot
    r = p  # result index
    # element whose index between r and i is larger than pivot
    # O(n)
    for i in range(r + 1, q):
        if arr[i] <= pivot:
            r += 1
            # do exchange
            arr[r], arr[i] = arr[i], arr[r]
    # exchange pivot and arr[r]
    arr[p], arr[r] = arr[r], pivot
    return r

    #return partition(arr, p, q)


def quick_select2(arr, p, q, k):
    if p == q:
        return arr[p]

    r = random_partition(arr, p, q)

    if k == r:
        return arr[r]
    elif k < r:
        return quick_select(arr, p, r, k)
    else:
        return quick_select(arr, r + 1, q, k)


n = int(input())
iqs = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    i, j, k_num = map(int, input().split())  # request
    i, k_num = i - 1, k_num - 1  # list indexing starts with 0
    # res = quick_select(iqs[i:j], 0, j - i, k_num)
    res = quick_select(iqs[i:j], k_num)
    print(res)


###  k order statistic == quick select

in_lines = """5
1 3 2 4 5
3
1 3 2
1 5 1
1 5 2"""

"""lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
print(lines)

n = int(lines[0])
iqs = list(map(int, lines[1].split()))
m = int(lines[2])
requests = []
for i in range(m):
    requests.append(tuple(map(int, lines[3 + i].split())))"""
