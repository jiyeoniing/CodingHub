# 7576 토마토 - 골드5

# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 들어 있지 않은 칸

# 토마토가 모두 익을 떄까지의 최소 날짜를 출력
# 저장될때 부터 전부 1이라면 0을 출력
# 모두 익지 못하면 -1 츌력

from collections import deque

# 하루가 지나면 왼 오 앞 뒤 토마토가 익음
def bfs():

    q = deque()
    for r in range(N):
        for c in range(M):
            if ARR[r][c] == 1:
                visited[r][c] = 1
                q.append((r, c))


    while q:
        (tr, tc) = q.popleft()

        for (dr, dc) in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nr = tr + dr
            nc = tc + dc

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 :
                if ARR[nr][nc] == -1:
                    visited[nr][nc] = 1

                if ARR[nr][nc] == 0:
                    ARR[nr][nc] = 1
                    visited[nr][nc] = visited[tr][tc] + 1
                    q.append((nr, nc))
    # print(visited)
    # print(ARR)
    x = 0
    for lst in ARR:
        x += lst.count(0)

    return x

# M x N 상자의 크기
M, N = map(int, input().split())

ARR = [list(map(int, input().split())) for _ in range(N)]
visited = [ [0]*M for _ in range(N)]

ans = bfs()

# ans는 0의 개수 즉 다 익었는지 확인하는 것.
# 0이 없으면 다익은 것임!
#  이때 visited의 최댓값 -1을 출력하면 됨.
maxV = 0

if ans==0:
    for lst in visited:
        x = max(lst)
        if maxV < x:
            maxV = x
    print(maxV-1)
else:
    print(-1)