import sys
input = sys.stdin.readline


def dfs(i, now):
    global minV, maxV, add, minus, multi, divide

    if i == N:
        minV = min(minV, now)
        maxV = max(maxV, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+numbers[i])
            add += 1

        if minus > 0:
            minus -= 1
            dfs(i+1, now-numbers[i])
            minus += 1

        if multi > 0:
            multi -= 1
            dfs(i+1, now*numbers[i])
            multi += 1

        if divide > 0:
            divide -= 1
            dfs(i+1, int(now/numbers[i]))
            divide += 1




N = int(input())
numbers = list(map(int, input().split()))
add, minus, multi, divide = map(int, input().split())
minV = 10000000000
maxV = -10000000000

dfs(1, numbers[0])

print(maxV)
print(minV)