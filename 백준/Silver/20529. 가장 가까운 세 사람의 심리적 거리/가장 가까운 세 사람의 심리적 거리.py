# 20529번
import sys
from collections import defaultdict

input = sys.stdin.readline

# 3명 정하기 조합
def combi(k, s, sumV):
    global minV

    if k==3:
        minV = min(minV, sumV)
        return
    
    for i in range(s, N):
        three[k] = students[i]
        cnt = 0
        for t in range(k):
            for j in range(4):
                if three[t][j] != three[k][j]:
                    cnt += 1
        combi(k+1, i+1, sumV+cnt)


T = int(input())
result = []

for _ in range(T):
    N = int(input())
    students = list(input().split())
    dic = defaultdict(int)
    for mbti in students:
        dic[mbti] += 1
    # print(dic)     # {'ENTJ': 1, 'INTP': 1, 'ESFJ': 1, 'ESFP': 4}

    sort_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    # [('ESFP', 4), ('INFP', 2), ('ENTJ', 1), ('INTP', 1), ('ESFJ', 1), ('ESTP', 1), ('ESTJ', 1), ('ISTJ', 1)]
    # print(sort_dic)

    for i in range( len(sort_dic) ):
        if sort_dic[i][1] >= 3:
            minV = 0
            break
        else:
            minV = 1e9
            three = ['mbti']*3
            combi(0, 0, 0)
            break
    print(minV)
            


    