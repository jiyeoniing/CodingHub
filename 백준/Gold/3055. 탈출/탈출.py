
import sys
from collections import deque
input = sys.stdin.readline

# bfs 물 먼저 이동 후 도치 이동 -> 물 이동 예정 칸에 고슴도치 갈 수 없으므로
def bfs(sr, sc):

    # 도치의 q
    q = deque()
    visited[sr][sc] = 1
    q.append((sr, sc))

    # 물도 저장
    for r, c in WATER:
        q.append((r,c))

    while q:
        tr, tc = q.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
            nr = tr + dr
            nc = tc + dc
            # 현재 값이 물일 때
            # 다음 지점이 도치지나온 곳이거나 아무것도 없으면 물이 이동함.
            if 0<=nr<N and 0<=nc<M and ARR[tr][tc] == '*' and (ARR[nr][nc] == '.' or ARR[nr][nc] == 'S'):
                ARR[nr][nc] = '*'
                q.append((nr, nc))

            # 현재 값이 고슴도치 위치 일때
            # 다음 지점이 도치 굴이거나 아무것도 없으면 도치가 이동함.
            elif 0<=nr<N and 0<=nc<M and ARR[tr][tc] == 'S' and (ARR[nr][nc] == '.' or ARR[nr][nc] == 'D'):
                visited[nr][nc] = visited[tr][tc] + 1
                ARR[nr][nc] = 'S'
                q.append((nr, nc))

N, M = map(int, input().split())
ARR = [list( input())[:M] for _ in range(N)]
# print(ARR)

# 1. 물의 위치 -> 리스트에 저장, 도치 위치, 굴 위치 저장
WATER = []
for r in range(N):
    for c in range(M):
        if ARR[r][c] == '*':
            WATER.append( (r,c) )
        
        # 고슴도치 시작지점
        if ARR[r][c] == 'S':
            sr, sc = r,c
        
        # 고슴도치 도착지점
        if ARR[r][c] == 'D':
            er, ec = r,c

# bfs
visited = [[0]*M for _ in range(N)]
bfs(sr, sc)

if visited[er][ec]:
    print(visited[er][ec]-1)
else:
    print('KAKTUS')

