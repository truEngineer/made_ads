def count_sort_letters(arr, arr_size, ind):
    count = [0] * 27  # 26 unique letters + 1 dummy
    base = ord('a') - 1
 
    for item in arr:
        let = ord(item[ind]) - base
        count[let] += 1
 
    for i in range(1, 27):
        count[i] += count[i - 1]
 
    output = [0] * arr_size
    for item in reversed(arr):
        let = ord(item[ind]) - base
        output[count[let] - 1] = item
        count[let] -= 1
 
    return output
 
 
def radix_sort_letters(array, arr_size, item_size, p_num):
    # p_num: number of sort phases
    for p in range(p_num):
        array = count_sort_letters(array, arr_size, item_size - 1 - p)
    return array
 
 
n, m, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(input())
res = radix_sort_letters(data, n, m, k)
for item in res:
    print(item)
