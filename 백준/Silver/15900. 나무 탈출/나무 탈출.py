import sys
input = sys.stdin.readline

def bfs(root):

    ST = []
    ST.append(root)
    visited[root] = 1
    
    while ST:
        i = ST.pop()

        for t in graph[i]:
            if not visited[t]:
                visited[t] = visited[i]+1
                parent[t] = i
                ST.append(t)
    return

# def gameCount(node):
#     global cnt

#     if parent[node] == 1:
#         return 1
    
#     p = gameCount(parent[node])
#     return p


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
parent = [0]*(N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
# print(parent) # [0, 0, 1, 2, 2] # 마지막의 부모가 1인 것들만 보면 됨.
setAll = set(i for i in range(1, N+1))
setP = set(parent)
setS = setAll - setP
# print(setS) # 리프 노드만 출력


ans = 0
for i in list(setS):
    ans += visited[i]-1

if ans%2 == 0:
    print('No')
else:
    print('Yes')