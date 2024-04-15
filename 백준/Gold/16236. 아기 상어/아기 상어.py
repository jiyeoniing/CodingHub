import sys
from collections import deque

input = sys.stdin.readline

# 0 :빈칸
# 1, 2, 3, 4, 5, 6 : 물고기 크기
# 9 : 아기상어 위치

# 아기 상어 물고기 먹기 bfs
def bfs(r,c):
    visited = [[0]*N for _ in range(N)]

    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    lst = []
    eat = 0

    while q:
        tr, tc = q.popleft()
        if eat == visited[tr][tc]:
            return lst, eat-1


        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = tr+dr
            nc = tc+dc
            # 나보다 작거나 같을 때 방문가능
            if 0<= nr <N and 0<=nc<N and visited[nr][nc]==0 and ARR[nr][nc] <= size:
                visited[nr][nc] = visited[tr][tc]+1
                q.append((nr,nc))

                # 나보다 작은 물고기 먹음
                if size > ARR[nr][nc] > 0:

                    lst.append((nr,nc))
                    eat = visited[nr][nc]

    # 먹을 물고기 못찾은 경우
    return lst, eat-1



N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]


# 1. 아기상어 위치 찾기 jr, jc
for r in range(N):
    for c in range(N):
        if ARR[r][c] == 9:
            jr, jc = r, c
            ARR[r][c] = 0

# 아기상어의 처음 크기
size = 2
cnt = ans = 0
while True:
    # true일동안 아기상어 잡어 먹을 수 있는 물고기 찾기
    lst, dist = bfs(jr, jc)

    if len(lst)==0:
        break
    lst.sort(key=lambda x: (x[0], x[1]))
    jr, jc = lst[0]
    ARR[jr][jc] = 0
    cnt += 1
    ans += dist
    if size==cnt:
        size += 1
        cnt = 0

print(ans)
