import sys
input = sys.stdin.readline

def dfs(start, end):
    st = []
    st.append((start, 0))
    visited[start] = True

    while st:
        s, current = st.pop()
        if s==end:
            return current
        for i, next in graph[s]:

            if not visited[i]:
                visited[i]=True
                st.append((i, current+next))
    return

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, distance = map(int, input().split())
    graph[a].append((b,distance))
    graph[b].append((a,distance))

# print(graph) #[[], [(2, 2), (4, 3)], [(1, 2)], [(4, 2)], [(3, 2), (1, 3)]]


for _ in range(M):
    visited = [False]*(N+1)
    start, end = map(int, input().split())
    print(dfs(start, end))


