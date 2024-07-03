import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[0]*N for _ in range(N)]

# 사과의 위치
K = int(input())
for _ in range(K):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 9

# 방향 변환 횟수
L = int(input())
turn = []
for _ in range(L):
    X, C = input().split()
    turn.append((int(X), C))

# print(turn)

# 시계 방향 순으로
dr = [ 0, 1, 0, -1]
dc = [ 1, 0, -1, 0]

i = 0 # 방향인덱스
time = 0
tr,tc = 0,0 # 뱀의 초기 위치
que = deque()
que.append((tr, tc))

while True:

    time += 1
    tr += dr[i]
    tc += dc[i]

    if tr<0 or tr>=N or tc<0 or tc>=N or (tr, tc) in que:
        break
    
    # 사과 없다면
    if graph[tr][tc] == 0:
        que.append((tr,tc))
        que.popleft()

    # 사과 있다면
    elif graph[tr][tc] == 9:
        graph[tr][tc] = 0 # 사과 먹어s주고
        que.append((tr,tc))


    if turn and time == turn[0][0]:
        if turn[0][1] == 'D':
            i = (i+1)%4
        else:
            i = (i-1)%4

        turn.pop(0)

print(time)

