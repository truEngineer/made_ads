from sys import setrecursionlimit
import threading
 
# colors
NOT_VISITED = 0
VISITED = 1
CLOSED = 2
# graph
topo_sort = []  # verts order for topological sort
ADJ_LST = None
 
 
def dfs(vert, verts_visits):
    global topo_sort
    verts_visits[vert] = VISITED
    for vert_next in ADJ_LST[vert]:
        if verts_visits[vert_next] == NOT_VISITED:
            ans = dfs(vert_next, verts_visits)
            if not ans:  # got a cycle!
                return False
        elif verts_visits[vert_next] == VISITED:  # got a cycle!
            return False
    verts_visits[vert] = CLOSED
    topo_sort.append(vert + 1)  # for topological sort
    return True
 
 
def main():
    global ADJ_LST, topo_sort
    n_verts, m_ribs = map(int, input().split())
    ADJ_LST = [[] for _ in range(n_verts)]
    # construct adjacency list: 
    for _ in range(m_ribs):
        vert_1, vert_2 = map(int, input().split())
        ADJ_LST[vert_1 - 1].append(vert_2 - 1)  # oriented!
    # DFS    
    verts_visits = [NOT_VISITED for _ in range(n_verts)]
    for vert in range(n_verts):
        if verts_visits[vert] == NOT_VISITED:
            ans = dfs(vert, verts_visits)
            if not ans:  # if cycle
                break
    if ans:  # if no cycle
        topo_sort.reverse()
        print(*topo_sort)
    else:
        print(-1)
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # best constant
thread = threading.Thread(target=main)
thread.start()
