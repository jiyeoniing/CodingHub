import sys
input = sys.stdin.readline

# def fibo(n):

#     if n==0:
#         return 0
    
#     elif n==1:
#         return 1

#     return fibo(n-1) + fibo(n-2)
    

# for i in range(11):
#     print(fibo(i))

# print(fibo(int(input())))

n = int(input())

dp = [0]*(n+1)
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])