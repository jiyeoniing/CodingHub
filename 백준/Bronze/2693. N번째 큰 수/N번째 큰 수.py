T = int(input())

for i in range(T):
    a_lst = list(map(int, input().split()))
    a_lst.sort()
    print(a_lst[-3])