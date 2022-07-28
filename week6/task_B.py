def find_max_path(mat, n, m):
    res = -1
    for i in range(m):
        res = max(res, mat[0][i])

    for i in range(1, n):
        res = -1
        for j in range(m):
            # When all paths are possible
            if 0 < j < m - 1:
                mat[i][j] += max(mat[i - 1][j], max(mat[i - 1][j - 1], mat[i - 1][j + 1]))
            # When diagonal right is not possible
            elif j > 0:
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j - 1])
            # When diagonal left is not possible
            elif j < m - 1:
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j + 1])
            # Store max path sum
            res = max(mat[i][j], res)
    return res


# Bottom-up function to count all paths from the first cell (0,0)
# to the last cell (M-1,N-1) in a given M x N rectangular grid
def countPaths(m, n):
    #  T[i][j] stores the number of paths from cell (0,0) to cell (i,j)
    T = [[0 for x in range(n)] for y in range(m)]
    # There is only one way to reach any cell in the first column i.e. to move down
    for i in range(m):
        T[i][0] = 1
    # There is only one way to reach any cell in the first row i.e. to move right
    for j in range(n):
        T[0][j] = 1

    # fill T in bottom-up manner
    for i in range(1, m):
        for j in range(1, n):
            T[i][j] = T[i-1][j] + T[i][j-1]

    # last cell of T stores the count of paths from cell(0,0) to cell(i,j)
    return T[m-1][n-1]


# Driver program to check findMaxPath
#N = 4
#M = 6
mat = ([[10, 10, 2, 0, 20, 4],
        [1, 0, 0, 30, 2, 5],
        [0, 10, 4, 0, 2, 0],
        [1, 0, 2, 20, 0, 4]])

print(find_max_path(mat, 4, 6))
