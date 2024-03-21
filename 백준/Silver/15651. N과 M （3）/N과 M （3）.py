# 15651

# N, M
# 1~N까지의 자연수 중에서 M개를 고른 수열

def perm(k):
    if k==M:
        print(*result)
        return
    
    for i in range(1, N+1):
        result[k]=i
        perm(k+1)

N, M = map(int, input().split())
result = [-1]*(M)
perm(0)
