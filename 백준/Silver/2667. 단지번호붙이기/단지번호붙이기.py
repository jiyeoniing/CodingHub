dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(r,c):
    q = []

    q.append( (r,c) )       # 빈 큐에 처음 1인 지점 넣어주기
    visited[r][c] = True    # 방문표시
    cnt = 1                 # 1인지점 세줄 cnt

    while q:
        (tr, tc) = q.pop(0)  # pop해주면서 4방향 조사

        for i in range(4):
            nr = tr + dr[i]
            nc = tc + dc[i]

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and ARR[nr][nc]==1: # 방문한적 없고 범위안에 있으면

                    visited[nr][nc] = True   # 방문표시 후 그 점 기준으로 방향 살펴야하므로 q에 넣어주기
                    q.append( (nr, nc) )
                    cnt += 1        # 1인지점 개수 세기

    return cnt

N = int(input())
ARR = [ list(map(int, input().strip())) for _ in range(N)]
visited = [ [False]*N for _ in range(N)] # 방문한 점 표시해줄 배열
ans = [] # 단지별 총수 넣어줄 리스트

for r in range(N):
    for c in range(N):
        if not visited[r][c] and ARR[r][c] == 1: # 방문하지 않았으면서 1일 때 bfs에 입력. 
            # 이웃한 1 다 세고 방문으로 표시되므로 if문으로 처음 만날때만 해주게 됨.
            result = bfs(r,c)
            ans.append(result)

ans.sort()
print(len(ans))
for x in ans:
    print(x)