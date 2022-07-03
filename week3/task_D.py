MAX_LEN = 1e7  # maximum rope length [cm]
 
 
def get_rope_length(lengths, num_of_houses):
    left = 0
    right = int(MAX_LEN) + 1
    while right - left > 1:
        mid = (left + right) // 2
        ofv = 0  # objective function value
        for lng in lengths:
            ofv += lng // mid
        if ofv < num_of_houses:
            right = mid
        else:
            left = mid
    return left
 
 
n, k = map(int, input().split())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
print(get_rope_length(ropes, k))
