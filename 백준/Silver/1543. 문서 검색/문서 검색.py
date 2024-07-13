import sys
input = sys.stdin.readline

word = input().strip()
x = input().strip()
n = len(x)


i=0
cnt = 0
while i < len(word)-n+1:
    if word[i:i+n] == x:
        cnt += 1
        i += n
    else:
        i+=1

print(cnt)


