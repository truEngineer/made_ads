N_ABC = ord('z') - ord('a') + 1  # number of ABC letters (lowcase)
 
 
def kth_phase(words, k):
    words_sorted = [''] * len(words)
    elems_amount = [0] * N_ABC
    elems_pos = [0] * N_ABC
    for ind in range(n_words):
        elems_amount[ord(words[ind][-k]) - ord('a')] += 1
    for ind, _ in enumerate(elems_amount):
        elems_pos[ind] = sum(elems_amount[:ind])
    for word in words:
        ind_lett = ord(word[-k]) - ord('a')
        words_sorted[elems_pos[ind_lett]] = word
        elems_pos[ind_lett] += 1
    return words_sorted
 
 
n_words, len_word, k_fin = list(map(int, input().split()))
words = []
for ind in range(n_words):
    words.append(input())
for k in range(1, k_fin + 1):
    words = kth_phase(words, k)
print(*words, sep='\n')
