# 1926 그림
import sys
from collections import deque

input = sys.stdin.readline

def bfs(r,c):

    q = deque()
    q.append( (r,c) )
    visited[r][c] = True
    cnt = 1

    while q:
        tr, tc = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr = tr + dr
            nc = tc + dc
            if 0<= nr < N and 0<= nc < M and not visited[nr][nc] and ARR[nr][nc]==1:
                cnt += 1
                visited[nr][nc] = True
                q.append( (nr, nc) )

    return cnt

N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
visited = [ [False]*M for _ in range(N)]

ans = 0
result = []
for r in range(N):
    for c in range(M):
        if not visited[r][c] and ARR[r][c]==1:
            result.append( bfs(r,c) )
            ans += 1

if len(result)==0:
    print(ans)
    print(0)

else:
    print(ans)
    print(max(result))