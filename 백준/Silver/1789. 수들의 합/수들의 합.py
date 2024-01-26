s = int(input())

s_0 = 0
i = 0
while True :
    if s_0 == s:
        break
    if s_0 > s:
        i -= 1
        break
    s_0 += i
    i += 1

print(i-1)