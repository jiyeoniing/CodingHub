import sys
from collections import deque

input = sys.stdin.readline


def bfs(r,c):

    q=deque()
    q.append( (r,c) )
    visited[r][c] = 1

    while q:
        tr, tc = q.popleft()


        if tr==N-1 and tc==M-1:
            return visited[tr][tc]
        
        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr = tr + dr
            nc = tc + dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and ARR[nr][nc]==1:
                visited[nr][nc] = visited[tr][tc] +1
                q.append((nr, nc))


N, M = map(int, input().split())
ARR = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

print( bfs(0, 0) )