import sys
input = sys.stdin.readline

def newAvg(lst):
    
    sumV = 0
    for v in lst:
        v = (v/maxV)*100
        sumV += v
    
    avg = sumV / len(lst)

    return avg

N =int(input())
lst = list(map(int, input().split()))
maxV = max(lst)
print(newAvg(lst))