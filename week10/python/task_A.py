from sys import setrecursionlimit
import threading
 
DEFAULT_COLOR = 0
ADJ_LST = None
 
 
def dfs(vert, verts_color, color):
    verts_color[vert] = color
    for vert_next in ADJ_LST[vert]:
        if verts_color[vert_next] == DEFAULT_COLOR:
            dfs(vert_next, verts_color, color)
 
 
def main():
    global ADJ_LST
    n_verts, m_ribs = map(int, input().split())
    ADJ_LST = [[] for _ in range(n_verts)]
    # construct adjacency list: 
    for _ in range(m_ribs):
        vert_1, vert_2 = map(int, input().split())
        ADJ_LST[vert_1 - 1].append(vert_2 - 1)
        ADJ_LST[vert_2 - 1].append(vert_1 - 1)
    # DFS    
    component_color = 0
    verts_color = [DEFAULT_COLOR for _ in range(n_verts)]
    for vert in range(n_verts):
        if verts_color[vert] == DEFAULT_COLOR:
            component_color += 1
            dfs(vert, verts_color, component_color)
    print(component_color)
    print(*verts_color)   
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # best constant
thread = threading.Thread(target=main)
thread.start()
