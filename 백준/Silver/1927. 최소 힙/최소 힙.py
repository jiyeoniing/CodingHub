# 1927.최소힙
# 실버 2
import heapq
import sys
input = sys.stdin.readline

# 연산의 개수
N = int(input())

# 배열 lst
lst = []

for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(lst, x)

    elif x==0:
        if not lst:
            print(0)
        else:
            ans = heapq.heappop(lst)
            print(ans)
