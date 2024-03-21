def skill(start,link):
    global minV
    s = 0
    l = 0
    for i in start:
        for j in start:
            s += lst[i][j]
    for i in link:
        for j in link:
            l += lst[i][j]
    if minV > abs(s-l):
        minV = abs(s-l)


def combi(k,s):
    start = []
    link = []
    if k == N//2:
        # print(result)
        for num in result:
            if num >=0:
                start.append(num)
        for num in arr:
            if num not in start:
                link.append(num)
        skill(start,link)
        return

    for i in range(s,len(arr)):
        result[k] = i
        combi(k+1,i+1)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
arr = [i for i in range(N)]

result = [-1] * len(arr)
minV = 100000
combi(0,0)
print(minV)