

import sys
from collections import deque

def bfs(r,c):
    global cntARR
    visited = [[-1]*M for _ in range(N)]

    q = deque()
    q.append((r,c))
    visited[r][c] = 0

    while q:
        tr, tc = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = tr+dr
            nc = tc+dc
            # 범위내에 있으며 한번도 방문하지 않은 곳 + 육지여야함.
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==-1 and ARR[nr][nc] == 'L':
                visited[nr][nc] = visited[tr][tc] +1
                cntARR[nr][nc] = max(visited[nr][nc], cntARR[nr][nc])
                q.append((nr, nc))

    return


N, M = map(int, input().split())
ARR = [list(input()) for _ in range(N)]

# 육지(L)만날 때마다 BFS돌려주며 CNT값 최대로 갱신시키기

cntARR = [ [-1]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if ARR[r][c] =='L':
            bfs(r,c)
# print(cntARR)

# 이제 최대인 지점 찾기
maxV = -1
for r in range(N):
    for c in range(M):
        if ARR[r][c] == 'L':
            maxV = max(cntARR[r][c], maxV)

print(maxV)