MAX_N = 100


lst_test = list(map(int, input().split()))
lst_sorted = []
elems_amount = [0] * (MAX_N + 1)
for _, elem in enumerate(lst_test):
    elems_amount[elem] += 1
for num in range(MAX_N + 1):
    lst_sorted.extend([num] * elems_amount[num])
print(*lst_sorted)
