# 18870
# 좌표 압축

import sys
from collections import defaultdict
input = sys.stdin.readline

dict = defaultdict(int)

n = int(input())
lst = list(map(int, input().split()))

sortList = sorted(lst)

cnt = 0
for i in sortList:

    if i not in dict:
        dict[i] = cnt
        cnt+=1
        


for i in lst:
    print(dict[i], end=' ')



