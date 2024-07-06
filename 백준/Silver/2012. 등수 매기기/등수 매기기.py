import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())

rank = [0]*(N+1)
for i in range(1, N+1):
    rank[i] = int(input())

rank.sort()
sumV = 0
for i in range(1, N+1):
    if rank[i] != i:
        sumV += abs(rank[i] - i)
print(sumV)


# dic = defaultdict(int)
# lst = []

# same = [] # 중복된것들
# for i in range(1, N+1):
#     n = int(input())
#     if n not in lst:
#         lst.append(n)
#     else:
#         same.append(n)  # 중복된 등수

    
# lst.sort()

# # 안나온 등수 찾기
# number = []
# for i in range(1, N+1):
#     if i not in lst:
#         number.append(i)  # 안나온 등수

# # 중복된 등수 와 안나온 등수 이용해 최소 구하기!!!!
# sumV = abs( sum(same) - sum(number) )

# print(sumV)






# 예상 등수로 말한 등수 넣기 => 그래야 같다고 하고 불만도=0됨. 

# 남은 사람들중 남은 등수와 조합해 최소 구하기










# 순열 사용으로 순서 정한 후 모두 다 계산.
# path = [0]*(N+1)
# visited = [False]*(N+1)

# minV = int(1e9)

# def part(k, badV):
#     global minV

#     if minV < badV:
#         return


#     if k == N+1:
#         minV = min(badV, minV)
#         # print(path)
#         # print(minV)
#         return
    
#     for i in range(1, N+1):
#         if not visited[i]:
#             visited[i]=True
#             path[k] = i # 순열 등수
#             part(k+1, badV+(abs(i - lst[k]))) 
#             visited[i] = False


# part(1,0)
# print(minV)
