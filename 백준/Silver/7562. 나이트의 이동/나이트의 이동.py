# 7562. 나이트의 이동

import sys
input = sys.stdin.readline
from collections import deque


T=int(input())

for _ in range(T):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    cnt = 0

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        tr,tc = q.popleft()

        if tr==er and tc==ec:

            break


        for dr, dc in [(1,-2), (2,-1), (2,1), (1, 2), (-1, -2), (-2, -1), (-1,2), (-2,1)]:
            nr = tr+dr
            nc = tc+dc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[tr][tc] + 1


    print(visited[er][ec]-1)







