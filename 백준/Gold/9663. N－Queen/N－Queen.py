import sys
input = sys.stdin.readline

# 가능 여부 확인
def check(lst, k):
    # print(lst)
    # 대각선일치하면 안됨
    for i in range(k):
        # 막 넣어준 곳과 맨처음곳 부터 비교
        # 같은 열에 있거나 lst[막 넣은 곳] - lst[index] == 둘이 뺀 값
        if lst[k] == lst[i] or abs(lst[k] - lst[i]) == abs(k-i):
            return False

    return True

# 순열
def part(k, lst):
    global cnt

    if k == N:
        cnt += 1
        return
    
    for i in range(N):

        if not visited[i] and check(lst+[i], k):
            visited[i] = True
            part(k+1, lst+[i])
            visited[i] = False
    return

cnt = 0
N = int(input())
visited = [False]*N
path = [0]*N
part(0, [])
print(cnt)