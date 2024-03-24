import sys

input = sys.stdin.readline

def perm(k, sumV, cnt):
    global ans
    
    # 합이 S도 아니고 S보다 크지도 않지만 다 돌았다면
    if k==N:
        if sumV == S and cnt>0:
            ans += 1
        return
    

    perm(k+1, sumV, cnt)
    perm(k+1, sumV+numbers[k], cnt+1)
    


# N개의 정수로 이루어진 numbers에서 부분수열중 원소를 다 더한 값이 S가 되도록
N, S = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort() # 그러면 더할수록 더 커지기만 함. 작아질 수 없음.
ans = 0
perm(0, 0, 0)
print(ans)