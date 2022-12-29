from random import randrange
 
 
def to_arabian(roma_n):
    ROMA_NUMS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    previous = roma_n[-1]
    res = ROMA_NUMS[previous]
    for current in roma_n[-2::-1]:
        if ROMA_NUMS[current] >= ROMA_NUMS[previous]:
            res += ROMA_NUMS[current]
        else:
            res -= ROMA_NUMS[current]
        previous = current
    return res
 
 
def compare_kings(king1, king2):
    name1, roma_num1 = king1.split()
    name2, roma_num2 = king2.split()
    if name1 == name2:
        if to_arabian(roma_num1) < to_arabian(roma_num2):
            return True  # king1 < king2
        else:  # suppose that there is no kings with both same: names and numbers!
            return False  # king1 > king2
    else:
        if name1 < name2:
            return True  # king1 < king2
        else:
            return False  # king1 > king2


def split_kings(a, pivot):  # safe_memory
    left = []
    right = []
    for i in range(len(a)):
        if compare_kings(a[i], pivot):
            left.append(a[i])
        else:
            right.append(a[i])
    return (left, right)

 
def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[randrange(0, len(a))]
        (left, right) = split_kings(a, pivot)
    return quick_sort(left) + quick_sort(right)
 
 
n = int(input())
kings = []
for i_king in range(n):
    kings.append(input())
# Test: ['Louis XLVII', 'Philippe II', 'Philip II', 'Louis VIII']
print(*quick_sort(kings), sep = "\n")
