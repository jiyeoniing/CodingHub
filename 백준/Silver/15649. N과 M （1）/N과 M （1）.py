# 15649

def perm(k):

    if k == M:
        print(*result)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            perm(k+1)
            visited[i] = False

    



# 길이가 M인 순열

N, M = map(int, input().split())
result = [-1]*(M)
visited = [False]*(N+1)
perm(0)