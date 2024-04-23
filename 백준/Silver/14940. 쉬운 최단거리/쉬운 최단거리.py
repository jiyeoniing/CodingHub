import sys
from collections import deque

input = sys.stdin.readline

def bfs(r,c):
    global visited

    q = deque()
    q.append((r,c))
    visited[r][c] = 0

    while q:
        tr, tc = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = tr+dr
            nc = tc+dc
            if 0<=nr<N and 0<=nc<M and ARR[nr][nc] == 1 and visited[nr][nc] == -1:
                visited[nr][nc] = visited[tr][tc] +1
                q.append((nr, nc))

N, M = map(int, input().split())
ARR = [ list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if ARR[r][c] == 2:
            sr, sc = r, c

bfs(sr, sc)
# print(visited)
for r in range(N):
    for c in range(M):
        if ARR[r][c] == 0 and visited[r][c] == -1:
            visited[r][c] = 0
        elif ARR[r][c] == 1 and visited[r][c] == -1:
            visited[r][c] = -1
for lst in visited:
    print(*lst)