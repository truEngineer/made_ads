MAX_ROPE_LEN = int(1e8)
 
 
def f_houses(ropes, piece_len):
    # piece_len - length of rope piece
    # returns:
    # number of houses for which ropes[] is enough for giving a
    # for giving a piece of lenght 'piece len' to each of the hause
    return sum([rope // piece_len for rope in ropes])  # int number
 
 
def binary_search_by_answer(f, arr_for_f, val):
    # solving equation 'f(x) >= val' with accuracy 'acc'
    # val - number of houses
    RATIO = 2
    left = 0
    right = MAX_ROPE_LEN + 1
    while right - left > 1:
        ans = (left + right) // RATIO  # new length of the piece
        f_val = f(arr_for_f, ans)  # calculate the function
        if f_val < val: # f(right) < val, since 'f(l)' is monotonicaly decays
            right = ans
        else:
            left = ans
    return left
 
 
# function 'f': numer of rope pieces of length equal 'l'
# if 'l_i' - lenght of the i'th initial rope, then
# f(l) = sum(l_i // l) >= k (must be not less than the nuber of houses 'k')
# this function 'f(l)' is monotonicaly decays with increasing of 'l'!
# boundaries: max(l) = max(l_i), min(l) = 1
ropes_n, houses_n = map(int, input().split())
ropes_arr = []
for rope_i in range(ropes_n):
    ropes_arr.append(int(input()))
print(binary_search_by_answer(f_houses, ropes_arr, houses_n))
