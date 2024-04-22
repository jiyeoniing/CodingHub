import sys
input = sys.stdin.readline

def dfs(start):
    cnt = 0
    ST = []
    ST.append(start)
    visited[start] = True

    while ST:
        i = ST.pop()

        for t in graph[i]:
            if not visited[t]:
                visited[t] = True
                ST.append(t)
                cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    # N : 국가의 수 M : 비행기의 종류
    N, M = map(int, input().split())
    graph = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    # 방문지점 표시
    visited = [False]*(N+1)
    ans = dfs(1)
    print(ans)