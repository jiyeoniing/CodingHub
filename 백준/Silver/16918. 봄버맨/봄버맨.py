import sys
input = sys.stdin.readline

# 1초 : 아무것도 하지 않음
# 2초 : 폭탄없는 모든 칸에 폭탄 설치
# 3초 : 3초전 설치된 폭탄 모두 폭발 => 폭발 후 다시 빈칸 됨.
# 1

# 폭탄 폭발 함수
def bfs(lst):
    # 폭탄 있는 점들 다 받아서 주변 폭발시키기

    for r,c in lst:
        ARR[r][c] = '.'
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            # 폭발했으니까 빈칸으로 변경시키기
            if 0<= nr<N and 0<=nc<M and ARR[nr][nc] == 'O':
                ARR[nr][nc] = '.'


N, M, TIME = map(int, input().split())
ARR = [list(input()) for _ in range(N)]

t = 1 # 처음 1초 아무것도 일어나지 않음
while t < TIME:

    t += 1 # 2초후 

    blst = []
    # 1. 폭탄 있는 점들 다 받기, 1초 후 폭탄 설치될 점들도 다 받기
    for r in range(N):
        for c in range(M):
            if ARR[r][c] == 'O':
                blst.append((r,c))
            else:
                ARR[r][c] = 'O'  # 2초후 빈칸 모두 폭탄 설치!!
    if t == TIME:
        break

    t +=1
    bfs(blst)  # 3초후
    # 다시 for문 면서 체크

for lst in ARR:
    print(''.join(lst), end='')
