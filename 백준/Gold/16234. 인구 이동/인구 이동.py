import sys
from collections import deque

input = sys.stdin.readline
# NxN 크기의 땅 
# 1x1 : 한개의 나라 존재

# 이웃나라의 인구차이가 L명 이상 R명 이하라면 
# 국경선을 개방
# 열수 있는 국경선 다 개방 후 인구이동 시작
# 인접한 칸을 이용해 이동가능
# 연합인구의 수 // 연합을 이루고 있는 칸의 개수 

# 문제풀이
# 이동할 수 있는 칸들 다 구하기
# 즉 각 칸마다 차이 L, R사이 찾기
# 무슨점부터 시작해야하지??

def bfs(r, c):

    q = deque()
    q.append( (r,c) )
    visited[r][c] = True
    result.append((r,c)) # 연합지점 시작점

    while q:
        tr, tc = q.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = tr + dr
            nc = tc + dc
            # 연합되었을 때만 방문으로 표시하므로 조건 : 방문하지 않았을 때
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                
                x = abs(ARR[tr][tc] - ARR[nr][nc])

                # 국경선 개방 국가라면 
                if L <= x <= R:
                    visited[nr][nc] = True # 연합지점으로 이미 넣었다 : 방문지점 표시
                    result.append((nr, nc)) # 연합지점 다 넣어주기
                    q.append((nr, nc))

# 연합 하나씩 하려면 
def change(lst):
    sumV = 0
    for r, c in lst:
        sumV += ARR[r][c]

    for r, c in lst:
        ARR[r][c] = sumV // len(lst)


# input값 불러오기
N, L, R = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]

day = 0 # 인구이동 날짜 변수
# 국경선 열리는 나라들만 result에 저장됨.
# 한번 다 돌고 바뀌고 또 바뀌어야 함.
while True:
    flag = 0 # while문 종료지점 표시
    visited = [[False]*N for _ in range(N)] # 인구이동 날 바뀔때 마다 초기화.
    for r in range(N):
        for c in range(N):

            # 연합지점은 방문한게 되니까. 
            # 연합지점 아니면서 아직 연합지점 계산된 적 없다면
            if not visited[r][c]:
                result = [] # 함수 실행할 때마다 result초기화.
                bfs(r,c)  # 연합지점 찾기

                if len(result) == 1: # 연합지점이 없음
                    continue
                else:
                    change(result)  # 연합지점 값들 변경
                    flag = 1

    if flag == 1: # 연합지점 변경된거니까
        day += 1

    else: # 연합지점 이제 존재 하지 않음. 종료지점.
        break
            

print(day)
    


