N_ABC = ord('z') - ord('a') + 1 # number of ABC letters (lowcase)
 
 
def substrings_counter(string, symbols):
    N = len(string)
    symbols_stat = letters_stat(symbols)
    
    start = 0
    end = 0
    # perform scanning (kinda)
    this_stat = letters_stat(string[0])  # consider the substring: string[start..end]
    result = 0
    while True:
        ord_ch = ord(string[end])  # last elements
        # if there are not enough letters in 'symbols' to construct the substring 
        if this_stat[ord_ch - ord('a')] > symbols_stat[ord_ch - ord('a')]:
            # delete first element from the substring
            this_stat[ord(string[start]) - ord('a')] -= 1
            start += 1           
        else:
            end += 1
            result += (end - start)  # add all subs with the last element
            if end < N:
                # add a new (next) element to the current substring (from the end)
                this_stat[ord(string[end]) - ord('a')] += 1
            else:  # terminal condition!
                break
    return result
 
 
def letters_stat(string):
    letters_amount = [0] * N_ABC
    for letter in string:
        letters_amount[ord(letter) - ord('a')] += 1
    return letters_amount
 
 
n, m = map(int, input().split())
grishas_string = input()
cards = input()
print(substrings_counter(grishas_string, cards))
