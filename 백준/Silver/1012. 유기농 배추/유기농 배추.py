import sys
from collections import deque
input = sys.stdin.readline

def bfs(r,c):

    q = deque()
    q.append((r,c))
    visited[r][c] = True

    while q:
        tr, tc = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = tr +dr
            nc = tc + dc
            if 0<= nr<N and 0<=nc<M and not visited[nr][nc] and ARR[nr][nc]==1:
                visited[nr][nc] = True
                q.append((nr, nc))

    return 1

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    ARR = [[0]*M for _ in range(N)]
    for _ in range(K):
        # 배추 위치 1로 저장
        r, c = map(int, input().split())
        ARR[r][c] = 1

    # 필요한 배추흰지렁이 개수
    cnt = 0

    visited = [[False]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and ARR[r][c] == 1:
                cnt += bfs(r,c)   # 인접지점 다 visited True로 변경하는 bfs


    print(cnt)