# possible answers of the system
LOWER, EQUAL, GREATER = -1, 0, 1
NUM_MIN = 1
 
 
def binary_search_interactive(num_max):
    left = NUM_MIN  # left boundary
    right = num_max  # right boundary
    if_right_ans = GREATER  # takes values -1, 0 or 1
    while not if_right_ans == EQUAL:
        # separates arr[left..right] in two equal parts
        middle = left + (right - left) // 2
        # interactive!
        print(middle)
        if_right_ans = int(input())
        # interactive ends :(
        if if_right_ans == LOWER:
            right = middle - 1  # since not the middle: right >= ans
        if if_right_ans == GREATER:
            left = middle + 1  # since not the middle: left <= ans
 
 
upper_boundary = int(input())
binary_search_interactive(upper_boundary)
