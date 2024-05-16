import sys
input = sys.stdin.readline
from collections import deque


# 욱제의 캐릭터는 (7, 0)에 있음.
# => 캐릭터의 위치(0,7)까지 이동해야함.

# .:빈칸    #:벽
N = 8

arr = [ list(input().strip()) for _ in range(N)]


now = deque()
now.append((7,0)) #시작위치

def move():
    while now:

        n = len(now)

        for _ in range(n):

            tr,tc = now.popleft()
            
            if arr[tr][tc] == '#':
                continue

            for dr, dc in [(0,0), (0,1), (0,-1), (1,0), (-1,0), (1,-1), (-1,1), (1,1), (-1,-1)]:
                nr = tr+dr
                nc = tc+dc

                if 0<=nr<N and 0<=nc<N and arr[nr][nc] == '.':
                    now.append((nr,nc))
                    if nr==0 and nc==7:
                        return 1

        arr.pop()
        arr.insert(0, ['.']*8)

    return 0

print(move())
    



# print(arr)