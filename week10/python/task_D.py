from sys import setrecursionlimit
import threading
 
NOT_VISITED = 0
VISITED = 1
CLOSED = 2
DEFAULT_COLOR = 0
 
 
def dfs_toposort(vert, adj_lst, verts_visits, topo_sort):
    verts_visits[vert] = VISITED
    for vert_next in adj_lst[vert]:
        if verts_visits[vert_next] == NOT_VISITED:
            dfs_toposort(vert_next, adj_lst, verts_visits, topo_sort)
    verts_visits[vert] = CLOSED
    topo_sort.append(vert)  # topological sort
 
 
def dfs_components(vert, adj_lst, verts_color, color):
    verts_color[vert] = color
    for vert_next in adj_lst[vert]:
        if verts_color[vert_next] == DEFAULT_COLOR:
            dfs_components(vert_next, adj_lst, verts_color, color)
 
 
def main():
    n_verts, m_ribs = map(int, input().split())
    adj_lst = [[] for _ in range(n_verts)]  # graph
    rev_adj_lst = [[] for _ in range(n_verts)]  # reversed graph
    # construct adjacency list: 
    for _ in range(m_ribs):
        vert_1, vert_2 = map(int, input().split())
        adj_lst[vert_1 - 1].append(vert_2 - 1)  # oriented!
        rev_adj_lst[vert_2 - 1].append(vert_1 - 1)  # reversed, oriented!
    # DFS-1 for initial graph
    topo_sort = []
    verts_visits = [NOT_VISITED for _ in range(n_verts)]
    for vert in range(n_verts):
        if verts_visits[vert] == NOT_VISITED:
            dfs_toposort(vert, adj_lst, verts_visits, topo_sort)
    topo_sort.reverse()  # order for coloring
    # DFS-2 for reversed graph
    component_color = 0
    verts_color = [DEFAULT_COLOR for _ in range(n_verts)]
    for vert in topo_sort:  # using obtained from topological sort order
        if verts_color[vert] == DEFAULT_COLOR:
            component_color += 1
            dfs_components(vert, rev_adj_lst, verts_color, component_color)
    # counting ribs between components (in condensed graph)
    ribs_condenced = set()
    for vert_from in range(n_verts):
        for vert_to in rev_adj_lst[vert_from]:
            if not verts_color[vert_from] == verts_color[vert_to]:
                ribs_condenced.add((verts_color[vert_from], verts_color[vert_to]))
    print(len(ribs_condenced))
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # best constant
thread = threading.Thread(target=main)
thread.start()
