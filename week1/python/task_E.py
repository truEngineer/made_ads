import random
 
 
def split_safe_memory(a, left, right, pivot):
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
 
def qsort(a, left, right):
    if left >= right:
        return a
    indPivot = random.randint(left, right)  # choose a random pivot from a[left..right]
    (right_less, left_greater) = split_safe_memory(a, left, right, a[indPivot])
    qsort(a, left, right_less - 1)
    qsort(a, left_greater + 1, right)
    return a
    
def main():
    n = int(input())
    test_lst = list(map(int, input().split()))
    print(*qsort(test_lst, 0, len(test_lst) - 1))
    
    
main()
