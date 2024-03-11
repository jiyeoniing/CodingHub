N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

lst.sort()

ans = []
for x in lst:
    ans.append(x*N)
    N -= 1

print(max(ans))