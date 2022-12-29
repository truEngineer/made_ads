import math
 
 
NO_APPROPRIATE_IND = -1
 
 
def ascending_subsequence(sequence):
    seq_len = len(sequence)
    # for each cell saving a max len of ascending
    # subsequence which ends in [i]
    max_len_by_ind = [ 0 for _ in range(seq_len)]
    max_len_by_ind[0] = 1
    # for subsequence extraction
    prev_elem_ind = [ 0 for _ in range(seq_len)]
    prev_elem_ind[0] = NO_APPROPRIATE_IND  # no previous element
    # lent's start!
    for ind in range(1, seq_len):
        max_prev_len = -math.inf
        max_prev_ind = NO_APPROPRIATE_IND
        for ind_prev in range(ind):
            max_candidate = max_len_by_ind[ind_prev]
            if max_candidate > max_prev_len and sequence[ind] > sequence[ind_prev]:
                max_prev_len = max_candidate
                max_prev_ind = ind_prev  # index of element with maximal subs. len
        if not max_prev_ind == NO_APPROPRIATE_IND:
            max_len_by_ind[ind] = max_len_by_ind[max_prev_ind] + 1
            prev_elem_ind[ind] = max_prev_ind
        else:
            max_len_by_ind[ind] = 1
            prev_elem_ind[ind] = NO_APPROPRIATE_IND
    # print(*max_len_by_ind)
    # print(*prev_elem_ind)
    # for the subs. of the max len
    max_subs_len = max(max_len_by_ind)
    print(max_subs_len)
    extract_route(sequence, prev_elem_ind, max_len_by_ind.index(max_subs_len))
 
 
def extract_route(sequence, prev_elem_ind, start):
    subsequence = []
    this_elem_ind = start
    while not this_elem_ind == NO_APPROPRIATE_IND:
        subsequence.append(sequence[this_elem_ind])
        this_elem_ind = prev_elem_ind[this_elem_ind]
    print(*reversed(subsequence))
    
 
seq_len = int(input())
sequence = list(map(int, input().split()))
ascending_subsequence(sequence)
