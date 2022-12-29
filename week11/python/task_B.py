import heapq
import math
 
INF = math.inf
# arrays for graph
ADJ_LST = None
VISITED = None
DISTS = None
 
 
def dijkstra():
    global VISITED, DISTS
    # starting with the first vert
    queue = [(DISTS[0], 1)]
    heapq.heapify(queue)
    
    for ind_vert in range(1, n_verts):
        if len(queue) == 0:
            break
        dist, vert = heapq.heappop(queue)
        while VISITED[vert - 1] == True:  # searching a vert that is not visited yet
            dist, vert = heapq.heappop(queue)
        VISITED[vert - 1] = True  # marking as visited
        for next_vert, weight in ADJ_LST[vert - 1]:  # check all neighbors
            DISTS[next_vert - 1] = min(DISTS[next_vert - 1], dist + weight)
            heapq.heappush(queue, (DISTS[next_vert - 1], next_vert))
 
 
n_verts, m_ribs = map(int, input().split())
VISITED = [False for _ in range(n_verts)]  # flafs if vert is visited (True) or not (False)
DISTS = [INF for _ in range(n_verts)]  # distances from the root (1)
DISTS[0] = 0  # root vert
# construct adjacency list: ADJ_LST[vert - 1] = [[neighbor_i, weight_i], ...]
ADJ_LST = [[] for _ in range(n_verts)]
for _ in range(m_ribs):
    vert_1, vert_2, weight = map(int, input().split())
    ADJ_LST[vert_1 - 1].append((vert_2, weight))
    ADJ_LST[vert_2 - 1].append((vert_1, weight))
dijkstra()  # update DISTS with Dijkstra algo
print(*DISTS)
