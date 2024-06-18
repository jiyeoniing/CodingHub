# 1697 - 실버1

import sys
from collections import deque
input = sys.stdin.readline


# 수빈 N 동생 K
N, K = map(int, input().split())
maxN = 100001
visited = [0]*(maxN)
def bfs(N, K):
    q = deque()
    q.append(N)
    visited[N] = 1
    
    while q:

        t = q.popleft()
        if t == K:
            return visited[t]-1

        for d in [t, -1, +1]:
            nt = t+d
            if 0<=nt<maxN and not visited[nt]:
                visited[nt] = visited[t]+1
                q.append(nt)
    return

print(bfs(N, K))
# print(visited)