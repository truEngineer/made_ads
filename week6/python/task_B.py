import math
 
 
START = "S"
DOWN = "D"
RIGHT = "R"
 
 
def greedy_turtle(size_y, size_x, field):
    # maximal profint on the way to this cell
    profit_field = [ [ -math.inf for _ in range(size_x)] for _ in range(size_y)]
    profit_field[1][1] = field[1][1]# start point - [1, 1]
    # for each cell stores the turn which was before acieving the cell
    route_field = [ [ None for _ in range(size_x)] for _ in range(size_y)]
    route_field[1][1] = START
 
    for ind_y in range(1, size_y):
        for ind_x in range(1, size_x):
            if not (ind_x == 1 and ind_y == 1):
                lefter_coins = profit_field[ind_y][ind_x - 1]
                upper_coins = profit_field[ind_y - 1][ind_x]
                if lefter_coins > upper_coins:
                    profit_field[ind_y][ind_x] = field[ind_y][ind_x] + lefter_coins
                    route_field[ind_y][ind_x] = RIGHT  # what turn was before the cell
                else:
                    profit_field[ind_y][ind_x] = field[ind_y][ind_x] + upper_coins
                    route_field[ind_y][ind_x] = DOWN  # what turn was before the cell
    # print(*profit_field, sep="\n")
    # print(*route_field, sep="\n")
    max_profit = profit_field[-1][-1]
    route = extract_route(size_y, size_x, route_field)
    return max_profit, route
    
    
def extract_route(size_y, size_x, route_field):
    route = ""
    ind_y = size_y - 1
    ind_x = size_x - 1
    this_cell = route_field[ind_y][ind_x]
    while not this_cell == START:
        route = this_cell + route
        if this_cell == DOWN:
            ind_y = ind_y - 1
        else:  # this_cell == RIGHT
            ind_x = ind_x - 1
        this_cell = route_field[ind_y][ind_x]
    return route
 
 
size_y, size_x = map(int, input().split())
# add an extra row on top and extra column at the left of the field
field = [[-math.inf for _ in range(size_x + 1)] for _ in range(size_y + 1)]
for ind_y in range(1, size_y + 1):
    field[ind_y][1:] = list(map(int, input().split()))
max_profit, route = greedy_turtle(size_y + 1, size_x + 1, field)
print(max_profit)
print(route)
