# N, M 
# N개의 수 정렬
def perm(k):
    if k==M:
        print(*path)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            path[k] = numbers[i]
            perm(k+1)
            visited[i]= False


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False]*10001
numbers.sort()
path = [-1]*M 
perm(0)

