# 소가길을건너간이유 골드3
# 14466

# 길을 건너지 않으면 만날 수 없는 소가 몇 쌍인지

import sys
from collections import deque

input = sys.stdin.readline

N, K, R = map(int, input().split())

dir = [ [ [] for _ in range(N) ] for _ in range(N)]
# print(dir)
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    dir[r1-1][c1-1].append( (r2-1, c2-1) )
    dir[r2-1][c2-1].append( (r1-1, c1-1) )


cows = []
for _ in range(K):
    r,c = map(int, input().split())
    cows.append((r-1,c-1))

def check(start, end):
    cow = deque([start])
    visited = [[False]*N for _ in range(N)]
    visited[start[0]][start[1]] = True

    while cow:
        tr, tc = cow.popleft()

        if (tr, tc) == end:
            return True
            

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr = tr+dr
            nc = tc+dc

            # 다리 없으면 계속 감!
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if (nr, nc) not in dir[tr][tc]:
                    cow.append((nr, nc))
                    visited[nr][nc] = True
                
    return False

cnt=0
for i in range(K):
    for j in range(i+1, K):

        if not check(cows[i], cows[j]):
            cnt+=1


print(cnt)