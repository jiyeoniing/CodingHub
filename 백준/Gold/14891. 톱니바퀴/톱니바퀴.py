# 맞닿은 부분이 다른 극이면 회전함.
# 같은 극이면 회전안함.
import sys
from collections import deque
input = sys.stdin.readline

def change(result):
    for n, dr in result:
        wheel[n].rotate(dr)
        
def check(n, direction):
    # 시계방향이면
    if direction == 1:
        if not visited[n]:
            visited[n] = True
            # wheel[n].rotate(1)
            result.append((n, 1))
        # 나의 3시방향  오른쪽의 9시방향 다른면 회전
        if n+1 <=4 and not visited[n+1] and wheel[n][2] != wheel[n+1][6]:
            # wheel[n+1].rotate(-1)
            result.append((n+1, -1))
            visited[n+1] = True
            check(n+1, -1)
        # 나의 9시 방향과 왼쪽의 3시방향 다르면 회전
        if n-1 >= 1 and not visited[n-1] and wheel[n][6] != wheel[n-1][2]:
            # wheel[n-1].rotate(-1)
            result.append((n-1, -1))
            visited[n-1]=True
            check(n-1, -1)
    
    if direction == -1:
        if not visited[n]:
            visited[n] = True
            # wheel[n].rotate(-1)
            result.append((n, -1))
        # 나의 3시방향  오른쪽의 9시방향 다른면 회전
        if n+1 <=4 and not visited[n+1] and wheel[n][2] != wheel[n+1][6]:
            # wheel[n+1].rotate(1)
            result.append((n+1, 1))
            visited[n+1] = True
            check(n+1, 1)
        # 나의 9시 방향과 왼쪽의 3시방향 다르면 회전
        if n-1 >= 1 and not visited[n-1] and wheel[n][6] != wheel[n-1][2]:
            # wheel[n-1].rotate(1)
            result.append((n-1, 1))
            visited[n-1]=True
            check(n-1, 1)

    return
            
             

wheel = [[]] # 톱니바퀴 1번부터 시작이니까
for _ in range(4):
    wheel.append(deque(list(map(int, input().strip()))))

cnt = int(input())

# [1, 0, 1, 0, 1, 1, 1, 1]
#  12    3     6     9

# 방향 direction 1: 시계방향 -1:반시계방향
for _ in range(cnt):
    number, direction = map(int, input().split())
    visited = [False]*(5)
    result = []
    check(number, direction)
    change(result)

sumV = 0
for i in range(1, 5):
    if wheel[i][0] == 1:
        sumV += 2**(i-1)

print(sumV)
    

# 