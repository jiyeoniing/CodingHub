# 1520 골드 3
# 내리막길

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
ARR = [[0]*(M+2)]+ [ [0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(M+2)]
# print(ARR)

# [  [0, 0, 0, 0, 0, 0, 0], 
#  [0, 50, 45, 37, 32, 30, 0], 
#  [0, 35, 50, 40, 20, 25, 0], 
#  [0, 30, 30, 25, 17, 28, 0], 
#  [0, 27, 24, 22, 15, 10, 0], 
#    [0, 0, 0, 0, 0, 0, 0]]

# visited = [[False]*(M+2) for _ in range(N+2)]
DP = [[-1]*(M+2) for _ in range(N+2)]
DP[1][1] = 1

def dfs(r,c):

    # 이미 경로 구했다면

    # 경로 아직 안구했다면
    if DP[r][c] == -1:
        DP[r][c] = 0
    
        for dr, dc in [(1,0), (0,1), (0,-1), (-1,0)]:
            nr = r+dr
            nc = c+dc
            # 내리막길이라면 앞의 값(nr,nc)이 현재 값보다 크다면
            if ARR[nr][nc] > ARR[r][c]:

                DP[r][c] += dfs(nr,nc)  # 조건에 맞는 네방향 경로수 더하기

    return DP[r][c]

# print(DP)
print(dfs(N,M))

