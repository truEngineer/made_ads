def qsort(lst, lst_len):
    # lst - unsorted list
    # lst_len - length of the list (lst_len = len(lst))
    for i in range(lst_len):
        for j in range(lst_len - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(*lst)
 
 
n = int(input())
test_lst = list(map(int, input().split()))
qsort(test_lst, n)
