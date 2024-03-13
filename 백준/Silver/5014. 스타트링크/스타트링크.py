from collections import deque

def bfs(S):
    q = deque()
    q.append(S)
    visited[S] = 1

    while q:
        x = q.popleft()

        if x == G:
            return visited[x]-1

        for dx in [U, -D]:
            nx = x + dx
            if 1 <= nx <= F and visited[nx] ==0:
                q.append(nx)
                visited[nx] = visited[x]+1

    return 'use the stairs'



F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)
ans = bfs(S)
print(ans)