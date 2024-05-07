# 17144. 미세먼지 안녕!

# 1초 동안 미세먼지 4방향 확산
# 확산되는 양은 abs( 각 칸의 미세먼지 / 5 )
# 남은 미세먼지 = 원래양 - abs( 각 칸의 미세먼ㄴ지 / 5 )*확산된 방향의 개수

# 공기청정기 작동
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]

# 미세먼지 이동
def bfs(dirty):

    for r, c in dirty:
        now = ARR[r][c]

        #  4방향 중 확산 가능 지점들 +
        cnt = 0
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = r+dr
            nc = c+dc
            if 0<=nr<N and 0<=nc<M and ARR[nr][nc] != -1:
                newARR[nr][nc] += now//5
                cnt += 1
        ARR[r][c] -= (now//5)*cnt
    
    for r in range(N):
        for c in range(M):
            ARR[r][c] += newARR[r][c]


# 1. 공기청정기 위치 저장
robot = []
for r in range(N):
    if ARR[r][0] == -1:
        robot.append((r, 0))

t = 0
while t < T:

    # 미세먼지 들어있는 지점들 저장
    dirty = []
    for r in range(N):
        for c in range(M):
            if ARR[r][c] != 0 and ARR[r][c] != -1:
                dirty.append((r,c))
    # print(dirty)

    # 이동한 미세먼지 넣어줄 곳
    newARR = [ [0]*M for _ in range(N)]

    # 미세먼지이동
    bfs(dirty)

    # 공기청정기 작동
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # 처음꺼가 반시계 방향
    r = robot[0][0]
    c = robot[0][1]

    i = 0
    st = []
    st.append(0)    # 공기청정기 나올때 0으로 나옴.
    while True:
        r += dr[i]
        c += dc[i]
        if r == robot[0][0] and c == robot[0][1]:
            break
        if 0<=r<=robot[0][0] and 0<=c<M:
            st.append(ARR[r][c])
            ARR[r][c] = st.pop(0)
        else: # 범위 벗어나면 방향 교체
            r -= dr[i]
            c -= dc[i]
            i = (i+1)%4

    # 다음 꺼가 시계 방향
    r = robot[1][0]
    c = robot[1][1]

    i = 0
    st = []
    st.append(0)    # 공기청정기 나올때 0으로 나옴.
    while True:
        r += dr[-i]
        c += dc[-i]
        if r == robot[1][0] and c == robot[1][1]:
            break
        if robot[1][0]<=r<N and 0<=c<M:
            st.append(ARR[r][c])
            ARR[r][c] = st.pop(0)
        else: # 범위 벗어나면 방향 교체
            r -= dr[-i]
            c -= dc[-i]
            i = (i+1)%4
    t += 1

sumV = 0
for r in range(N):
    for c in range(M):
        sumV += ARR[r][c]

print(sumV+2)
# print(ARR)