import sys
input = sys.stdin.readline

N = int(input())  #4
enter = []
for _ in range(N):
    enter.append(input()[:-1])

# print(enter)

out = []
for _ in range(N):
    out.append(input()[:-1])

# print(out)

ans = []
i = 0


for car in enter:

    if car in ans:
        continue

    while True:

        if car == out[i]:
            i+=1
            break


        if car != out[i]:
            ans.append(out[i])
        i += 1
            
# print(ans)
print(len(ans))
