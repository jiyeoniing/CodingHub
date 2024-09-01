# 촌수계산 - 실버 2

# 2644

import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
graph = [ [] for _ in range(n+1) ]
visited = [0]*(n+1)

m = int(input())
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)

def dfs(s, e, cnt):

    if visited[s]:
        return
    
    visited[s] = cnt

    for i in graph[s]:
        dfs(i, e, cnt+1)


dfs(a,b,1)
# print(visited)
print(visited[b]-1)