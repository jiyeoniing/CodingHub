import sys
from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(lst):
    
    q = deque()
    for r,c in lst:
        q.append((r,c))
        if ARR[r][c] == 'J':
            cnt[r][c] = 1
        else:
            fired[r][c] = 1
    
    while q:
        tr,tc = q.popleft()

        if ARR[tr][tc] == 'J' and (tr==0 or tr == N-1 or tc==0 or tc==M-1):
            return cnt[tr][tc]
        for i in range(4):
            nr = tr + dr[i]
            nc = tc + dc[i]
            if 0<=nr<N and 0<=nc<M and ARR[tr][tc] == 'J' and ARR[nr][nc] == '.' and cnt[nr][nc] == 0:
                ARR[nr][nc] = 'J'
                cnt[nr][nc] = cnt[tr][tc] + 1
                q.append((nr, nc))

            elif 0<=nr<N and 0<=nc<M and ARR[tr][tc] == 'F' and ARR[nr][nc] != '#' and fired[nr][nc] == 0:
                ARR[nr][nc]= 'F'
                fired[nr][nc] = fired[tr][tc] +1 
                q.append((nr, nc))
    return

N, M = map(int, input().split())
ARR = [list(input()) for _ in range(N)]

pos_lst = []
fire_lst = []

for r in range(N):
    for c in range(M):
        if ARR[r][c] == 'J':
            pos_lst.append((r,c))
        elif ARR[r][c] == 'F':
            fire_lst.append((r,c))

# J가 앞에 오도록 합치기
lst = pos_lst + fire_lst
# print(lst)

cnt = [[0]*M for _ in range(N)]
fired = [[0]*M for _ in range(N)]

result = bfs(lst)
if result:
    print(result)
else:
    print('IMPOSSIBLE')
