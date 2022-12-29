import math
 
INF = None
# graph
ADJ_LST = None
RIBS_LIST = None
# verts statuses
EX_PATH = "+"  # min path exists
NO_MIN_PATH = "-"
NO_PATH = "*"
NO_PARENT = -1
 
 
def dfs(vert, verts_marks):
    # dfs from the vert that is acievable from a negative cycle
    verts_marks[vert] = NO_MIN_PATH
    for vert_next in ADJ_LST[vert]:
        if not verts_marks[vert_next] == NO_MIN_PATH:
            dfs(vert_next, verts_marks)
 
 
def ford(n_verts, start):
    ans = [NO_PATH for _ in range(n_verts)]  # marking verts for answer
    ans[start] = EX_PATH
    # dp[vert]([k]) = minimal path length from start to vert (containing k ribs)
    dp = [INF for _ in range(n_verts)]
    parent = [NO_PARENT for _ in range(n_verts)]
    dp[start] = 0
    
    for k in range(1, n_verts):
        for vert_from, vert_to, weight in RIBS_LIST:
            if (dp[vert_to] > dp[vert_from] + weight) and (not dp[vert_from] == INF):
                ans[vert_to] = EX_PATH  # have a path to vert_to from start vert!
                parent[vert_to] = vert_from  # update parent
                dp[vert_to] = dp[vert_from] + weight  # max(-INF, dp[vert_from] + weight)
 
    # check if cycle exists and mark vertices "status"
    for vert_from, vert_to, weight in RIBS_LIST:
        if (dp[vert_to] > dp[vert_from] + weight) and (not dp[vert_from] == INF):
            # vert_to is achievable from a nedative cycle!
            if not ans[vert_to] == NO_MIN_PATH:
                # run dfs and mark child verts as achievable from negative cycle
                dfs(vert_to, ans)
                
                # going backwards and marking verts as acievable from negative cycle
                vert = vert_to
                for _ in range(n_verts):
                    vert = parent[vert]
                    if (not ans[vert] == NO_MIN_PATH) and (not vert == NO_PARENT):
                        ans[vert] = NO_MIN_PATH  # also acievable
                        dfs(vert, ans)  # running dfs if we have other childs except previous
                    else:
                        break  # vert is already marked      
 
    # print answer for distances to verts from the start vert
    for vert in range(n_verts):
        if ans[vert] == EX_PATH:
            print(dp[vert])
        else:
            print(ans[vert])
 
            
n_verts, m_ribs, vert_start = map(int, input().split())
# also construct adjacency list: ADJ_LST[vert - 1] = [neighbor_i, ...]
ADJ_LST = [[] for _ in range(n_verts)]
# ribs list
RIBS_LIST = [None for _ in range(m_ribs)]
max_weight = -math.inf  # for maximal weight in graph
for rib_ind in range(m_ribs):
    vert_from, vert_to, weight = map(int, input().split())
    ADJ_LST[vert_from - 1].append(vert_to - 1)
    RIBS_LIST[rib_ind] = [vert_from - 1, vert_to - 1, weight]
 
    if max_weight < abs(weight):
        max_weight = abs(weight)
INF = (n_verts - 1) * max_weight + 1
 
ford(n_verts, vert_start - 1)  # start ford
