def perm(k,s):
    if k==M:
        print(*result)
        return
    
    for i in range(s, N+1):
        result[k] = i
        perm(k+1, i)

N, M = map(int, input().split())
result = [-1]*M
perm(0,1)