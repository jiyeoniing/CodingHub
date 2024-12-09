def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    st=-1
    for i in arr:

        if i!=st:
            answer.append(i)
        st = i
    return answer