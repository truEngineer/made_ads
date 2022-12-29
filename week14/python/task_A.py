import math
 
 
ABC_FIRST = "a"
HASH_PRIME = 29
HASH_M = 999999000001
 
 
def abc_ind(char):
    return ord(char) - ord(ABC_FIRST) + 1
 
 
def hash_func(string):
    len_string = len(string)
    hash_substr = [0 for _ in range(len_string)]
    hash_substr[0] = abc_ind(string[0])
    powers = [1 for _ in range(len_string)]
    for ind in range(1, len_string):
        hash_substr[ind] = (hash_substr[ind - 1] * HASH_PRIME + abc_ind(string[ind])) % HASH_M
        powers[ind] = (powers[ind - 1] * HASH_PRIME) % HASH_M
    return hash_substr, powers
 
 
def get_hash(left, right, hash_lst, powers):
    if left == 0:
        return hash_lst[right]
    return (hash_lst[right] - (hash_lst[left - 1] * powers[right - left + 1]) % HASH_M + HASH_M) % HASH_M
 
 
string = input()
requests_num = int(input())
hash_lst, powers = hash_func(string)
 
for _ in range(requests_num):
    left1, right1, left2, right2 = map(int, input().split())
    if (right1 - left1 == right2 - left2) and \
       (get_hash(left1 - 1, right1 - 1, hash_lst, powers) == get_hash(left2 - 1, right2 - 1, hash_lst, powers)):
        print("Yes")
    else:
        print("No")
