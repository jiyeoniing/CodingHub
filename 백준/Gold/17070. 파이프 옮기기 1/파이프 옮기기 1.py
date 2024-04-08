
import sys
from collections import deque

input = sys.stdin.readline
        # 가로, 세로, 대각선
delta = [(0, 1), (1, 0), (1,1)]

direction = {
    0 : [0, 2],     # 가로일때
    1 : [1, 2],     # 세로일때
    2 : [0, 1, 2],  # 대각선 일때
}

def dfs(r,c,way):
    global ans

    if r==N-1 and c==N-1:
        ans += 1
        return

    # 방향이 가로라면
    if way == 0:
        # 가로로 갈때
        if 0<=r<N  and 0<=c+1<N  and ARR[r][c+1]==0:
            dfs(r,c+1,0)
        # 대각선
        if 0 <= r + 1 < N and 0 <= c + 1 < N and ARR[r + 1][c] == 0 and ARR[r][c+1]==0 and ARR[r + 1][c + 1] == 0:
            dfs(r+1,c+1,2)

    # 방향이 세로라면
    if way==1:
        if 0<=r+1<N and 0<=c<N and ARR[r+1][c]==0:
            dfs(r+1, c, 1)
        if 0 <= r + 1 < N and 0 <= c + 1 < N and ARR[r + 1][c] == 0 and ARR[r][c+1]==0 and ARR[r + 1][c + 1] == 0:
            dfs(r+1,c+1, 2)
    if way==2:
        # 가로로 갈때
        if 0 <= r < N and 0 <= c + 1 < N and ARR[r][c + 1] == 0:
            dfs(r, c + 1, 0)
        # 세로
        if 0<=r+1<N and 0<=c<N and ARR[r+1][c]==0:
            dfs(r+1, c, 1)
        # 대각선
        if 0 <= r + 1 < N and 0 <= c + 1 < N and ARR[r + 1][c] == 0 and ARR[r][c+1]==0 and ARR[r + 1][c + 1] == 0:
            dfs(r + 1, c + 1, 2)

N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]

# 가로방향 way = 0
ans = 0
dfs(0, 1, 0)
print(ans)

