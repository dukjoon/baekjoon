import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)

def dfs(v):
    global counter
    counter += 1
    dfs_num[v] = dfs_low[v] = counter
    dfs_stack.append(v)
    visited[v] = True

    for u in graph[v]:
        if dfs_num[u] == 0:
            dfs(u)
        if visited[u]:
            dfs_low[v] = min(dfs_low[v], dfs_low[u])

    if dfs_num[v] == dfs_low[v]:
        component = []
        while True:
            u = dfs_stack.pop()
            visited[u] = False
            component.append(u)
            if u == v:
                break
        scc.append(component)

def is_satisfiable():
    for component in scc:
        for v in component:
            if -v in component:
                return False
    return True

def find_assignment():
    assignment = [None] * N
    for component in scc:
        for v in component:
            if assignment[abs(v) - 1] is None:
                assignment[abs(v) - 1] = 1 if v > 0 else 0
    return assignment

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[-u].append(v)
    graph[-v].append(u)

dfs_num = [0] * (2 * N + 1)
dfs_low = [0] * (2 * N + 1)
visited = [False] * (2 * N + 1)
dfs_stack = deque()
counter = 0
scc = []

for v in range(1, 2 * N + 1):
    if dfs_num[v] == 0:
        dfs(v)

if is_satisfiable():
    print(1)
    assignment = find_assignment()
    print(*assignment)
else:
    print(0)
