import sys
from collections import deque

input = sys.stdin.readline

def bfs(r,c):

    q = deque()
    q.append((r,c))
    visited[r][c] = True
    color = ARR[r][c]

    while q:
        tr, tc = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = tr +dr
            nc = tc + dc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and ARR[nr][nc] == color:
                visited[nr][nc] = True
                q.append((nr, nc))

def bfs_2(r,c):

    q = deque()
    q.append((r,c))
    used[r][c] = True
    color = ARR[r][c]

    if color == 'G' or color == 'R':
        colors = ['G', 'R']
    else:
        colors = ['B']

    while q:
        tr, tc = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = tr +dr
            nc = tc + dc
            if 0<=nr<N and 0<=nc<N and not used[nr][nc] and ARR[nr][nc] in colors:
                used[nr][nc] = True
                q.append((nr, nc))

N =int(input())
ARR = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
used = [[False]*N for _ in range(N)]

cntA = 0
cntB = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r,c)
            cntA += 1
        if not used[r][c]:
            bfs_2(r,c)
            cntB += 1

print(cntA, cntB)

