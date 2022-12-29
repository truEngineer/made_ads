def merge(lst1, lst2):
    n1 = len(lst1) # n1 <= n2 
    n2 = len(lst2)
    ind1 = 0
    ind2 = 0
    inv = 0
    lst_merge = [0] * (n1 + n2)
    while ind1 + ind2 < n1 + n2:
        if  ind1 == n1 or (ind2 < n2 and lst2[ind2] < lst1[ind1]):
            lst_merge[ind1 + ind2] = lst2[ind2]
            ind2 += 1
            inv += (n1 - ind1)
        else:
            lst_merge[ind1 + ind2] = lst1[ind1]
            ind1 += 1
    return lst_merge, inv
 
def merge_sort(lst):
    n = len(lst)
    inv = 0
    if n == 1:
        return lst, inv
    first_half = lst[:n // 2]
    secnd_half = lst[n // 2:]
    first_half, dInv1 = merge_sort(first_half)
    secnd_half, dInv2 = merge_sort(secnd_half)
    merged_lst, dInv3 = merge(first_half, secnd_half)
    inv = inv + dInv1 + dInv2 + dInv3
    return merged_lst, inv
 
 
n = int(input())
test_lst = list(map(int, input().split()))
sorted_lst, n_inv = merge_sort(test_lst)
print(n_inv)
