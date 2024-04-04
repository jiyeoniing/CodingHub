# 빙산_골드4

from collections import deque
import sys
input = sys.stdin.readline

def bfs(r,c):

    q = deque()
    q.append((r,c))
    lst.append((r,c))
    used[r][c] = True

    while q:
        tr, tc = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = tr + dr
            nc = tc + dc
            if 0<=nr<N and 0<=nc<M and ARR[nr][nc] != 0 and not used[nr][nc]:
                used[nr][nc] = True
                q.append((nr, nc))
                lst.append((nr,nc))

    return 1


N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]

# 1. 0이 아닌 지점. 즉, 빙산인 곳 다 넣어주기
lst = []
for r in range(N):
    for c in range(M):
        if ARR[r][c] != 0:
            lst.append((r,c))

time = 0
while True:
    visited = [[False]*M for _ in range(N)]
    for r,c in lst:
        # 주변에 0인 개수 세줌.
        cnt = 0
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            # 만약 빼서 0이 되었는데 세주면 안됨. 빙산 중 방문점 표시해주기
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and ARR[nr][nc] == 0:
                cnt += 1

        # 나온 0의 개수 만큼 빼주기
        ARR[r][c] -= cnt
        if ARR[r][c] < 0:
            ARR[r][c] = 0
        visited[r][c] = True
    time += 1
    #print(ARR)/
    
    sumV = 0
    used = [[False]*M for _ in range(N)]
    lst = [] # 초기화 0이 아닌 지점만 보면 되니까.
    for r in range(N):
        for c in range(M): 
            if ARR[r][c] != 0 and not used[r][c]:
                sumV += bfs(r,c)


    #print(sumV)
    if sumV >= 2:
        ans = time
        break

    if not lst:
        ans = 0
        break

print(ans)