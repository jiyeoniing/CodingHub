from collections import deque
import sys
input = sys.stdin.readline

# 구역의 개수
N =int(input())
# 각 구역의 사람수 1~N번 구역
people = [0] + list(map(int, input().split()))

# 전체 인구수 합
sumAll = sum(people)

graph = [set() for _ in range(N+1)]
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for j in lst[1:]:
        graph[i].add(j)
        graph[j].add(i)
# print(graph) # [set(), {2, 4}, {1, 3, 5, 6}, {2, 4}, {1, 3}, {2}, {2}]



# 인구 1이상 N-1이하로 묶어서 1개만 구해서 차이구하기

# 1개일 때 나머지 묶이는지
# 2개 일때 나머지 묶이는지
# 1~N//2까지만 구해도 반대편 알아서 정해짐.

# 조합으로 만들고 두개의 인구에 대해 인접해 있는지 확인 후
# 차이 구하기

# 인접해 있을까?
def bfs(lst):

    q = deque()
    used = [False]*(N+1)

    start = lst[0]
    q.append(start)
    used[start] = True

    sumV = people[start]
    while q:

        t = q.popleft()

        for i in graph[t]:

            # 구한 팀 안에 속한 구역이면서 인접구역이면
            if i in lst and not used[i]:
                sumV += people[i]  # 선거구의 인구합
                used[i] = True  # 방문 표시
                q.append(i)

    return sumV

    

def combi(k, s, lst, sumP):

    if k==stop:

        # 상대팀도 구해줘야함.
        lst_2 = []
        for j in range(1, N+1):
            if j not in lst:
                lst_2.append(j)

        if sumP == bfs(lst) and (sumAll-sumP)==bfs(lst_2):
            ans = abs(sumP - (sumAll-sumP) )
            result.append(ans)
        return
    
    for i in range(s, N+1):
        if not visited[i]:
            visited[i] = True
            combi(k+1, i+1, lst+[i], sumP + people[i])
            visited[i]= False


# 결과 구하기
# ex) N=6이면 1~3명까지 이루어진 구역하나 만들어야함.
result = []

for i in range(1, N//2+1):
    visited = [False]*(N+1)
    stop = i
    combi(0, 1, [], 0)


if result:

    print(min(result))

else:
    print(-1)

