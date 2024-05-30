n, m = map(int, input().split())

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            D[n] = D[n//i] + 1
            return False
    D[n] = 1
    return True
    
D = [0]*(m+1)
res = [False]*(m+1)
for i in range(2, m+1):
    res[i] = isPrime(i)

ans = 0
# print(D)
# print(res)
for i in range(n, m+1):
    if res[D[i]]:
        ans+=1

print(ans)