# 2468. 안전영역
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def bfs(r,c):
    
    q = deque()
    q.append( (r,c) )
    visited[r][c] = 1

    while q:
        (tr, tc) = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = tr + dr
            nc = tc + dc
            if 0<= nr < N and 0<= nc < N and visited[nr][nc]==0 and ARR[nr][nc] >= h:
                visited[nr][nc]= 1
                q.append( (nr, nc) )

    return 1


N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]
height = [False]*101
result = []
maxV = 0

for r in range(N):
    for c in range(N):
        h = ARR[r][c]
        if not height[h]:
            height[h] = True
            sumV = 0 # 각 높이에서의 안전영역 개수
            visited = [ [0]*N for _ in range(N)]

            
            for i in range(N):
                for j in range(N):
                    if visited[i][j] == 0 and ARR[i][j] >= h:
                        sumV += bfs(i, j)


            if maxV < sumV:
                maxV = sumV
print(maxV)

