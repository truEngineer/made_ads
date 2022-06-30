def count_letters(string):
    hist = [0]*26  # number of letters
    for let in string:
        hist[ord(let) - 97] += 1  # ord('a') = 97
    return hist
 
 
def calc_substr_count(string, strlen, cards):
    result = 0
    beg, end = 0, 1  # sliding window (substring)
    crds_hist = count_letters(cards)  # cards histogram 
    subs_hist = count_letters(string[0])  # current substring histogram
    
    while end < strlen + 1:
        # last char 'ord' in the current substring
        ord_ch = ord(string[end - 1])
        if subs_hist[ord_ch - 97] > crds_hist[ord_ch - 97]:
            beg += 1  # update substring begin
            # delete char from current substring hist 
            subs_hist[ord(string[beg - 1]) - 97] -= 1
        else:
            # increment number of matching substrings
            result += end - beg
            end += 1  # update substring end
            if end < strlen + 1:
                # add char to current substring hist
                subs_hist[ord(string[end - 1]) - 97] += 1
    return result
 
 
n, m = map(int, input().split())
s = input()  # string
t = input()  # cards
print(calc_substr_count(s, n, t))
