# 18428 감시피하기
# 골드 5

import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N = int(input())
ARR = [ list(input().split()) for _ in range(N)]

# print(ARR)

# T = 선생님 위치
# S = 학생 위치

T = deque()
S = []
W = []

for i in range(N):
    for j in range(N):

        if ARR[i][j] == 'T':
            T.append((i,j))
        elif ARR[i][j] == 'S':
            S.append((i, j))
        elif ARR[i][j] == 'X':
            W.append((i, j))


walls = []
for i in combinations(W, 3):
    walls.append(i)

# print(walls) 

def check():

    for (r,c) in T:

        for dr, dc in [ (0,1), (0, -1), (1,0), (-1,0)]:

            for i in range(1, N+1):
                tr = r + dr*i
                tc = c + dc*i

                if 0<=tr<N and 0<=tc<N and ARR[tr][tc]=='S':
                    return False
                elif 0<=tr<N and 0<=tc<N and ARR[tr][tc]=='O':
                    break
                    
    return True


def a():

    for wall in walls:

        for (r,c) in wall:
            ARR[r][c] = 'O'

        if check():
            return True

        for (r,c) in wall:
                ARR[r][c] = 'X'

    return False

if a():
    print('YES')
else:
    print('NO')