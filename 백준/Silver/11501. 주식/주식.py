# 11501 실버 2
# 주식

# 3가지 중 1개의 행동을 함.
# 주식 하나를 산다.
# 원하는 만큼 가지고 있는 주식을 판다.
# 아무것도 안한다.

# 날별로 주식의 가격 알때, 최대 이익 구하기

# 마지막날 주식 가격이 앞의 날들보다 크다면 무조건 1개씩 사서 마지막에 다 팔면 최대 이익
# 주식 가격이 계속 떨어지면 아무것도 안하는 게 최대 이익 0임.

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    days = int(input())
    stocks = list(map(int, input().split()))
    # max_stock = max(stocks) # 최대 주가
    # # 총 이익 저장
    # save = 0

    # # 최대 주가보다 낮으면 일단 사고 최대 주가 나오면 다 팔기 그리고 새로 시작
    # money = 0
    # cnt = 0
    # for i in range(days):
    #     if stocks[i] < max_stock:
    #         money += stocks[i]
    #         cnt += 1
    #     elif stocks[i] == max_stock:
    #         mine = money
    #         money = max_stock*cnt # 현재 주가에 가진거 다 팔기
    #         money -= mine # 내가 샀던 가 빼면 이익임.

    #         save += money # 현재 이익 저장

    #         cnt = 0 # 다시 가진 주식 수 0개
    #         if i == days-1:
    #             break
    #         else:
    #             max_stock = max(stocks[i+1:])
    #             money = 0

    # print(save)
    stocks.reverse()
    maxV = stocks[0]
    sum = 0

    for i in range(1, days):
        # 다음날 주가 하락
        if stocks[i] > maxV:
            maxV = stocks[i]
            continue
        sum += maxV - stocks[i]
    print(sum)

        
    


