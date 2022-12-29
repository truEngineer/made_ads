import math
 
 
def greedy_grasshopper(n_bump, max_step, bump_add):
    bump_add.append(0)  # income for achieving the last bump
    # for each bump storing
    # 1. the max number of coins on the way to this bump
    # 2. the previously visited bump
    max_coins_list = [0 for _ in range(n_bump)]
    prev_bump_list = [0 for _ in range(n_bump)]
    # [0] - first bump
    # [n_bump - 1] - last bump
    for ind_bump in range(1, n_bump):
        # print(f"{ind_bump=}")
        prev_max_coins = -math.inf
        prev_max_ind = -1
        for prev_step in range(1, max_step + 1):
            prev_ind = ind_bump - prev_step
            if prev_ind >= 0:
                if max_coins_list[prev_ind] > prev_max_coins:
                    prev_max_coins = max_coins_list[prev_ind]
                    prev_max_ind = prev_ind
            else:
                break
        # found the previously visited bump to achieve max profit
        max_coins_list[ind_bump] = prev_max_coins + bump_add[ind_bump - 1]
        prev_bump_list[ind_bump] = prev_max_ind
    len_route, route = extract_route(prev_bump_list)
    return max_coins_list, len_route, route
 
 
def extract_route(prev_bump_list):
    reversed_route = [len(prev_bump_list)]  # last route point
    this_bump = prev_bump_list[-1]
    while not this_bump == 0:
        reversed_route.append(this_bump + 1)  # numbering from '1'!
        this_bump = prev_bump_list[this_bump]
    reversed_route.append(1)  # add the starting point
    return len(reversed_route) - 1, reversed(reversed_route)
 
 
n_bump, max_step = map(int, input().split())
bump_add = list(map(int, input().split()))
max_coins, n_steps, route = greedy_grasshopper(n_bump, max_step, bump_add)
print(max_coins[-1])
print(n_steps)
print(*route)
