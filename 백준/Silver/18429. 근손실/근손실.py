import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = list(map(int, input().split()))


visited = [False]*N
path = [-1]*N
cnt = 0
def part(k, kg):
    global cnt

    if kg < 0:
        return

    if k == N:
        # print(path)
        # print(kg)
        cnt += 1
        return
    
    for i in range(N):
        if not visited[i]:
            path[k] = weight[i]
            visited[i] = True
            part(k+1, kg-K+weight[i])
            visited[i] = False



part(0, 0)
print(cnt)

