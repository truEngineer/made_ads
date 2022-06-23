def roman2decimal(string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    i, res = 0, 0
    while i < len(string):
        dgt1 = roman_dict[string[i]]
        if i + 1 < len(string):
            dgt2 = roman_dict[string[i + 1]]
            if dgt1 >= dgt2:
                res = res + dgt1
            else:
                res = res + dgt2 - dgt1
                i += 1
        else:
            res = res + dgt1
        i += 1
    return res


def sort_kings(arr, n):  # bubble sort based
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # sort kings by name
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # sort kings with the same names by number
            if arr[j][2] > arr[j + 1][2] and arr[j][0] == arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


num_of_kings = int(input())
kings = []
for _ in range(num_of_kings):
    name, roman = input().split()
    decimal = roman2decimal(roman)
    kings.append((name, roman, decimal))
sort_kings(kings, num_of_kings)
for king in kings:
    print(king[0], king[1])
