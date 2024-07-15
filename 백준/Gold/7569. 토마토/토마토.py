import sys
input = sys.stdin.readline

from collections import deque

M, N, H = map(int, input().split())
graph = []

for _ in range(H):
    graph.append( [ list(map(int, input().split())) for _ in range(N)] )
# print(graph)

# [ [[0, 0, 0, 0, 0], 
#    [0, 0, 0, 0, 0], 
#    [0, 0, 0, 0, 0]], 

#     [[0, 0, 0, 0, 0], 
#      [0, 0, 1, 0, 0], 
#      [0, 0, 0, 0, 0]] ]

# 익은 토마토들의 인덱스 값 찾기
tomato = deque()
cnt = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            if graph[h][r][c] == 1:
                tomato.append( (h, r, c) )
            if graph[h][r][c] == 0:
                cnt += 1

# print('익지 않은 토마토', cnt)

def go():
    global cnt

    # 이미 모든 토마토 익은 상태면 0 출력
    if cnt == 0:
        return 0
    
    while tomato:

        th, tr, tc = tomato.popleft()

        if cnt == 0:
            # print(th, tr, tc)
            return graph

        for dh, dr, dc in [ (-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:

            nh = th+dh
            nr = tr+dr
            nc = tc+dc
            if 0<=nh<H and 0<=nr<N and 0<=nc<M and graph[nh][nr][nc]==0:
                cnt -= 1
                if cnt == 0:
                    return graph[th][tr][tc]
                graph[nh][nr][nc] = graph[th][tr][tc]+1 # 익은 토마토로 변경
                tomato.append( (nh, nr, nc) )


    return -1
    
print(go())