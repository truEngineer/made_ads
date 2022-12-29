from sys import setrecursionlimit
import threading
 
VISITED = True
NOT_VISITED = False
TIME_IN = 0
ROOT = -1
 
 
def dfs(vert, father, adj_lst, verts_time_in, verts_up, verts_visits, articulation_pnts):
    global TIME_IN
    TIME_IN += 1
    verts_visits[vert] = VISITED
    verts_time_in[vert] = TIME_IN
    verts_up[vert] = TIME_IN  # initialize
    
    n_tree_childs = 0
    for vert_next in adj_lst[vert]:
        if vert_next == father:
            continue
        if verts_visits[vert_next] == NOT_VISITED:
            # find child in tree
            dfs(vert_next, vert, adj_lst, verts_time_in, verts_up, verts_visits, articulation_pnts)
            n_tree_childs += 1
            verts_up[vert] = min(verts_up[vert], verts_up[vert_next])
            if (verts_up[vert_next] >= verts_time_in[vert]) and (father != ROOT):
                articulation_pnts.append(vert + 1)  # find art. pnt!
        else:  # if visited
            # not a child (one of the previous vertices)
            verts_up[vert] = min(verts_up[vert], verts_time_in[vert_next])
    if father == ROOT and n_tree_childs > 1:
        articulation_pnts.append(vert + 1)  # find art. pnt!
 
 
def main():
    articulation_pnts = []
    n_verts, m_ribs = map(int, input().split())
    adj_lst = [[] for _ in range(n_verts)]
    # construct adjacency list: 
    for _ in range(m_ribs):
        vert_1, vert_2 = map(int, input().split())
        adj_lst[vert_1 - 1].append(vert_2 - 1)
        adj_lst[vert_2 - 1].append(vert_1 - 1)
    # DFS    
    component_color = 0
    verts_time_in = [None for _ in range(n_verts)]
    verts_up = [None for _ in range(n_verts)]
    verts_visits = [NOT_VISITED for _ in range(n_verts)]
    for vert in range(n_verts):
        if verts_visits[vert] == NOT_VISITED:
            dfs(vert, ROOT, adj_lst, verts_time_in, verts_up, verts_visits, articulation_pnts)
    articulation_pnts = list(set(articulation_pnts))
    print(len(articulation_pnts))
    print(*sorted(articulation_pnts))
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # best constant
thread = threading.Thread(target=main)
thread.start()
