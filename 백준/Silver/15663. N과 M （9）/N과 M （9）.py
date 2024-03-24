import sys
from collections import defaultdict

input = sys.stdin.readline

def perm(k):

    if k == M:
        x = str(path)
        if x not in dic.keys():
            dic[x] += 1
            print(*path)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path[k]= numbers[i]
            perm(k+1)
            visited[i]= False



N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
path = [-1]*M
dic = defaultdict(int)
visited = [False]*N

perm(0)