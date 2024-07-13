# 23971 - 브론즈3
# ZOAC 4

import sys
input = sys.stdin.readline

# 한명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐있음
# 세로로 N칸 가로로 M칸 이상 비우고 앉아야함.

N, M, R, C = map(int, input().split())

import math

x = math.ceil( N/(R+1) )
y = math.ceil( M/(C+1) )

print(x*y)