# 과자나눠주기 실버2
# 16401


# M명의 조카, N개의  과자

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
lst = list(map(int, input().split()))


start = 1
end = max(lst)
result = 0
while start <= end:
    mid = (start+end)//2

    cnt = 0
    for i in lst:
        cnt += i//mid

    if cnt >= M:
        result = mid
        start = mid+1

    elif cnt < M:
        end = mid-1

print(result)
