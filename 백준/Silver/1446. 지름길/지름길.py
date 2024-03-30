from heapq import heappush, heappop
import sys

input = sys.stdin.readline

# N개의 지름길   D길이의 고속도로  D <= 100000
N, D = map(int, input().split())
# 시작점이 1이 아닐수 있음.
graph = [[] for _ in range(10001)]
# 그래서 graph에 각 점마다 원래 길인 (1, start+1) 추가
for i in range(D):
    graph[i].append((1, i+1))


INF = int(1e9)
# 인덱스 위치까지 누적합 저장 리스트
result = [INF]*1001


# 시작점 인덱스에 (가중치(지름길거리), 다음위치) 저장
for _ in range(N):
    s, e, w = map(int, input().split())
    graph[s].append( (w, e) )


def daijkstra(start):

    heap = []
    heappush(heap, (0, start))
    result[start] = 0

    while heap:

        distance, start = heappop(heap)

        # 이미 저장된 누적합보다 추가될 거리가 커져버리면 return
        if result[start] < distance:
            continue

        for distance_w, next in graph[start]:

            
            # 현재 next위치의 누적합
            baro = result[next]
            new_distance = distance + distance_w

            if baro > new_distance:
                result[next]=new_distance

                heappush(heap, (new_distance, next))


# 함수 돌리기
daijkstra(0)  
        
# 도착지점D에서의 최소값 출력.
print(result[D])

