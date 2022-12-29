import math
 
 
def levenshtein_dist(first_seq, second_seq):
    # saving in dp[i][j] the Levenshtein distance
    # between seq_1[0..i - 1] and seq_2[0..j - 1]
    first_len = len(first_seq)
    second_len = len(second_seq)
    lev_dist = [ [0 for _ in range(first_len + 1)] for _ in range(second_len + 1)]
    # start filling DP array
    for second_ind in range(second_len + 1):
        for first_ind in range(first_len + 1):
            # distances between [] and some seq is the len of the seq
            if second_ind == 0:
                lev_dist[second_ind][first_ind] = first_ind
                continue
            if first_ind == 0:
                lev_dist[second_ind][first_ind] = second_ind
                continue
            # if insert
            lev_ins = lev_dist[second_ind - 1][first_ind] + 1
            # if delete
            lev_del = lev_dist[second_ind][first_ind - 1] + 1
            # if change
            led_chg = lev_dist[second_ind - 1][first_ind - 1] + \
                      int(not first_seq[first_ind - 1] == second_seq[second_ind - 1])
            # DP update
            lev_dist[second_ind][first_ind] = min(lev_ins, lev_del, led_chg)
    # print(*lev_dist, sep="\n")
    print(lev_dist[-1][-1])
 
 
first_seq = input()
second_seq = input()
levenshtein_dist(first_seq, second_seq)
