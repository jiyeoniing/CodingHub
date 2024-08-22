import sys
from itertools import combinations

input = sys.stdin.readline

# def combi(s, k):

#     if s==6:
#         print(*path)
#         return
    
#     for i in range(k,K):

#         if not visited[i]:
#             path[s] = lotto[i]
#             visited[i] = True
#             combi(s+1, i+1)
#             visited[i] = False

while True:
    lst = list(map(int, input().split()))
    K = lst[0]
    if K==0:
        break
    lotto = lst[1:]
    path = [0]*6
    visited = [False]*K
    # combi(0, 0)
    for i in combinations(lotto, 6):
        print(*i)
    print()
