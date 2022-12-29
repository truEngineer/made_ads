def z_function(string):
    len_string = len(string)
    string_z = [0 for _ in range(len_string)]
    string_z[0] = -1
    # saving z-block with the rightest right boundary
    left = 0
    right = 0
    for ind in range(1, len_string):
        string_z[ind] = max(0, min(right - ind, string_z[ind - left]))
        while ind + string_z[ind] < len_string and \
              string[string_z[ind]] == string[ind + string_z[ind]]:
            string_z[ind] += 1
        if ind + string_z[ind] > right:
            left = ind
            right = left + string_z[ind]
    return string_z[1:]  # returning all except the first one
 
 
string = input()
print(*z_function(string))
