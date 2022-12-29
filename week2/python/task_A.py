import random
 
 
def split_safe_memory(a, left, right, pivot):  # split realization from previous HW
    # split array as: [left...right_less)..equal..(left_greater...right]
    right_less = left  # right boundary (not include) of the array part with elements < pivot
    left_greater = right  # left boundary (not include) of the array part with elements > pivot
    
    i = left  # start with the left element
    while i <= left_greater:
        if a[i] < pivot:
            a[right_less], a[i] = a[i], a[right_less]
            right_less += 1
            i += 1
        else:
            if a[i] > pivot:
                a[i], a[left_greater] = a[left_greater], a[i]
                left_greater -= 1
            else:
                i += 1
    return (right_less, left_greater)  # not included!
 
def find_k(a, left, right, k):
    if left - right == 1:
        return a[k]
    indPivot = random.randint(left, right)  # choose a random pivot from a[left..right]
    (right_less, left_greater) = split_safe_memory(a, left, right, a[indPivot])
    if k < right_less:
        return find_k(a, left, right_less - 1, k)
    else:
        if k > left_greater:
            return find_k(a, left_greater + 1, right, k)
        else:
            return a[right_less]
    
def main():
    n_clones = int(input())
    clones_iq = list(map(int, input().split()))
#     clones_iq = [1, 1, 1, 2, 2, 4, 5, 6, 6]
    m_req = int(input())  # number of requests
    for ind_req in range(m_req):
        i, j, k = map(int, input().split())
        ij_clones = clones_iq[i - 1:j].copy()
        print(find_k(ij_clones, 0, len(ij_clones) - 1, k - 1))  # '- 1' since the numeration is from zero!
    
    
main()
