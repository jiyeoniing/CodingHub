from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ARR = [ list(map(int, input().split())) for _ in range(N)]
minC = -1e9

# 1. 2인점 birus 리스트에 담기  / 0인점 safe리스트에 담기
virus = []
safe = []

for r in range(N):
    for c in range(M):
        if ARR[r][c] == 2:
            virus.append( (r, c))

        elif ARR[r][c] == 0:
            safe.append( (r, c) )          


# 3. safeZone ARR에서 0 -> 1로 변환해주기 , BFS 돌리기
def bfs(safeZone):

    visited = [[False]*M for _ in range(N)]
    cnt = lenS -3 # 벽으로 변한 지점 3개 빼고 0인 지점들

    # 벽으로 바뀐 지점 1로 변환
    for r, c in safeZone:
        ARR[r][c] = 1

    # deque로 바이러스인 지점 다 넣어주고 bfs돌리기
    q = deque()

    for r, c in virus:
        q.append((r, c))
        visited[r][c] = True

    while q:
        tr, tc = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = tr + dr
            nc = tc + dc

            # 0인 지점들 중 감염되서 바뀌면 if문으로 들어감.
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and ARR[nr][nc]==0:
                visited[nr][nc] = True
                q.append((nr, nc))
                cnt -= 1


    # bfs 끝난 후 원래 점으로 초기화
    for r, c in safeZone:
        ARR[r][c] = 0

    return cnt

# 2. safe인 점들중 벽으로 만들 3점 뽑아주기 -> 조합 combi
lenS = len(safe)  # 0인 점 총 개수  
used = [False]*lenS

def combi(k, s, safeZone):
    #print(safeZone)
    global minC

    if k == 3:
        minC = max(minC, bfs(safeZone))
        return
    
    for i in range(s, lenS):
        if not used[i]:
            used[i] = True
            combi(k+1, i+1, safeZone+[safe[i]])
            used[i]=False

combi(0, 0, [])
print(minC)