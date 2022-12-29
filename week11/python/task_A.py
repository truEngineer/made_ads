import queue
 
 
MOVES = [(1, 2), (-1, 2), (1, -2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1)]
NOT_VISITED = -1
 
 
def chess_horse_bfs(x_st, y_st, x_fin, y_fin, size):
    parents = [[None for _ in range(size)] for _ in range(size)]
    turns = [[NOT_VISITED for _ in range(size)] for _ in range(size)]
 
    cells_queue = queue.Queue()
    turns[y_st - 1][x_st - 1] = 1
    cells_queue.put((x_st, y_st))
 
    while not cells_queue.empty():
        x, y = cells_queue.get()
        steps_to_xy = turns[y - 1][x - 1]
        for dx, dy in MOVES:
            x_next = x + dx
            y_next = y + dy
            if (0 < x_next <= size) and (0 < y_next <= size) \
               and (turns[y_next - 1][x_next - 1] == NOT_VISITED):
                cells_queue.put((x_next, y_next))
                # remember the parent (x, y) and the number of the cell (x_next, y_next)
                turns[y_next - 1][x_next - 1] = steps_to_xy + 1
                parents[y_next - 1][x_next - 1] = (x, y)
            if (x_next == x_fin) and (y_next == y_fin):
                n_cells, path = restore_path(parents, turns, x_st, y_st, x_fin, y_fin)
                return n_cells, path  # return answers
 
 
def restore_path(parents, turns, x_st, y_st, x_fin, y_fin):
    path = []
    n_cells = turns[y_fin - 1][x_fin - 1]
    x, y = x_fin, y_fin
    while not turns[y - 1][x - 1] == 1:
        path.append([x, y])  # add cell
        x, y = parents[y - 1][x - 1]
    path.append([x, y])  # add the start cell
    path.reverse()
    return n_cells, path
 
        
field_size = int(input())
FIELD = [[NOT_VISITED for _ in range(field_size)] for _ in range(field_size)]
x_start, y_start = map(int, input().split())
x_end, y_end = map(int, input().split())
n_cells, cells = chess_horse_bfs(x_start, y_start, x_end, y_end, field_size)
# print answer
print(n_cells)
for cell in cells:
    print(*cell)
