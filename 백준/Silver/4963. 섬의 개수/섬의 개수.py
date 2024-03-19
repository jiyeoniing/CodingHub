# 4963. 섬의 개수

import sys
from collections import deque

input = sys.stdin.readline
dr = [1, -1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, 1, -1, 1, 1, -1, -1]

def bfs(r,c):
    q = deque()
    q.append( (r,c) )
    visited[r][c] = True

    while q:
        (tr, tc) = q.popleft()
        for i in range(8):
            nr = tr + dr[i]
            nc = tc + dc[i]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and ARR[nr][nc]==1:
                visited[nr][nc] = True
                q.append( (nr, nc))

    return 1

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    else:
        ARR = [ list(map(int, input().split())) for _ in range(N)]
        # print(ARR)
        visited = [[False]*M for _ in range(N)]
        # print(visited)
        cnt = 0
        for r in range(N):
            for c in range(M):
                if not visited[r][c] and ARR[r][c]==1:
                        x = bfs(r,c)
                        cnt += x
        print(cnt)
