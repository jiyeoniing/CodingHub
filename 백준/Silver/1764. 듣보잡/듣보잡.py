# 듣보잡

# 실버4

import sys
from collections import defaultdict, Counter
input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
for _ in range(N+M):
    lst.append(input()[:-1])

ans = Counter(lst)
# print(ans)
result = []
for i in ans:
    if ans[i] == 2:
        result.append(i)

result.sort()
print(len(result))
for s in result:
    print(s)