import sys
input = sys.stdin.readline

def check(lst, visited):

    same = 1
    for i in range(1, len(lst)):
        
        if lst[i-1] == lst[i]:
            same += 1

        # 1만큼 증가 했다면
        elif lst[i-1] +1 == lst[i] and same >= L and visited[i-L:i] == [False]*L:
            same = 1                 # 초기값 초기화
            visited[i-L:i]=[True]*L  # 경사로 건설

        # 감소 했다면 => 반대편에서 계산 될거나 이지점 기준으로 증가지점 발견 => 일단 초기화 
        elif lst[i-1] > lst[i]:
            same = 1

        # 이게 다 아니면
        else:
            return False
        
    # 무사히 통과
    return True


N, L = map(int, input().split())
ARR = [ list(map(int, input().split())) for _ in range(N)]

ARR_2 = []
for c in range(N):
    one = []
    for r in range(N):
        one.append(ARR[r][c])

    ARR_2.append(one)


ans = 0
for lst in ARR:
    visited = [False]*len(lst)
    if check(lst, visited) and check(lst[::-1], visited[::-1]):
        ans += 1

for lst in ARR_2:
    visited = [False]*len(lst)
    if check(lst, visited) and check(lst[::-1], visited[::-1]):
        ans += 1

print(ans)