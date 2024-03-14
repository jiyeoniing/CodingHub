import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

maxV = 0
for _ in range(N):
    x = lst.pop(0)
    value = x*(len(lst)+1)
    if maxV < value:
        maxV = value

print(maxV)