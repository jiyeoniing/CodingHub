def check(n, width, height, park):
    cnt=n*n
    
    for r in range(height-n+1):
        for c in range(width-n+1):
            
            for i in range(r, r+n):
                for j in range(c, c+n):
                    if park[i][j] =='-1':
                        cnt -=1
                        
            if cnt==0:
                return True
            else:
                cnt=n*n
    return False

def solution(mats, park):
    
    width=len(park[0]) # 공원 너비
    height=len(park) # 공원 높이
    mats.sort(reverse=True)
    answer=-1
    
    for n in mats:
        if check(n, width, height, park):
            answer=n
            return answer
            
    return answer