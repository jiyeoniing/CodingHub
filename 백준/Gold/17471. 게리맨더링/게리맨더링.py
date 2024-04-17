
from collections import deque
import sys
input = sys.stdin.readline

# 두 선거구의 인구차이의 최솟값 구하기
# 나눌 수 없으면 -1 출력
minV = 1e9

N = int(input())
# 지역 1번 부터 시작
people = [0] + list(map(int, input().split()))
sumP = sum(people) # 전체합 구해두기
graph = [ set() for _ in range(N+1)]  # 그래프 
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for x in lst[1:]:
        graph[i].add(x)
    
# print(graph)  # 양방향임

# 연결 여부 확인
def check(team):

    cnt = len(team)-1
    visited = [False]*(N+1)

    q = deque()
    q.append(team[0])
    visited[team[0]] = True
    
    while q:
        i = q.popleft()

        for t in list(graph[i]):
            if t in team and not visited[t]:
                q.append(t)
                visited[t] = True
                cnt -= 1
    if cnt == 0:
        return True
    else:
        return False

def combi(k, s, teamA, sumA):
    global minV

    if k == K:
        teamB = []
        for j in range(1, N+1):
            if j not in teamA:
                teamB.append(j)

        if check(teamA) and check(teamB):
            minV = min(minV, abs(2*sumA - sumP))  # sumA - (sumP - sumA)
            return
    
    for i in range(s, N+1):
        combi(k+1, i+1, teamA+[i], sumA+people[i])


    return

# N=6이면 한 선거구 뽑을 때 1, 2, 3(5, 4, 3)까지만 뽑으면 다른 구 정해짐.
for K in range(1, N//2+1):
    K = K # 한 선거구 총 수
    visited = [False]*(N+1)
    combi(0, 0, [], 0)

if minV == 1e9:
    print(-1)
else:
    print(minV)
