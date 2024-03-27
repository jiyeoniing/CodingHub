# 치킨배달
# 0 : 없음 1 : 집 2: 치킨집
import sys
input = sys.stdin.readline

# NxN 행렬, M개의 치킨집을 골라야함. 그리고 가까운 치킨집이 그집의 치킨집거리.
N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
chick = []
home = []
minV = 1e9 # 치킨 도시 거리의 최소 
# 1. 1이면 home리스트에 넣기 2이면 chick 리스트에 넣기
for i in range(N):
    for j in range(N):
        if ARR[i][j] == 1:
            home.append( (i, j) )

        elif ARR[i][j] == 2:
            chick.append( (i, j) )

# print(chick) # [(1, 2), (2, 2), (4, 4)]
# print(home)  # [(0, 2), (1, 4), (2, 1), (3, 2)]

# 3. M개의 치킨집 뽑은 path와 home사이의 거리 합 구하는 함수
def distance(lstCH, lstHome):

    sumV = 0 #각 치킨집과 집사이의 거리의 합

    for hr, hc in lstHome: # 각 집 하나씩 불러와서 최소구하기
        minH = 1e9
        for i in lstCH:
            r, c = chick[i]
            value = abs(r-hr) + abs(c-hc)
            minH = min(value, minH) # 방금 구한 치킨집과의 거리와 전의 거리 중 최소인걸로 넣어주기

        sumV += minH

    return sumV

# 2. chick리스트에서 M개로 이루어진 조합 만들어주기
lenC = len(chick)
visited = [False]*(lenC)
numbers = [i for i in range((lenC))]
path = [0]*M # 치킨집들 중 M개를 뽑은 조합.

def combi(k, s):
    global minV

    if k == M:
        # print(path) # M개의 치킨집과 집들과의 거리의 합 구해야함.
        x = distance(path, home)
        minV = min(x, minV)
        return
    
    for i in range(s, lenC):
        if not visited[i]:
            visited[i]=True
            path[k] = numbers[i]
            combi(k+1, i+1)
            visited[i]= False
            
combi(0, 0)
print(minV)


