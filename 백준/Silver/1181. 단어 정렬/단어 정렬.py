T = int(input())

lst = []
for i in range(T):
    lst.append(input())

total = []

for i in range(1,51):
    len_same=[]
    for k in lst:
        if len(k) == i:
            len_same.append(k)
          
    len_same = list(set(len_same))  
    len_same.sort()
    
    if len(len_same)>=1:
        total.extend(len_same)
        
for x in total:
    print(x)
    