# 녹색 옷 입은 애가 젤다지?

import sys
import heapq

# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop

input = sys.stdin.readline
INF = int(1E9)
i = 1
while True:
    N = int(input())

    if N == 0:
        break

    arr = [list(map(int,input().split())) for _ in range(N)]
    distance = [[INF]*N for _ in range(N)]

    # print(arr)

    def daikstra(r, c):
        q = []
        heapq.heappush(q, (arr[r][c], r, c))
        distance[r][c] = arr[r][c]  # 처음 시작점!!! (0,0)

        while q:
            (dist, tr, tc) = heapq.heappop(q)

            if distance[tr][tc] < dist:  # 이미 구해진 거리(distanc[tr][tc]) 와 새로 들어올 거리 비교 이미 작다면 pass
                continue

            for dr,dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = tr+dr
                nc = tc+dc
                if 0<=nr<N and 0<=nc<N and distance[nr][nc] > dist + arr[nr][nc]: # 이미구해진 거리 와 새로구해질 거리 비교
                    distance[nr][nc] = dist + arr[nr][nc]
                    heapq.heappush(q, (distance[nr][nc], nr, nc))

    daikstra(0,0)
    print(f'Problem {i}: {distance[N-1][N-1]}')
    i += 1