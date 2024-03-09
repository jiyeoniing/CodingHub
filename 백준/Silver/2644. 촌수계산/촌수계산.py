# 2644. 촌수계산

# 부모 자식 : 1
# 나 할아버지 : 2
# 아버지형제 할아버지 : 1
# 나 아버지형제 : 3

# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]] 
def dfs(start, end, cnt):
    global ans

    if start == end:
        ans = cnt
        return

    for x in family[start]:
        if not visited[x]:
            visited[x] = True
            dfs(x, end, cnt+1)
            visited[x] = False


people = int(input())
family = [[] for _ in range(people+1)] # 이어진 관계 넣어줄 배열
visited = [False]*(people+1) # 들렸으면 갈필요없음
lst = list(map(int, input().split())) # 서로 다른 사람의 번호
m = int(input()) # 관계의 개수

# x , y = 부모의 번호, 나의 번호
for _ in range(m):
    (x, y) = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

# print(family) # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]   

ans = 0
dfs(lst[0], lst[1], 0)

if ans == 0:
    print(-1)

else:
    print(ans)