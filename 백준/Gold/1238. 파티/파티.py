# 1238 파티

# N명의 학생
# M개의 단방향 도로
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dajikstra(start):

    result[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        price, ky = heappop(heap)

        for next_price, next in graph[ky]:

            baro = result[next]
            new_price = next_price + price

            if baro > new_price:
                result[next] = new_price
                heappush(heap, (new_price, next))

def dajikstraRevese(start):

    result_2[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        price, ky = heappop(heap)

        for next_price, next in reverseGraph[ky]:

            baro = result_2[next]
            new_price = next_price + price

            if baro > new_price:
                result_2[next] = new_price
                heappush(heap, (new_price, next))

N, M, X = map(int, input().split())
graph = [ [] for _ in range(N+1)]
reverseGraph = [ [] for _ in range(N+1)]
INF = 1e9
result = [INF]*(N+1)
result_2 = [INF]*(N+1)

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    reverseGraph[e].append((w,s))

dajikstra(X)
dajikstraRevese(X)
sumTwo = [-1]*(N+1)
for i in range(1,N+1):
    sumTwo[i] = result[i] + result_2[i]

print(max(sumTwo))