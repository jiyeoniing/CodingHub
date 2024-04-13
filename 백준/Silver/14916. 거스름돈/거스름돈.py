
# 거스름돈 액수 : N
N = int(input())

cnt= 0

# 5로 나누어 떨어질 수 있을 때 까지 2를 빼주기
while N>0:
    if N%5 == 0:
        cnt += N//5
        N = 0
        break

    else:
        N -= 2
        cnt += 1

if N == 0:
    print(cnt)

else:
    print(-1)
