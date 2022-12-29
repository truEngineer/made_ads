from sys import setrecursionlimit
import threading
 
ROOT_NAME = "Polycarp".lower()
USERNAMES = [ROOT_NAME]
ADJ_LST = [[]]
DEFAULT_DEEP = 0
 
 
def dfs(vert, vert_father, verts_deep):
    verts_deep[vert] = verts_deep[vert_father] + 1
    for vert_next in ADJ_LST[vert]:
        if verts_deep[vert_next] == DEFAULT_DEEP:
            dfs(vert_next, vert, verts_deep)
 
 
def main():
    global ADJ_LST
    n_reposts = int(input())
    # construct adjacency list: 
    for _ in range(n_reposts):
        user_1, _, user_2 = input().split()  # user_2 exists!
        user_1 = user_1.lower()
        user_2 = user_2.lower()
        ind_2 = USERNAMES.index(user_2)
        if user_1 not in USERNAMES:
            USERNAMES.append(user_1)
            ADJ_LST.append([])
            ind_1 = len(USERNAMES) - 1
        else:
            ind_1 = USERNAMES.index(user_1)
        ADJ_LST[ind_2].append(ind_1)  # rib from initial poster to reposter!
 
    # list of depps for each vert   
    verts_deep = [DEFAULT_DEEP for _ in range(len(ADJ_LST))]
    # starting from root!
    dfs(0, 0, verts_deep)
    print(max(verts_deep))  # find the deepest
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # best constant
thread = threading.Thread(target=main)
thread.start()

