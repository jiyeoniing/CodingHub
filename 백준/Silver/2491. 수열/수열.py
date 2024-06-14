# 2491.수열 - 실버4
# 6/14 (금)

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
# maxV = -1

# for i in range(N-1):

#     if lst[i] <= lst[i+1]:
#         cnt = 1
#         k = i
#         while k < N-1 and lst[k] <= lst[k+1]:
#             cnt += 1
#             k += 1

#     if lst[i] >= lst[i+1]:
#         cnt = 1
#         k = i
#         while k<N-1 and lst[k] >= lst[k+1]:
#             cnt += 1
#             k += 1
#     maxV = max(maxV, cnt)

# print(maxV)

min_dp = [1]*(N)
max_dp = [1]*(N)

for i in range(1, N):
    # 감소하는 수열
    if lst[i-1] >= lst[i]:
        min_dp[i] = min_dp[i-1]+1
    # 증가하는 수열
    if lst[i-1] <= lst[i]:
        max_dp[i] = max_dp[i-1]+1

maxV = max(max(max_dp), max(min_dp))
print(maxV)