import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ARR = list( list( input().rstrip() )for _ in range(N))
# print(ARR)

# 1행 1열부터 시작
maxV = -1
visited = [0]*128
visited[ord(ARR[0][0])] = 1

# print(visited)

#  최대라서 다 가봐야함 즉 dfs

def dfs(r, c, cnt):
    # print(memory)

    global maxV
    
    maxV = max(maxV, cnt)
 
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        nr = r+dr
        nc = c+dc
        if 0<=nr<N and 0<=nc<M and visited[ord(ARR[nr][nc])] == 0:
            
            # memory.append(ARR[nr][nc])
            visited[ord(ARR[nr][nc])] = 1
            # print(memory)
            dfs(nr, nc, cnt+1)
            visited[ord(ARR[nr][nc])] = 0
            # memory.pop()

    return 


dfs(0,0,1)
print(maxV)