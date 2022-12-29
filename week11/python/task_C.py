WEIGHTS_MAT = None
# task condition
NO_RIB = 100_000
MAX_RIB = 10_000
# for marking and checking
INF = None
NO_PATH = -1
 
 
def floyd_negative_cycle(n_verts):
    dists = WEIGHTS_MAT  # changing global WEIGHTS_MAT!
    next_vert = [[NO_PATH for _ in range(n_verts)] for _ in range(n_verts)]
    # filling next_vert matrix by the initial ribs
    for i in range(n_verts):
        for j in range(n_verts):
            if abs(dists[i][j]) <= MAX_RIB:
                next_vert[i][j] = j
    # start floyd
    for mid in range(n_verts):
        for start in range(n_verts):
            for end in range(n_verts):
                if (dists[start][end] > dists[start][mid] + dists[mid][end]) and \
                   (not dists[start][mid] == NO_RIB) and (not dists[mid][end] == NO_RIB):
                    dists[start][end] = max(-INF, dists[start][mid] + dists[mid][end])
                    next_vert[start][end] = next_vert[start][mid]  # filling matrix
    find_negative_cycle(next_vert, n_verts)  # fing negative cycle and print the answer
 
 
def find_negative_cycle(next_vert_mat, n_verts):
    cycle_flag = False
    start_vert = None  # vert which will be an entry point in our cycle
    for vert_ind in range(n_verts):
        if WEIGHTS_MAT[vert_ind][vert_ind] < 0:  # check if vert in a cycle
            cycle_flag = True
            start_vert = vert_ind
            break
    # printing the result
    if not cycle_flag:
        print("NO")
    else:
        print("YES")
        cycle = [start_vert + 1]
        start_ind = 0
        next_vert = next_vert_mat[start_vert][start_vert]
        while not next_vert == start_vert:
            cycle.append(next_vert + 1)
            next_vert = next_vert_mat[next_vert][start_vert]
            # if get the vert which is already in the cycle[]
            if (next_vert + 1) in cycle:  
                # we have found anoter cycle: 
                # not from start_vert to start_vert
                # but from next_vert to next_vert!
                if WEIGHTS_MAT[next_vert][next_vert] < 0:
                    # check that the new cycle is negative
                    start_ind = cycle.index(next_vert + 1)
                    break
        print(len(cycle[start_ind:]))
        print(*cycle[start_ind:])
 
 
n_verts= int(input())
INF = n_verts * NO_RIB
WEIGHTS_MAT = [None for _ in range(n_verts)]
for vert_ind in range(n_verts):
    WEIGHTS_MAT[vert_ind] = list(map(int, input().split()))
floyd_negative_cycle(n_verts)
