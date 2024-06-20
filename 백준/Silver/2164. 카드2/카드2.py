# 2164 - 실버4
# 카드 2

# N장의 카드 1~N까지 번호 
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
cards = deque()
for i in range(1, N+1):
    cards.append(i)

# cards.rotate(-1)
# print(cards)

while len(cards)> 1:
    cards.popleft()
    cards.rotate(-1)


print(*cards)
    

