import sys

input = sys.stdin.readline

# N:나무의 수 M: 가져갈 나무의 길이
N, M = map(int, input().split())
trees = list(map(int, input().split()))

end = max(trees)
start = 0

while start <= end: 
    total = 0
    mid = (start+end)//2

    for tree in trees:
        if tree > mid:
            total += tree-mid

    if total >= M:
        result=mid
        start = mid+1

    elif total < M:
        end = mid-1

print(result)