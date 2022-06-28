def anagram_check(str1, str2, strl):
    # count sort based solution
    # any two anagrams will have the same number of a’s,
    # the same number of b’s, the same number of c’s, and so on ...
    numsym = 26  # number of letters in the alphabet

    # symbol counters
    cnt1 = [0] * numsym
    cnt2 = [0] * numsym

    for i in range(strl):
        ind1 = ord(str1[i]) - ord('a')  # 'a': first letter of the alphabet
        ind2 = ord(str2[i]) - ord('a')  # ord('a') = 97, ord('z') = 122
        cnt1[ind1] += 1
        cnt2[ind2] += 1

    j = 0
    flag = True  # anagram status
    while j < numsym and flag:
        if cnt1[j] == cnt2[j]:
            j += 1
        else:
            flag = False

    return flag


#length1, length2 = map(int, input().split())
#string1 = input()
#string2 = input()
#print(anagram_check(string1, string2, len(string1)))  # 26 possible characters


def count_letters2(arr):
    count = [0] * 26  # number of different letters
    # ord('z') - ord('a') + 1 = 26
    for let in arr:
        count[ord(let) - ord('a')] += 1
    # str = ''
    # for i in range(ord('z') - ord('a') + 1):
    #     str += chr(ord('a') + i) * alphArr[i]
    return count


def comp_substr2(arr, subarr):
    subarr = count_letters2(subarr)
    for i in range(26):  # number of different letters = len(arr)
        if subarr[i] > arr[i]:
            return False  # can't compose the substring: not enough letters
    return True


def count_letters_hist(arr, set_l, num_l):  # use 'usdLet' array based 'countSort'!
    hist = [0] * num_l  # array of numbers of different letters in 'str'
    for el in arr:
        hist[set_l.index(el)] += 1
    return hist


def comp_substr(arr, subarr, set_l, num_l):
    hist = count_letters_hist(subarr, set_l, num_l)
    for i in range(num_l):
        if hist[i] > arr[i]:
            return False  # can't compose the substring: not enough letters
    return True

import itertools


def get_substr_count(string, len_s, cards, num_c):
    substr_count = 0

    # window size = 1 (count all substrings with length 1)
    set_let = set(cards)
    for let in string:
        substr_count += let in set_let

    # window size from 2 to num_c
    for ws in range(2, num_c + 1):  # maximum ws = num_c
        combs = list(itertools.combinations(cards, ws))
        #print(combs)
        for i in range(0, len_s - ws + 1):
            #print(i)
            for cmb in combs:  # for cmb in combs:
                if anagram_check(string[i : i + ws], cmb, ws):
                    # sorted(string[i : i + ws]) == sorted(cmb):
                    #print(cmb, "in")
                    #print("".join(cmb), "".join(string[i: i + ws]))
                    substr_count += 1
                    break  # to avoid extra addition

    return substr_count

# 26 12
# string = "abcccbdhddhhsbbbsbssssbcbb"
# cards = "aaabcccssbcd"
# output 70


def count_chars(string):
    hist = [0] * 26  # number of letters
    for ch in string:
        hist[ord(ch) - 97] += 1  # ord('a') = 97
    return hist


def calc_substr_count2(string, str_l, cards):
    crds_hist = count_chars(cards)  # cards histogram
    result = 0
    beg, end = 0, 1  # substring indexes

    while end < str_l + 1:
        substring = string[beg:end]

        for i, ch in enumerate(substring):
            ord_ch = ord(ch)

            if end - beg == 1 and crds_hist[ord_ch - 97] == 0:
                beg += 1
                end += 1
                break

            if substring.count(ch) > crds_hist[ord_ch - 97]:
                beg += 1
                break
            elif i == end - beg - 1:  # end of substring
                result += end - beg
                end += 1

    return result


def count_letters(string):
    hist = [0] * 26  # number of letters
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


#n, m = map(int, input().split())
#s = input()  # string
#t = input()  # cards
n, m = 10000, 10000
s = ['a'] * n
t = ['a'] * m
print(calc_substr_count(s, n, t))
#print(get_substr_count(s, n, t, m))


def get_substr_count2(string, len_s, cards, num_c):
    substr_count = 0

    # window size from 1 to num_c
    for ws in range(num_c + 1):  # maximum ws = num_c
        combs = list(itertools.combinations(cards, ws))
        #print(combs)
        for i in range(0, len_s - ws + 1):
            #print(i)
            for cmb in combs:  # for cmb in combs:
                if anagram_check(string[i : i + ws], cmb, ws):
                    # sorted(string[i : i + ws]) == sorted(cmb):
                    #print(cmb, "in")
                    #print("".join(cmb), "".join(string[i: i + ws]))
                    substr_count += 1
                    break  # to avoid extra addition

    return substr_count


"""def count_letters(str):
    hist = [0] * (ord('z') - ord('a') + 1)
    for let in str:
        hist[ord(let) - ord('a')] += 1
    return hist  # letters histogram

cards_hist = count_letters(t)
substr_count = 0

for i in range(n):
    cards_check = cards_hist.copy()
    if cards_check[ord(s[i]) - ord('a')] > 0:
        cards_check[ord(s[i]) - ord('a')] = cards_check[ord(s[i]) - ord('a')] - 1
        substr_count += 1
        for j in range(i + 1, n):
            if cards_check[ord(s[j]) - ord('a')] > 0:
                cards_check[ord(s[j]) - ord('a')] = cards_check[ord(s[j]) - ord('a')] - 1
                substr_count += 1
            else:
                break

print(substr_count)"""

"""set_let = list(set(s))  # letters set
num_let = len(set_let)  # letters count
chr_num_arr = count_letters(t, set_let, num_let)  # count_letters(t)
count_subs = 0
for i in range(n):
    for j in range(i, n):
        if comp_substr(chr_num_arr, s[i : j + 1], set_let, num_let):  # strIn[i:j + 1] – go through all substrings
            count_subs += 1
print(count_subs)"""
