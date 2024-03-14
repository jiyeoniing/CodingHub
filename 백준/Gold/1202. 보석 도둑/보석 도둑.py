# 1202 보석도둑

import heapq
import sys
input = sys.stdin.readline

# N개의 보석, K개의 가방
N, K = map(int, input().split())
rubi = []
for _ in range(N):
    kg, value = map(int, input().split())
    rubi.append( (kg, value) )
rubi.sort(key=lambda x: x[0]) # 무게가 가벼운 것부터 차례대로 넣어주기

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort() # 가방 무게 오름차순 정렬. 작은 것부터 차례로 늘려가면서 그래야 다 비교할 수 있음.

sumV = 0 # 보석 가격의 합
lst = []  # 작은 무게부터 보석의 가격 넣어줄 lst
i = 0 # 보석 인덱스
# 주의할 점 : 작은 것부터 넣어줘야 가방 바뀌고도 최고 가격 빼준 리스트에 그대로 추가해 줄 수 있음.
for bag in bags:

    while i < len(rubi) and rubi[i][0] <= bag:

        heapq.heappush(lst, -rubi[i][1])
        i += 1

    if lst:
        maxV = heapq.heappop(lst)
        sumV += -maxV

print(sumV)
 