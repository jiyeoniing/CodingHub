# 동시에 여러군데에서 줄어듬. 즉 bfs
import sys
from collections import deque

input = sys.stdin.readline

# 치즈가 모두 녹아 없어지는 데 걸리는 시간
# 모두 녹기 한시간전에 남아있는 치즈 조각의 개수
# 구현 방법?
# 이미 방문한곳에 1이 없으면 처음부분이다.
def bfs(r,c):
    q = deque()
    q.append( (r,c) )  
    visited[r][c] = True
    cnt = 0

    while q:
        tr, tc = q.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = tr + dr
            nc = tc + dc
            # o인점들을 append해주어야 그 다음이 치즈인지 확인함.

            # 일단 범위안에 속하는지 
            if 0<=nr<N and 0<=nc<M:
                # 방문한적없고 0이면 0인지점 append
                if not visited[nr][nc] and ARR[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    
                # 방문한 적 없고 1이면 0다음 방문이니까 막 녹는 치즈 부분
                if not visited[nr][nc] and ARR[nr][nc] == 1:
                    visited[nr][nc] = True
                    ARR[nr][nc] = 0
                    cnt += 1
    return cnt


N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
result = []

while True:
        
        # 계속 초기화 시켜줘야함.
        visited = [[False]*M for _ in range(N)]
        ans = bfs(0, 0) # 1시간 후 치즈개수 출력
        result.append(ans)

        if ans == 0: # 이제 녹일 치즈 없다면
            break
        
print(len(result)-1)
print(result[-2])
