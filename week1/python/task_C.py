def merge(lst1, lst2):
    n1 = len(lst1) # n1 <= n2 
    n2 = len(lst2)
    ind1 = 0
    ind2 = 0
    lst_merge = [0] * (n1 + n2)
    while ind1 + ind2 < n1 + n2:
        if  ind1 == n1 or (ind2 < n2 and lst2[ind2] < lst1[ind1]):
            lst_merge[ind1 + ind2] = lst2[ind2]
            ind2 += 1
        else:
            lst_merge[ind1 + ind2] = lst1[ind1]
            ind1 += 1
    return lst_merge
 
def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    first_half = lst[:n // 2]
    secnd_half = lst[n // 2:]
    return merge(merge_sort(first_half), merge_sort(secnd_half))
 
 
n = int(input())
test_lst = list(map(int, input().split()))
print(*merge_sort(test_lst))
