KMP_DELIMITER = "#"
 
 
def kmp_prefix(string, substring):
    substring_positions = []  # positions of substring in string
    len_substring = len(substring)
    # PREFIX FUNCTION
    string = substring + KMP_DELIMITER + string
    len_string = len(string)
    prefix = [0 for _ in range(len_string)]
    for ind in range(1, len_string):
        prev_prefix = prefix[ind - 1]
        while prev_prefix > 0 and string[prev_prefix] != string[ind]:
            prev_prefix = prefix[prev_prefix - 1]
        if string[prev_prefix] == string[ind]:
            prev_prefix += 1
        prefix[ind] = prev_prefix
        # DETECTING THE SUBSTRING IN THE STRING
        if prev_prefix == len_substring:
            knp_ind = ind - len_substring + 1
            ind_in_string = knp_ind - (len_substring + 1)
            substring_positions.append(ind_in_string + 1)
    return substring_positions
 
 
substring = input()
string = input()
positions = kmp_prefix(string, substring)
print(len(positions))
print(*positions)
