import sys
input = sys.stdin.readline

def blank_cnt(r,c):
    cnt = 0
    for dr, dc in [(1,0), (0, 1), (0,-1), (-1,0)]:
        nr = r+dr
        nc = c+dc
        if 0<=nr<N and 0<=nc<N and ARR[nr][nc] == 0:
            cnt += 1
    return cnt

def like_cnt(r,c):
    cnt = 0
    for dr, dc in [(1,0), (0, 1), (0,-1), (-1,0)]:
        nr = r+dr
        nc = c+dc
        if 0<=nr<N and 0<=nc<N and ARR[nr][nc] in mylike:
            cnt += 1
    return cnt



N = int(input())
ARR = [[0]*N for _ in range(N)]
graph = [[] for _ in range(N*N+1)]

lst = []
for _ in range(N*N):
    x = list(map(int, input().split()))
    graph[x[0]].extend(x[1:])
    lst.append(x)


# print(graph)


# 첫번째 사람은 무조건 가운데
i = 0
while i < N*N:
    now = lst[i][0]
    mylike = lst[i][1:]

    maxL = -1
    maxB = -1
    # 행 열 순서
    for r in range(N):
        for c in range(N):
            if ARR[r][c] == 0:
                blank = blank_cnt(r,c)  # 주변 빈칸의 개수
                like = like_cnt(r,c)    # 좋아하는 학생 수
                if maxL < like:
                    maxL = like
                    maxB = blank
                    result = (r,c)
                elif maxL==like:
                    if maxB < blank:
                        maxB = blank
                        result = (r,c)
    r,c = result
    ARR[r][c] = now
    i += 1

# print(ARR)
def satisfy(ARR):
    global sumV
    sumV = 0

    for r in range(N):
        for c in range(N):
            me = ARR[r][c]
            cnt = 0
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<N and 0<=nc<N and ARR[nr][nc] in graph[me]:
                    cnt += 1

            if cnt > 0:
                sumV += 10**(cnt-1)
    return sumV

# print(ARR)
print( satisfy(ARR) )


