import sys
input = sys.stdin.readline

def perm(k, s):
    if k == M:
        print(*path)
        return
    
    prev = 0
    for i in range(s, N):
        if prev != numbers[i]:
            prev = numbers[i]
            path[k] = numbers[i]
            perm(k+1, i)


# 서로다른 N개의 수에서 중복을 허용하여 M개를 고르는 경우의 수
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

path = [-1]*M

perm(0, 0)