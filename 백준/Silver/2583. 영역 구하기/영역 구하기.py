# 2583 영역구하기
import sys
from collections import deque

# 1의 영역을 구해야함.
def bfs(r,c):
     q = deque()
     q.append( (r,c) )
     visited[r][c] = True
     cnt = 1

     while q:
          tr, tc = q.popleft()
          for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
               nr = tr + dr
               nc = tc + dc
               if 0<= nr < N and 0 <= nc < M and not visited[nr][nc] and ARR[nr][nc] == 1:
                    cnt += 1
                    visited[nr][nc] = True
                    q.append( (nr, nc) )
     return cnt




N, M, K = map(int, input().split())
ARR = [[1]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for _ in range(K):
     c1, r1, c2, r2 = map(int, input().split())
     for r in range(r1, r2):
          for c in range(c1, c2):
               ARR[r][c] = 0

result = []
ans = 0
for i in range(N):
     for j in range(M):
          if not visited[i][j] and ARR[i][j] == 1:
               ans += 1
               result.append(bfs(i,j))


result.sort()
print(ans)
print(*result)

# [[1, 1, 1, 1, 0, 0, 1],
# [1, 0, 1, 1, 0, 0, 1],
# [0, 0, 0, 0, 1, 1, 1],
# [0, 0, 0, 0, 1, 1, 1],
# [1, 0, 1, 1, 1, 1, 1]]