def perm(k):

    if k == M:
        print(*path)
        return
    
    for i in range(N):
        path[k] = numbers[i]
        perm(k+1)


    return
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
path = [-1]*M
perm(0)