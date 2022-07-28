
class Graph:
    def __init__(self, nodes):
        self.nodes = list(nodes)
        self.edges = dict((n, dict()) for n in nodes)

    def add_edge(self, a, b, w):
        if a in self.nodes:
            self.edges[a][b] = w
        else:
            self.nodes.append(a)
            self.edges[a] = {b: w}

    def update_edge(self, a, b, d):
        if a not in self.nodes:
            self.edges[a] = dict()
            self.nodes.append(a)
        if b in self.edges[a]:
            self.edges[a][b] += d
        else:
            self.edges[a][b] = d

    def bfs(self, s, t):
        parent = dict()
        visited = set([s])
        queue = [s]
        while queue:
            a = queue.pop()
            for b in self.edges[a]:
                if b not in visited and self.edges[a][b] > 0:
                    queue.append(b)
                    visited.add(b)
                    parent[b] = a
        return (t in visited), parent

    def max_flow(self, s, t):
        residual = Graph(self.nodes)
        for a in self.nodes:
            for b in self.edges[a]:
                residual.add_edge(a, b, self.edges[a][b])
        flow = 0
        path, parent = residual.bfs(s, t)
        while path:
            path_flow = 21  # float("Inf")
            a = t
            while a != s:
                path_flow = min(path_flow, residual.edges[parent[a]][a])
                a = parent[a]
            flow += path_flow
            b = t
            while b != s:
                a = parent[b]
                residual.update_edge(a, b, -path_flow)
                residual.update_edge(b, a, path_flow)
                b = a
            path, parent = residual.bfs(s, t)
        return flow


n = int(input())
m = int(input())
source, sink = str(1), str(n)
g = Graph(range(1, n + 1))

for i in range(m):
    a, b, w = [k for k in input().split()]
    w = int(w)
    c = '%s+%s' % (a, b)
    g.update_edge(a, c, w)
    g.update_edge(c, b, w)
    g.update_edge(b, a, w)

max_flow = g.max_flow(source, sink)
print(max_flow)

# input:
# 2
# 2
# 1 2 1
# 2 1 3
# output: 4
