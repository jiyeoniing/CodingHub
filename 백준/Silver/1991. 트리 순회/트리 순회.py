import sys
input = sys.stdin.readline

# A -> 1, B -> 2, C -> 3

# 알파벳 => 숫자
def changeN(alphabet):
    if alphabet =='.':
        return 0
    return ord(alphabet) - 64

# 숫자 => 알파벳
def changeA(number):
    return chr(number + 64)

# 전위 순회 루트/왼/오
def preOrder(root):

    print(changeA(root), end='')
    if left[root]: # 왼쪽 자식 있다면
        preOrder(left[root])

    if right[root]: # 왼쪽 다 보고 오른쪽 자식 있다면
        preOrder(right[root])

    return

# 중위 순회 왼/루트/오
def inOrder(root):

    if left[root]: # 왼쪽 자식 있다면
        inOrder(left[root])

    print(changeA(root),end='')

    if right[root]: # 왼쪽 다 보고 오른쪽 자식 있다면
        inOrder(right[root])

    return

# 후위 순회 왼/오/루트
def postOrder(root):

    if left[root]:
        postOrder(left[root])
    if right[root]:
        postOrder(right[root])
    print(changeA(root),end='')
    return


# 알파벳 최대 26인덱스
left = [0]*27
right = [0]*27

N = int(input())

for _ in range(N):
    p, c1, c2 = map(str, input().split())
    p, c1, c2 = changeN(p), changeN(c1), changeN(c2)
    left[p] = c1
    right[p] = c2

root = 1
preOrder(root)
print()
inOrder(root)
print()
postOrder(root)







