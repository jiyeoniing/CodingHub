# 15650. N과 M 2

# N, M
# 1~N까지 자연수 중에서 중복 없이 M개를 고른 수열 오른차순이어야함.
# 즉 조합임!
def permSort(k, s):
    
    if k==M:
        print(*result)
        return
    
    for i in range(s, N+1):

        if not visited[i]:
            visited[i] = True
            result[k]= i
            permSort(k+1, i+1)  # 이게 중요!!! 
            # 0번째까 2로 바뀌는 동시에 다음 실행 함수는 2보다 큰게 2뒤에 붙어야 하니까.
            visited[i] = False



N, M = map(int, input().split())
result = [-1]*M
visited = [False]*(N+1)
permSort(0, 1)

