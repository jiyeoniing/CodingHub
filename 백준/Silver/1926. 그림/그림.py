# 그림

import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(r,c, sumV):

    q = deque()
    q.append((r,c))
    visited[r][c] = True
    sumV += visited[r][c]

    while q:
        tr, tc = q.popleft()

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr = tr+dr
            nc = tc+dc
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and arr[nr][nc]==1:
                visited[nr][nc] = True
                sumV += visited[nr][nc]
                q.append((nr, nc))
                # print(visited)
    return sumV


sumList = []
for r in range(n):
    for c in range(m):

        if not visited[r][c] and arr[r][c]==1:
            x = bfs(r,c, 0)
            # print(x)
            sumList.append(x)


if sumList:
    print(len(sumList))
    print(max(sumList))

else:
    print(0)
    print(0)