import sys
input = sys.stdin.readline

def findMy(x):

    result = -1
    while x > 0:

        # 땅 획득 실패
        if x in visited:
            result = x

        # 마지막까지 무사히 땅 획득
        if x==1:
            # 이제 내땅 x표시
            visited.add(x)
            print(visited)
            result = 0

        # 계속 부모로 들어감
        x //= 2

    return result


# N개의 땅  Q:오리 수
N, Q = map(int, input().split())
duck = [0]*(Q+1)

# 오리가 원하는 땅 저장
for idx in range(1, Q+1):
    duck[idx] = int(input())

visited = set()
for idx in range(1, Q+1):
    result = 0

    target = duck[idx]
    while target > 1:
        if target in visited:
            result = target

        target //= 2

    visited.add(duck[idx])
    print(result)