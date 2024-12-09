def solution(s):

    st = []
    
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if len(st)>0:
                st.pop(-1)
            else:
                return False
    if len(st)>0 :
        return False
    else:
        return True